"""Quick look: python -I _source/peek.py /path width height [scrollY ...]"""
import sys, pathlib
from playwright.sync_api import sync_playwright
path, w, h = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
ys = [int(v) for v in sys.argv[4:]] or [0]
out = pathlib.Path(__file__).resolve().parent / "peek"; out.mkdir(exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": w, "height": h})
    errs = []; pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None); pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto("http://localhost:3000" + path, wait_until="load")
    pg.wait_for_function("() => !document.getElementById('loader')", timeout=10000)
    for y in ys:
        pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(2600 if y == ys[0] else 1500)
        name = f"{path.strip('/') or 'home'}_{w}_{y}.png"; pg.screenshot(path=str(out / name)); print(out / name)
    print("height", pg.evaluate("document.documentElement.scrollHeight"), "errors", errs)
    b.close()
