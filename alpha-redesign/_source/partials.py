"""Shared partials (head, loader, nav, CTA, footer, privacy) for the static pages.

The site itself is plain HTML. This file is a dev-time convenience so the pages
share one nav/footer: run  python -I _source/build_pages.py  to rewrite the
.html files. This file is identical in the Impact Earnings and Impact Alpha
Group redesigns; brand content lives in site_config.py.
"""
from site_config import SITE, LINE, IMPORTANT, NAV_ITEMS, FOOTER_LINKS, CTA, STORAGE_NOTE, LAUNCH

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200'%3E%3Crect width='200' height='200' rx='44' fill='%23050a07'/%3E%3Cg stroke='%23d9b671' stroke-width='6' fill='none' stroke-linejoin='round'%3E%3Cpath d='M106 94 A62 62 0 0 1 174 26 A62 62 0 0 1 106 94Z'/%3E%3Cpath d='M106 94 A62 62 0 0 1 174 26 A62 62 0 0 1 106 94Z' transform='rotate(90 100 100)'/%3E%3Cpath d='M106 94 A62 62 0 0 1 174 26 A62 62 0 0 1 106 94Z' transform='rotate(180 100 100)'/%3E%3Cpath d='M106 94 A62 62 0 0 1 174 26 A62 62 0 0 1 106 94Z' transform='rotate(270 100 100)'/%3E%3Cpath d='M110.3 9.1 124.9 23.7 124.9 44.3 110.3 58.9 89.7 58.9 75.1 44.3 75.1 23.7 89.7 9.1Z'/%3E%3Cpath d='M110.3 9.1 124.9 23.7 124.9 44.3 110.3 58.9 89.7 58.9 75.1 44.3 75.1 23.7 89.7 9.1Z' transform='rotate(90 100 100)'/%3E%3Cpath d='M110.3 9.1 124.9 23.7 124.9 44.3 110.3 58.9 89.7 58.9 75.1 44.3 75.1 23.7 89.7 9.1Z' transform='rotate(180 100 100)'/%3E%3Cpath d='M110.3 9.1 124.9 23.7 124.9 44.3 110.3 58.9 89.7 58.9 75.1 44.3 75.1 23.7 89.7 9.1Z' transform='rotate(270 100 100)'/%3E%3Cpath d='M102 98 A30 30 0 0 1 134 66 A30 30 0 0 1 102 98Z'/%3E%3Cpath d='M102 98 A30 30 0 0 1 134 66 A30 30 0 0 1 102 98Z' transform='rotate(90 100 100)'/%3E%3Cpath d='M102 98 A30 30 0 0 1 134 66 A30 30 0 0 1 102 98Z' transform='rotate(180 100 100)'/%3E%3Cpath d='M102 98 A30 30 0 0 1 134 66 A30 30 0 0 1 102 98Z' transform='rotate(270 100 100)'/%3E%3C/g%3E%3Cpath d='M100 88 112 100 100 112 88 100Z' fill='%23d9b671'/%3E%3C/svg%3E")

# The original nav emblem, verbatim (gold stroke, width 6).
MARK = """<svg viewBox="0 0 200 200" fill="none" stroke="#d9b671" stroke-width="6" stroke-linejoin="round" aria-hidden="true">
      <path d="M100 88 112 100 100 112 88 100Z"/>
      <path d="M102 98 A30 30 0 0 1 134 66 A30 30 0 0 1 102 98Z"/>
      <path d="M102 98 A30 30 0 0 1 134 66 A30 30 0 0 1 102 98Z" transform="rotate(90 100 100)"/>
      <path d="M102 98 A30 30 0 0 1 134 66 A30 30 0 0 1 102 98Z" transform="rotate(180 100 100)"/>
      <path d="M102 98 A30 30 0 0 1 134 66 A30 30 0 0 1 102 98Z" transform="rotate(270 100 100)"/>
      <path d="M110.3 9.1 124.9 23.7 124.9 44.3 110.3 58.9 89.7 58.9 75.1 44.3 75.1 23.7 89.7 9.1Z"/>
      <path d="M110.3 9.1 124.9 23.7 124.9 44.3 110.3 58.9 89.7 58.9 75.1 44.3 75.1 23.7 89.7 9.1Z" transform="rotate(90 100 100)"/>
      <path d="M110.3 9.1 124.9 23.7 124.9 44.3 110.3 58.9 89.7 58.9 75.1 44.3 75.1 23.7 89.7 9.1Z" transform="rotate(180 100 100)"/>
      <path d="M110.3 9.1 124.9 23.7 124.9 44.3 110.3 58.9 89.7 58.9 75.1 44.3 75.1 23.7 89.7 9.1Z" transform="rotate(270 100 100)"/>
      <path d="M106 94 A62 62 0 0 1 174 26 A62 62 0 0 1 106 94Z"/>
      <path d="M106 94 A62 62 0 0 1 174 26 A62 62 0 0 1 106 94Z" transform="rotate(90 100 100)"/>
      <path d="M106 94 A62 62 0 0 1 174 26 A62 62 0 0 1 106 94Z" transform="rotate(180 100 100)"/>
      <path d="M106 94 A62 62 0 0 1 174 26 A62 62 0 0 1 106 94Z" transform="rotate(270 100 100)"/>
    </svg>"""

# The original loader markup, verbatim.
LOADER = """<div class="loader" id="loader" aria-hidden="true">
  <svg class="loader-mark" viewBox="0 0 200 200" fill="none">
    <path class="ec" d="M100 88 112 100 100 112 88 100Z"/>
    <path class="ei" d="M102 98 A30 30 0 0 1 134 66 A30 30 0 0 1 102 98Z"/>
    <path class="ei" d="M102 98 A30 30 0 0 1 134 66 A30 30 0 0 1 102 98Z" transform="rotate(90 100 100)"/>
    <path class="ei" d="M102 98 A30 30 0 0 1 134 66 A30 30 0 0 1 102 98Z" transform="rotate(180 100 100)"/>
    <path class="ei" d="M102 98 A30 30 0 0 1 134 66 A30 30 0 0 1 102 98Z" transform="rotate(270 100 100)"/>
    <path class="eo" d="M110.3 9.1 124.9 23.7 124.9 44.3 110.3 58.9 89.7 58.9 75.1 44.3 75.1 23.7 89.7 9.1Z"/>
    <path class="eo" d="M110.3 9.1 124.9 23.7 124.9 44.3 110.3 58.9 89.7 58.9 75.1 44.3 75.1 23.7 89.7 9.1Z" transform="rotate(90 100 100)"/>
    <path class="eo" d="M110.3 9.1 124.9 23.7 124.9 44.3 110.3 58.9 89.7 58.9 75.1 44.3 75.1 23.7 89.7 9.1Z" transform="rotate(180 100 100)"/>
    <path class="eo" d="M110.3 9.1 124.9 23.7 124.9 44.3 110.3 58.9 89.7 58.9 75.1 44.3 75.1 23.7 89.7 9.1Z" transform="rotate(270 100 100)"/>
    <path class="ep" d="M106 94 A62 62 0 0 1 174 26 A62 62 0 0 1 106 94Z"/>
    <path class="ep" d="M106 94 A62 62 0 0 1 174 26 A62 62 0 0 1 106 94Z" transform="rotate(90 100 100)"/>
    <path class="ep" d="M106 94 A62 62 0 0 1 174 26 A62 62 0 0 1 106 94Z" transform="rotate(180 100 100)"/>
    <path class="ep" d="M106 94 A62 62 0 0 1 174 26 A62 62 0 0 1 106 94Z" transform="rotate(270 100 100)"/>
  </svg>
  <div class="loader-word"><span>%s</span></div>
  <div class="loader-bar"><i></i></div>
</div>""" % SITE["loader_word"]

ARR = '<span class="arr" aria-hidden="true">&rarr;</span>'
EXT = 'target="_blank" rel="noopener"'


def fine(extra=""):
    """The short disclaimer line, styled small, for next to buttons."""
    return f'<p class="fineprint"{extra}>{LINE}</p>'


def head(title, desc, active, og=False):
    robots = "" if LAUNCH else '<meta name="robots" content="noindex, nofollow">\n'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{robots}<title>{title}</title>
<meta name="description" content="{desc}">
{og_tags(title, desc) if og else ""}<meta name="theme-color" content="#ffffff">
<meta name="referrer" content="strict-origin-when-cross-origin">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="/fonts/fonts.css">
<link rel="stylesheet" href="/assets/site.css">
<script src="/assets/gate.js"></script>
<script src="/assets/site.js" defer></script>
</head>
<body data-page="{active}">
<a class="skip" href="#main">Skip to content</a>
{LOADER}
{nav(active)}
<main id="main">
"""


def og_tags(title, desc):
    return (f'<meta property="og:title" content="{title}">\n'
            f'<meta property="og:description" content="{desc}">\n'
            '<meta property="og:type" content="website">\n')


def nav(active):
    def cur(key):
        return ' aria-current="page"' if key == active else ""
    links = "\n      ".join(
        f'<a class="nav-link" href="{href}"{cur(k)}>{label}</a>' for k, href, label in NAV_ITEMS)
    mlinks = "\n  ".join(
        f'<a class="m-link" href="{href}"{cur(k)}>{label} {ARR}</a>' for k, href, label in NAV_ITEMS)
    return f"""<header class="nav" id="nav">
  <div class="container nav-inner">
    <a class="logo" href="/" aria-label="{SITE['name']} home"{' aria-current="page"' if active == 'home' else ''}>
      <span class="logo-tile">{MARK}</span>
      <span class="logo-word">{SITE['logo_word']}</span>
    </a>
    <nav class="nav-links" aria-label="Main">
      {links}
    </nav>
    <div class="nav-cta">
      <a class="btn btn-primary btn-sm" href="{SITE['book']}" {EXT}>{SITE['book_label']} {ARR}</a>
      <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mobileMenu"><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-menu" id="mobileMenu" aria-label="Menu">
  {mlinks}
  <a class="btn btn-primary" href="{SITE['book']}" {EXT}>{SITE['book_label']} {ARR}</a>
  <p class="m-note">{LINE}</p>
</div>"""


def steps(extra="", items=None):
    """The original three-step list, word for word."""
    lis = "\n".join(f'          <li><span class="n">{i + 1:02d}</span><p>{t}</p></li>' for i, t in enumerate(items or CTA["steps"]))
    return f"""<ol class="steps" data-stagger{extra}>
{lis}
        </ol>"""


def cta(bg="bg-sage"):
    p_label, p_href = CTA["primary"]
    sec = ""
    if CTA.get("secondary"):
        s_label, s_href = CTA["secondary"]
        ext = EXT if s_href.startswith("http") else ""
        sec = f'\n            <a class="btn btn-ghost-dark" href="{s_href}" {ext}>{s_label}</a>'
    fine_html = f'\n          <p class="fine">{CTA["fine"]}</p>' if CTA.get("fine") else ""
    return f"""
<section class="section {bg}" id="start">
  <div class="container">
    <div class="cta-panel" data-reveal="scale">
      <div class="cta-grid">
        <div data-stagger>
          <span class="eyebrow">{CTA['eyebrow']}</span>
          <h2 class="h2">{CTA['heading']}</h2>
          <div class="btn-row">
            <a class="btn btn-gold" href="{p_href}" {EXT}>{p_label} {ARR}</a>{sec}
          </div>{fine_html}
          <p class="fine">{LINE}</p>
        </div>
        {steps()}
      </div>
    </div>
  </div>
</section>
"""


def footer():
    links = "\n        ".join(
        f'<li><a href="{h}"{" " + EXT if ext else ""}>{l}</a></li>' for l, h, ext in FOOTER_LINKS)
    return f"""</main>
<footer class="footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <a class="logo" href="/" aria-label="{SITE['name']} home"><span class="logo-tile">{MARK}</span><span class="logo-word">{SITE['logo_word']}</span></a>
        <p class="footer-tag">{SITE['tagline']}</p>
      </div>
      <ul class="footer-links">
        {links}
        <li><button type="button" class="motion-toggle" aria-pressed="false">Pause animations</button></li>
      </ul>
    </div>
    <div class="footer-legal">
      <p>{IMPORTANT}</p>
      <p class="copy">{SITE['copyright']}<br>{LINE}</p>
    </div>
  </div>
</footer>
</body>
</html>
"""


def privacy_body():
    """Draft privacy policy (same policy as the live site's /privacy), plus this
    site's one browser-storage setting. DRAFT until Francene approves."""
    return f"""
<section class="section bg-white">
  <div class="container">
    <div class="prose privacy">
      <p class="draft"><b>Draft for review.</b> This policy is waiting for approval from Francene Loomiller. Items in [brackets] still need to be confirmed.</p>
      <p class="updated">Last updated: November 13, 2026</p>

      <h2>Who we are</h2>
      <p>This website, and its sister site, is run by <b>[legal business name, to be confirmed]</b>, doing business as Impact Earnings and Impact Alpha Group, led by Francene Loomiller, based in <b>[city, state, to be confirmed]</b>. In this policy, &ldquo;we&rdquo; and &ldquo;us&rdquo; mean that business. It covers impactearnings.com and impactalphagroup.com.</p>
      <p>Questions about this policy or your information: <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>

      <h2>What we collect, and why</h2>
      <ul>
        <li><b>Contact form.</b> Your name, email address and message. We use them only to read and reply to your message.</li>
        <li><b>Newsletter signup.</b> When you join The Impact Earnings Dispatch, the signup page asks for your name, email address and phone number, and offers an optional box to receive text messages. We use this to send the newsletter, and to text you only if you checked that box.</li>
        <li><b>Community Call registration.</b> To register for the call, you give your name, email address and, on some registration pages, your phone number. We use this to send you the call details and reminders.</li>
        <li><b>Booking a call with Francene.</b> The booking calendar collects the time you choose, your time zone, and the contact details you enter, so we can hold the conversation.</li>
        <li><b>Basic technical information.</b> Like nearly every website, our hosting provider automatically records information such as your IP address, browser type and the pages requested, to keep the site running and secure.</li>
      </ul>
      <p>These websites do not use cookies, analytics, or advertising trackers. {STORAGE_NOTE} The fonts are served from our own site, so loading a page doesn&rsquo;t send your information to a font provider.</p>

      <h2>Who we share it with</h2>
      <p>We use a small number of service providers to run the site and these services. They handle your information on our behalf:</p>
      <ul>
        <li><b>Vercel</b>, which hosts this website. <a href="https://vercel.com/legal/privacy-policy" {EXT}>Vercel&rsquo;s privacy policy</a>.</li>
        <li><b>FormSubmit</b>, which delivers contact-form messages to our email. <a href="https://formsubmit.co/privacy.pdf" {EXT}>FormSubmit&rsquo;s privacy policy</a>.</li>
        <li><b>Google Workspace</b>, our email provider, where messages and replies are stored. <a href="https://policies.google.com/privacy" {EXT}>Google&rsquo;s privacy policy</a>.</li>
        <li><b>HighLevel (LeadConnector)</b>, which runs our signup, registration and booking pages at go.impactearnings.com and stores what you enter there. Those pages may also set cookies of their own, including a security cookie from Cloudflare. <a href="https://www.gohighlevel.com/privacy-policy" {EXT}>HighLevel&rsquo;s privacy policy</a>.</li>
        <li><b>Zoom</b>, which hosts the Community Call and its registration page. <a href="https://explore.zoom.us/en/privacy/" {EXT}>Zoom&rsquo;s privacy policy</a>.</li>
      </ul>
      <p>Links to LinkedIn and other sites take you to services with their own privacy policies.</p>
      <p><b>We do not sell or rent your personal information</b>, and we don&rsquo;t share it with anyone else except where the law requires it.</p>

      <h2>Your choices</h2>
      <ul>
        <li>Every newsletter email includes an unsubscribe link. If you agreed to text messages, reply STOP to any text to stop them.</li>
        <li>To ask for a copy of the information we hold about you, or to have it corrected or deleted, email <a href="mailto:{SITE['email']}">{SITE['email']}</a>. We&rsquo;ll answer within 30 days.</li>
      </ul>

      <h2>Children</h2>
      <p>Our websites and services are not directed at children under 13, and we don&rsquo;t knowingly collect information from them. If you believe a child has sent us information, email us and we&rsquo;ll delete it.</p>

      <h2>Changes to this policy</h2>
      <p>If we change this policy, we&rsquo;ll update it on this page and change the &ldquo;Last updated&rdquo; date above.</p>
    </div>
  </div>
</section>
"""
