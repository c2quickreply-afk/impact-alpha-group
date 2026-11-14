"""Copy check: every line of visible text on the redesigned pages (outside the
illustrative visuals) must appear word for word in the original site.
    python -I _source/copycheck.py
Prints any line that isn't in the original; exits 1 if there are any."""
import html, pathlib, re, sys
from html.parser import HTMLParser

HERE = pathlib.Path(__file__).resolve().parent
SITE = HERE.parent
ORIGINAL = SITE.parent / "earnings.html"
PAGES = ["index.html", "about.html", "community.html", "contact.html", "404.html"]
# illustrative visuals (allowed to have their own labels) and hidden helpers
SKIP_CLASSES = {"call", "vis", "call-card", "review", "partner", "loader", "skip", "topic-panel", "sr-only"}
BREAK = {"p", "h1", "h2", "h3", "h4", "li", "a", "button", "label", "small", "b", "span", "div", "figcaption", "br", "option"}
VOID = {"br", "img", "input", "meta", "link", "hr", "source", "path", "circle", "rect", "line", "stop"}


class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.stack = []; self.out = []; self.buf = ""
    def flush(self):
        if self.buf.strip(): self.out.append(self.buf)
        self.buf = ""
    def skipping(self):
        return any(s for _, s in self.stack)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        skip = tag in ("script", "style", "svg", "head", "title") or bool(SKIP_CLASSES & set((a.get("class") or "").split())) or "hidden" in a
        if tag in BREAK: self.flush()
        if tag not in VOID: self.stack.append((tag, skip))
    def handle_endtag(self, tag):
        if tag in VOID: return
        while self.stack:
            t, _ = self.stack.pop()
            if t == tag: break
        if tag in BREAK: self.flush()
    def handle_data(self, d):
        if not self.skipping(): self.buf += d


def norm(s):
    s = html.unescape(s).replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[→↓✓]", " ", s)          # arrows / tick are decoration
    return re.sub(r"\s+", " ", s).strip()


def visible_html(src):
    p = Text(); p.feed(src); p.flush()
    return [norm(x) for x in p.out if norm(x)]


def visible(path):
    p = Text(); p.feed(path.read_text(encoding="utf-8")); p.flush()
    return [norm(x) for x in p.out if norm(x)]


# New lines the user asked for (2026-11-06): market that the Community Call is free and open to all.
APPROVED = ["The Community Call", "Free to join.", "Open to everyone.", "Live session · Free to join",
            "Page not found."]  # the 404 page (the original site had none)
orig_lines = visible(ORIGINAL)
# the original form's wording lives in placeholder attributes
orig_lines += [norm(v) for v in re.findall(r'placeholder="([^"]+)"', ORIGINAL.read_text(encoding="utf-8"))]
orig = " ".join(orig_lines)
orig_nospace = orig.replace(" ", "")
bad = 0
for page in PAGES:
    missing = []
    for line in visible(SITE / page):
        if line in APPROVED:
            continue
        if line.isdigit():                      # animated counters (25+, 100s)
            continue
        if line in orig or line.replace(" ", "") in orig_nospace:
            continue
        missing.append(line)
    print(f"{page}: {'OK' if not missing else str(len(missing)) + ' line(s) not in the original'}")
    for m in dict.fromkeys(missing):
        print("   -", m)
    bad += len(missing)
# Helen's note (class="partner") is copied from the live Alpha site, so it's
# checked word for word against ../alpha.html instead.
alpha = " ".join(visible(SITE.parent / "alpha.html")).replace(" ", "")
src = (SITE / "about.html").read_text(encoding="utf-8")
i = src.find('class="partner"')
if i >= 0:
    j = src.find("</p>", i)
    for line in visible_html(src[src.find(">", i) + 1:j]):
        if line.replace(" ", "") not in alpha:
            print("about.html (Helen): not on the live Alpha site:", line); bad += 1
sys.exit(1 if bad else 0)
