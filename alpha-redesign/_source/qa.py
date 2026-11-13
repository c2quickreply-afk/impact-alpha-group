"""Visual QA for the redesign. Needs the preview server running on :3000.
    python -I _source/qa.py [base_url] [--no-shots]
For every page x width it scrolls one screen at a time, screenshots each screen to
_source/qa/<page>/<width>/, and flags: horizontal overflow, clipped text,
elements invisible while on screen, broken images, console errors, internal
links that 404, a loader that doesn't dismiss, side bands > 7% at 1280/1920,
and the 375px page height in phone screens.
"""
import json, pathlib, sys
from playwright.sync_api import sync_playwright

BASE = next((a for a in sys.argv[1:] if a.startswith("http")), "http://localhost:3001").rstrip("/")
SHOTS = "--no-shots" not in sys.argv
OUT = pathlib.Path(__file__).resolve().parent / "qa"
PAGES = {"home": "/", "approach": "/approach", "about": "/about", "contact": "/contact", "privacy": "/privacy"}
WIDTHS = {375: 812, 768: 1024, 1280: 800, 1920: 1080, 2560: 1440}

CHECK_SCREEN = """(vh) => {
  const out = [];
  const els = document.querySelectorAll('[data-reveal],[data-stagger]>*,[data-hero]');
  for (const el of els) {
    const r = el.getBoundingClientRect();
    if (r.height < 4 || r.width < 4) continue;
    if (r.top < vh * 0.12 || r.bottom > vh * 0.88) continue;
    if (getComputedStyle(el).display === 'none') continue;
    let o = 1, n = el;
    while (n && n !== document.documentElement) { o *= +getComputedStyle(n).opacity; n = n.parentElement; }
    if (o < 0.9) out.push((el.className || el.tagName) + ' opacity=' + o.toFixed(2) + ' "' + (el.textContent||'').trim().slice(0,40) + '"');
  }
  return out;
}"""

CHECK_PAGE = """() => {
  const res = {overflow: null, clipped: [], broken: [], offscreen: [], band: null, height: document.documentElement.scrollHeight};
  const de = document.documentElement;
  if (de.scrollWidth > innerWidth + 1) {
    const wide = [];
    for (const el of document.querySelectorAll('body *')) {
      const r = el.getBoundingClientRect();
      if (r.right > innerWidth + 1 && r.width > 0 && getComputedStyle(el).position !== 'fixed') wide.push(el.tagName + '.' + el.className + ' right=' + Math.round(r.right));
      if (wide.length > 5) break;
    }
    res.overflow = de.scrollWidth + ' > ' + innerWidth + ' ' + wide.join(' | ');
  }
  const skip = el => el.closest('.loader,.mobile-menu,.topic-panel,.sr-only,.skip');
  for (const el of document.querySelectorAll('body *')) {
    if (skip(el)) continue;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const clipsX = /hidden|clip/.test(cs.overflowX), clipsY = /hidden|clip/.test(cs.overflowY);
    if (!(clipsX || clipsY)) continue;
    // does any text inside get cut by this box?
    const box = el.getBoundingClientRect();
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    let t;
    while ((t = walker.nextNode())) {
      if (!t.textContent.trim()) continue;
      const pe = t.parentElement;
      if (skip(pe)) continue;
      const pcs = getComputedStyle(pe);
      if (pcs.display === 'none' || pcs.visibility === 'hidden' || +pcs.opacity === 0) continue;
      const range = document.createRange(); range.selectNodeContents(t);
      for (const r of range.getClientRects()) {
        if (r.width < 1) continue;
        const cutY = clipsY && (r.top < box.top - 1 || r.bottom > box.bottom + 1);
        const cutX = clipsX && (r.left < box.left - 1 || r.right > box.right + 1);
        if (cutY || cutX) { res.clipped.push((el.className || el.tagName) + ' cuts "' + t.textContent.trim().slice(0, 40) + '"'); break; }
      }
      if (res.clipped.length > 12) break;
    }
  }
  // ellipsis / single-line overflow on text elements
  for (const el of document.querySelectorAll('h1,h2,h3,h4,p,a,span,li,b,small,label,button')) {
    if (skip(el)) continue;
    const cs = getComputedStyle(el);
    if (cs.display === 'none') continue;
    if (cs.textOverflow === 'ellipsis' && el.scrollWidth > el.clientWidth + 1) res.clipped.push('ellipsis ' + el.textContent.trim().slice(0, 40));
  }
  for (const img of document.images) if (img.complete && img.naturalWidth === 0) res.broken.push(img.src);
  // first content container inside main: how far is content from the edge?
  const c = document.querySelector('main .container');
  if (c) { const r = c.getBoundingClientRect(); const pl = parseFloat(getComputedStyle(c).paddingLeft); res.band = (r.left + pl) / innerWidth; }
  res.links = [...document.querySelectorAll('a[href]')].map(a => a.href).filter(h => h.startsWith(location.origin));
  res.images = [...document.querySelectorAll('img')].map(i => ({src: i.currentSrc.split('/').pop(), fit: getComputedStyle(i).objectFit, pos: getComputedStyle(i).objectPosition}));
  return res;
}"""


def main():
    issues, notes = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        links = set()
        for name, path in PAGES.items():
            for w, h in WIDTHS.items():
                ctx = b.new_context(viewport={"width": w, "height": h})
                pg = ctx.new_page()
                errs = []
                pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
                pg.on("pageerror", lambda e: errs.append(str(e)))
                pg.on("requestfailed", lambda r: errs.append("request failed " + r.url) if r.url.startswith(BASE) else None)
                tag = f"{name}@{w}"
                resp = pg.goto(BASE + path, wait_until="domcontentloaded")
                if not resp or resp.status != 200:
                    issues.append(f"{tag}: page status {resp.status if resp else 'none'}")
                try:
                    pg.wait_for_function("() => { const l = document.getElementById('loader'); return !l || getComputedStyle(l).visibility === 'hidden'; }", timeout=9000)
                except Exception:
                    issues.append(f"{tag}: loader did not dismiss within 9s")
                pg.wait_for_timeout(900)
                total = pg.evaluate("document.documentElement.scrollHeight")
                shot_dir = OUT / name / str(w)
                if SHOTS:
                    shot_dir.mkdir(parents=True, exist_ok=True)
                y, i = 0, 0
                while True:
                    pg.evaluate(f"window.scrollTo(0,{y})")
                    pg.wait_for_timeout(1300)
                    for bad in pg.evaluate(CHECK_SCREEN, h):
                        issues.append(f"{tag} screen {i}: invisible on screen: {bad}")
                    if SHOTS:
                        pg.screenshot(path=str(shot_dir / f"{i:02d}.png"))
                    if y + h >= total:
                        break
                    y += h; i += 1
                # scroll back up through the page to make sure reveals replay upward
                for yy in range(y, -1, -h):
                    pg.evaluate(f"window.scrollTo(0,{yy})")
                    pg.wait_for_timeout(1100)
                    for bad in pg.evaluate(CHECK_SCREEN, h):
                        issues.append(f"{tag} (scrolling up @{yy}): invisible on screen: {bad}")
                res = pg.evaluate(CHECK_PAGE)
                if res["overflow"]:
                    issues.append(f"{tag}: horizontal overflow {res['overflow']}")
                for c in sorted(set(res["clipped"])):
                    issues.append(f"{tag}: clipped text: {c}")
                for bimg in res["broken"]:
                    issues.append(f"{tag}: broken image {bimg}")
                for e in errs:
                    issues.append(f"{tag}: console: {e}")
                if w in (1280, 1920) and res["band"] is not None and res["band"] > 0.07:
                    issues.append(f"{tag}: side band {res['band']*100:.1f}% (> 7%)")
                if w == 375:
                    screens = res["height"] / h
                    notes.append(f"{name} @375: {screens:.1f} phone screens tall")
                    if name == "home" and screens > 11:
                        issues.append(f"{tag}: homepage is {screens:.1f} screens tall (> 11)")
                if w == 1280:
                    notes.append(f"{name} @1280 images: {res['images']}")
                    notes.append(f"{name} @1280 band {res['band']*100:.1f}%" if res['band'] else "")
                if w == 1920:
                    notes.append(f"{name} @1920 band {res['band']*100:.1f}%" if res['band'] else "")
                links.update(res["links"])
                ctx.close()
        # mobile menu: opens, closes, navigates
        ctx = b.new_context(viewport={"width": 375, "height": 812})
        pg = ctx.new_page()
        pg.goto(BASE + "/", wait_until="load")
        pg.wait_for_function("() => !document.getElementById('loader')", timeout=10000)
        pg.click("#burger"); pg.wait_for_timeout(400)
        if pg.evaluate("getComputedStyle(document.getElementById('mobileMenu')).visibility") != "visible":
            issues.append("mobile menu did not open")
        pg.keyboard.press("Escape"); pg.wait_for_timeout(400)
        if pg.evaluate("getComputedStyle(document.getElementById('mobileMenu')).visibility") != "hidden":
            issues.append("mobile menu did not close on Escape")
        pg.click("#burger"); pg.wait_for_timeout(400)
        pg.click("#mobileMenu a[href='/about']")
        pg.wait_for_load_state("load")
        if not pg.url.rstrip("/").endswith("/about"):
            issues.append(f"mobile menu link went to {pg.url}")
        if pg.evaluate("!!document.getElementById('loader')"):
            issues.append("loader showed again on second page of the visit")
        # nav never covers an anchor target
        ctx.close()
        for url in sorted(links):
            r = b.new_context().request.get(url.split("#")[0])
            if r.status != 200:
                issues.append(f"internal link {url} -> {r.status}")
        notes.append(f"checked {len(links)} internal links")
        b.close()
    OUT.mkdir(exist_ok=True)
    report = "ISSUES (%d)\n" % len(issues) + "\n".join(issues) + "\n\nNOTES\n" + "\n".join(n for n in notes if n)
    (OUT / "report.txt").write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
