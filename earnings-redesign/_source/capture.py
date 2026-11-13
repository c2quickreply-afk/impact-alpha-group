"""Capture the ORIGINAL Impact Earnings page (earnings.html in the repo root):
full-page screenshots at 1440 and 390, plus loader frames every ~150ms.
Run:  python -I _source/capture.py   (from earnings-redesign/)
"""
import pathlib, time
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
ORIG = (HERE.parent.parent / "earnings.html").as_uri()
OUT = HERE / "original"
FRAMES = HERE / "loader" / "frames"
import sys
PREFIX = "orig"
if len(sys.argv) > 1:  # python capture.py <url> <prefix>  -> loader frames only
    ORIG, PREFIX = sys.argv[1], sys.argv[2]

with sync_playwright() as p:
    b = p.chromium.launch()
    # loader frames
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    import base64
    cdp = pg.context.new_cdp_session(pg)
    pg.goto(ORIG, wait_until="commit")
    t0 = time.time()
    i = 0
    while time.time() - t0 < 4.5:
        ms = int((time.time() - t0) * 1000)
        data = cdp.send("Page.captureScreenshot", {"format": "jpeg", "quality": 70})["data"]
        (FRAMES / f"{PREFIX}_{i:02d}_{ms:05d}ms.jpg").write_bytes(base64.b64decode(data))
        i += 1
        time.sleep(0.12)
    pg.close()
    if PREFIX != "orig":
        b.close(); raise SystemExit

    for w, h in ((1440, 900), (390, 844)):
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.goto(ORIG, wait_until="load")
        pg.wait_for_timeout(3800)
        total = pg.evaluate("document.documentElement.scrollHeight")
        y = 0
        while y < total:
            pg.evaluate(f"window.scrollTo(0,{y})")
            pg.wait_for_timeout(250)
            y += h
        pg.evaluate("window.scrollTo(0,0)")
        pg.wait_for_timeout(600)
        pg.screenshot(path=str(OUT / f"home_{w}.png"), full_page=True)
        pg.close()
    b.close()
print("done")
