"""Contact sheet: python -I _source/sheet.py <width> <height> <screens> /path ..."""
import sys, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
w, h, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
paths = sys.argv[4:]
out = pathlib.Path(__file__).resolve().parent / "peek"; out.mkdir(exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    for path in paths:
        pg = b.new_page(viewport={"width": w, "height": h})
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e))); pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.goto("http://localhost:3000" + path, wait_until="load")
        pg.wait_for_function("() => !document.getElementById('loader')", timeout=10000)
        total = pg.evaluate("document.documentElement.scrollHeight")
        shots = []
        for i in range(n):
            y = i * h
            if y >= total: break
            pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(1500)
            f = out / f"_tmp{i}.png"; pg.screenshot(path=str(f)); shots.append(Image.open(f))
        sheet = Image.new("RGB", (w * len(shots) + 10 * (len(shots) - 1), h), "red")
        for i, im in enumerate(shots): sheet.paste(im, (i * (w + 10), 0))
        scale = min(1, 1900 / sheet.width)
        sheet = sheet.resize((int(sheet.width * scale), int(sheet.height * scale)))
        name = out / f"sheet_{(path.strip('/') or 'home')}_{w}.png"; sheet.save(name)
        print(name, "height", total, round(total / h, 1), "screens", "errors", errs)
        pg.close()
    b.close()
