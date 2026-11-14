"""Writes the static pages from partials.py + the page bodies below.
Run from earnings-redesign/:  python -I _source/build_pages.py

COPY RULE: every sentence outside the illustrative visuals (the call window,
custody flow, discernment checklist, security ring, mail card) is copied
word for word from the live site's compliance-reviewed copy (repo root
earnings.html). Don't paraphrase it or add claims. Every booking, call,
newsletter and contact button gets the disclaimer line (fine()) next to it.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from partials import head, footer, cta, steps, fine, privacy_body, SITE, ARR, EXT  # noqa: E402
from site_config import LINE, LAUNCH, PRIVACY_APPROVED  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

_S = 'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="square" stroke-linejoin="miter" aria-hidden="true"'
ICON = {
    "shield": f'<svg {_S}><path d="M12 3l8 4v5c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
    "check": f'<svg {_S}><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
    "plus": '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M6 1v10M1 6h10"/></svg>',
    "video": f'<svg {_S}><path d="M3 6h13v12H3z"/><path d="M16 10.5l5-3v9l-5-3"/></svg>',
    "mic": f'<svg {_S}><path d="M9 3h6v11H9z"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>',
    "mic_off": f'<svg {_S}><path d="M9 3h6v11H9z"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/><path d="M3 3l18 18"/></svg>',
    "people": f'<svg {_S}><path d="M9 11a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7zM2.5 20c.6-3.4 3.2-5.5 6.5-5.5s5.9 2.1 6.5 5.5"/><path d="M16 4.3a3.5 3.5 0 0 1 0 6.4M18 14.8c1.9.7 3.2 2.5 3.5 5.2"/></svg>',
    "chat": f'<svg {_S}><path d="M3 4h18v13H8l-5 4z"/></svg>',
    "share": f'<svg {_S}><path d="M3 4h18v13H3z"/><path d="M12 14V8M9 10.5L12 7.5l3 3M8 21h8"/></svg>',
    "smile": f'<svg {_S}><circle cx="12" cy="12" r="9"/><path d="M8.5 14.5c1.8 2 5.2 2 7 0M9 9.5v.01M15 9.5v.01"/></svg>',
    "person": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="12" cy="9" r="4"/><path d="M4 21c.8-4.4 4-7 8-7s7.2 2.6 8 7z"/></svg>',
    "lock": f'<svg {_S}><path d="M5 11h14v10H5z"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
    "bars": f'<svg {_S}><path d="M4 20V12M10 20V6M16 20v-9M22 20H2"/></svg>',
    "chip": f'<svg {_S}><path d="M7 7h10v10H7z"/><path d="M10 10h4v4h-4zM10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/></svg>',
    "sliders": f'<svg {_S}><path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12"/><path d="M14 4v4M8 10v4M16 16v4"/></svg>',
    "bolt": f'<svg {_S}><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></svg>',
    "news": f'<svg {_S}><path d="M4 4h13v16H6a2 2 0 0 1-2-2z"/><path d="M17 8h3v10a2 2 0 0 1-2 2M8 8h5M8 12h5M8 16h3"/></svg>',
    "bulb": f'<svg {_S}><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9V16h7v-2.1A6 6 0 0 0 12 3z"/></svg>',
    "refresh": f'<svg {_S}><path d="M20 11a8 8 0 0 0-14.6-4.5M4 13a8 8 0 0 0 14.6 4.5"/><path d="M5 3v4h4M19 21v-4h-4"/></svg>',
    "gear": f'<svg {_S}><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/></svg>',
    "spark": f'<svg {_S}><path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/></svg>',
    "alert": f'<svg {_S}><path d="M12 3l9.5 17h-19z"/><path d="M12 10v4M12 17.5v.01"/></svg>',
    "mail": f'<svg {_S}><path d="M3 5h18v14H3z"/><path d="M3.5 6.5L12 13l8.5-6.5"/></svg>',
    "link": f'<svg {_S}><path d="M3 3h18v18H3z"/><path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/></svg>',
}

TOPICS = [
    ("Digital Assets &amp; Market Trends", "Understand cryptocurrencies, blockchain networks and the forces shaping adoption."),
    ("Automation &amp; Emerging Technology", "Explore how AI, automated systems and new financial tools are changing participation in markets."),
    ("Security &amp; Self-Custody", "Learn practical habits for protecting wallets, accounts, devices and digital assets."),
    ("Opportunities &mdash; with Discernment", "Learn frameworks for evaluating emerging platforms, strategies and projects through an experienced, risk-aware lens."),
    ("Capital With Purpose", "Discover how technology and investment can support meaningful real-world outcomes."),
]


def topics_list():
    rows = []
    for i, (t, d) in enumerate(TOPICS):
        rows.append(f"""      <div class="topic">
        <button class="topic-btn" type="button" aria-expanded="false" aria-controls="tp{i}">
          <span class="topic-title"><span class="topic-n">{i + 1:02d}</span>{t}</span>
          <span class="topic-desc">{d}</span>
          <span class="topic-ic">{ICON['plus']}</span>
        </button>
        <div class="topic-panel" id="tp{i}"><p>{d}</p></div>
      </div>""")
    return '<div class="topics" data-stagger>\n' + "\n".join(rows) + "\n    </div>"


def principles():
    return """<div class="principles" data-stagger>
          <div class="principle"><b>Education</b><span>before opportunity</span></div>
          <div class="principle"><b>Understanding</b><span>before action</span></div>
          <div class="principle"><b>Discernment</b><span>before hype</span></div>
        </div>"""


PORTRAIT_CAP = "<figcaption><b>Francene Loomiller</b><small>Founder &middot; Financial Markets &amp; Digital Assets</small></figcaption>"

# ----------------------------------------------------------------------------
# Visuals (illustrative; the only places with wording that isn't the original's)
# ----------------------------------------------------------------------------
CALL = f"""<div class="hero-visual" id="heroVisual">
        <div class="call" data-hero style="--d:250" role="img" aria-label="Illustration of an Impact Earnings Community Call on Zoom, with Francene Loomiller presenting a teaching slide on how to make sense of something new in emerging technology">
          <div class="call-bar" aria-hidden="true">
            <span class="call-title">{ICON['lock']}Impact Earnings Community Call</span>
            <span class="call-time" id="callTime">00:00</span>
          </div>
          <div class="call-stage" aria-hidden="true">
            <div class="share">
              <span class="share-tag"><i></i>Viewing Francene Loomiller&rsquo;s screen</span>
              <div class="slide">
                <div class="slide-top">
                  <div>
                    <span class="slide-eyebrow">Emerging technology</span>
                    <p class="slide-title">How we make sense of something new</p>
                  </div>
                  <span class="tag-illus">Illustrative</span>
                </div>
                <div class="pipe" id="pipe">
                  <div class="pipe-track"><i class="pipe-fill"></i><i class="pipe-packet"></i></div>
                  <div class="pn on"><span class="pn-ic">{ICON['news']}</span><b>What&rsquo;s new</b><small>Tools, features &amp; headlines</small></div>
                  <div class="pn"><span class="pn-ic">{ICON['bulb']}</span><b>How it works</b><small>The mechanics, plainly</small></div>
                  <div class="pn"><span class="pn-ic">{ICON['sliders']}</span><b>How to use it</b><small>Whether it fits you</small></div>
                  <div class="pn"><span class="pn-ic">{ICON['refresh']}</span><b>How to keep up</b><small>As it keeps changing</small></div>
                </div>
                <div class="pipe-detail" id="pipeDetail"><span class="pd-n">01</span><p>A new tool, feature or development makes the news. We start with the facts: what changed, and why people are talking about it.</p></div>
                <p class="slide-note">Illustrative: how we work through new developments together.</p>
              </div>
            </div>
            <div class="tiles">
              <figure class="tile host">
                <img src="/images/francene.jpg" alt="" width="854" height="1280">
                <span class="talk"><i></i><i></i><i></i></span>
                <figcaption>{ICON['mic']}Francene<span class="ln">&nbsp;Loomiller</span></figcaption>
              </figure>
              <div class="tile"><span class="av">{ICON['person']}</span><span class="muted-ic">{ICON['mic_off']}</span></div>
              <div class="tile"><span class="av">{ICON['person']}</span><span class="muted-ic">{ICON['mic_off']}</span></div>
            </div>
          </div>
          <div class="call-controls" aria-hidden="true">
            <div class="ctl-group">
              <span class="ctl">{ICON['mic_off']}<small>Unmute</small></span>
              <span class="ctl">{ICON['video']}<small>Video</small></span>
            </div>
            <div class="ctl-group">
              <span class="ctl">{ICON['people']}<small>Participants</small></span>
              <span class="ctl">{ICON['chat']}<small>Chat</small></span>
              <span class="ctl">{ICON['share']}<small>Share</small></span>
              <span class="ctl ctl-x">{ICON['smile']}<small>Reactions</small></span>
            </div>
            <span class="ctl-leave">Leave</span>
          </div>
        </div>
      </div>"""

VIS_FLOW = """<div class="vis" data-reveal="right">
          <div class="vis-card">
            <div class="vis-head"><span class="vis-title">From hype to understanding</span><span class="vis-sub">A core idea</span></div>
            <div class="flow">
              <div class="flow-node"><span class="k">What you hear</span><p class="v">Headlines &amp; hype</p><p class="d">Fast, loud, and often incomplete.</p></div>
              <div class="flow-mid" aria-hidden="true"><svg viewBox="0 0 46 24"><path d="M2 12h40M36 6l6 6-6 6"/></svg></div>
              <div class="flow-node you"><span class="k">What you understand</span><p class="v">The full picture</p><p class="d">How it works, what it asks of you, and what can go wrong.</p></div>
            </div>
            <div class="keys">
              <div class="key"><b>The basics</b><span>How the technology actually works</span></div>
              <div class="key"><b>The context</b><span>Why it matters, and why now</span></div>
              <div class="key"><b>The trade-offs</b><span>What it costs in time, money and risk</span></div>
            </div>
          </div>
        </div>"""

VIS_EVAL = f"""<div class="vis mist" data-reveal="left">
          <div class="vis-card" data-anim="eval">
            <div class="vis-head"><span class="vis-title">What we work through on the call</span><span class="vis-sub">Together, live</span></div>
            <div class="eval-row"><span class="eval-ic">{ICON['gear']}</span><p class="eval-q">How does it work?<small>The mechanism, in plain language</small></p><span class="eval-state">Up next</span></div>
            <div class="eval-row"><span class="eval-ic">{ICON['spark']}</span><p class="eval-q">Where might value come from?<small>And whether that&rsquo;s realistic</small></p><span class="eval-state">Up next</span></div>
            <div class="eval-row"><span class="eval-ic">{ICON['alert']}</span><p class="eval-q">What risks deserve attention?<small>Platform, market and security risk</small></p><span class="eval-state">Up next</span></div>
            <div class="eval-foot"><i></i>Then decide what feels right for you.</div>
          </div>
        </div>"""

CHECKS = ["Wallets", "Passwords", "Devices", "Self-custody", "Platform security", "Scam avoidance"]
VIS_SEC = """<div class="vis cream" data-reveal="right">
          <div class="vis-card" data-anim="checks">
            <div class="sec-top">
              <div class="ring"><svg viewBox="0 0 64 64"><circle class="bg" cx="32" cy="32" r="26"/><circle class="fg" cx="32" cy="32" r="26"/></svg><b><span class="ring-n">0</span>/6</b></div>
              <div><p class="vis-title">Security habits</p><p class="vis-sub">An institutional risk mindset, applied to your own activity</p></div>
            </div>
            <ul class="checks">""" + "".join(
    f'<li><span class="box"><svg viewBox="0 0 12 12"><path d="M2.5 6.2l2.3 2.3L9.5 3.8"/></svg></span>{c}</li>' for c in CHECKS) + """</ul>
          </div>
        </div>"""


# ----------------------------------------------------------------------------
# Pages
# ----------------------------------------------------------------------------
HOME_DESC = ("Impact Earnings: plain-language education on digital assets, security, automation and emerging "
             "technology, led by Francene Loomiller. Education only, not financial advice.")


def home():
    return head("Impact Earnings &mdash; Where Opportunity Meets Understanding", HOME_DESC, "home", og=True) + f"""
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-copy">
        <span class="eyebrow" data-hero style="--d:0">Education &middot; Clarity &middot; Discernment</span>
        <h1 class="h1" data-hero style="--d:80">Make sense of the <span class="accent">new financial era.</span></h1>
        <p class="lead" data-hero style="--d:180">Clear, experience-led education on digital assets, markets, automation, security and emerging opportunities.</p>
        <div class="btn-row" data-hero style="--d:280">
          <a class="btn btn-primary" href="{SITE['book']}" {EXT}>Book a Call {ARR}</a>
          <a class="btn btn-secondary" href="{SITE['call']}" {EXT}>Join the Community Call</a>
        </div>
        <p class="hero-note" data-hero style="--d:380">{ICON['shield']}{LINE}</p>
      </div>
      {CALL}
    </div>
  </div>
  <div class="creds">
    <div class="container">
      <div class="creds-grid" data-stagger>
        <div class="cred"><p class="cred-num"><span data-count="25">25</span><span class="suf">+</span></p><p class="cred-label">Years in financial markets</p></div>
        <div class="cred"><p class="cred-num"><span data-count="100">100</span><span class="suf">s</span></p><p class="cred-label">Educational sessions hosted</p></div>
        <div class="cred"><p class="cred-num">Both worlds</p><p class="cred-label">Institutional finance, digital assets &amp; emerging opportunities</p></div>
        <div class="cred"><p class="cred-num">No hype</p><p class="cred-label">A community-first, education-led approach</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-sage">
  <div class="container thesis">
    <div data-reveal>
      <span class="eyebrow">Our thesis</span>
      <p class="thesis-lede">Opportunity is evolving. <span class="accent">Understanding comes first.</span></p>
    </div>
    <div>
      <p class="statement" id="statement" data-em="institutions. noise, complexity,">The financial landscape is changing quickly. Digital assets, artificial intelligence, automation, and new models of ownership are opening doors that were once largely reserved for institutions. But with greater access comes more noise, more complexity, and more to navigate.</p>
      <p class="lead" style="margin-top:20px" data-reveal>Impact Earnings exists to help individuals better understand what&rsquo;s changing, explore emerging opportunities with greater clarity, and make informed decisions that feel right for them &mdash; without hype, pressure, or unnecessary complexity.</p>
      <div class="thesis-tail" data-stagger>
        <span class="pill">{ICON['check']}Education first</span><span class="pill">{ICON['check']}No hype</span><span class="pill">{ICON['check']}No guarantees</span>
      </div>
    </div>
  </div>
</section>

<section class="section bg-white">
  <div class="container">
    <div class="section-head feature-cols">
      <div data-reveal>
        <span class="eyebrow">The Community Call</span>
        <h2 class="h2">Free to join. <span class="accent">Open to everyone.</span></h2>
      </div>
      <div class="section-aside" data-reveal style="--d:120">
        <p class="lead">Join us on Zoom for a relaxed, educational conversation around digital assets, automation, emerging opportunities, security, and what&rsquo;s happening in the market.</p>
        <p style="margin-top:16px"><a class="link-arrow" href="{SITE['call']}" {EXT}>Join the Community Call {ARR}</a></p>
        {fine()}
      </div>
    </div>
    <div class="features">
      <div class="feature">
        <div class="feature-copy" data-stagger>
          <span class="step-tag">01</span>
          <h3 class="h3">Start with understanding</h3>
          <p>Learn how digital assets, wallets, exchanges, custody and market cycles actually work before putting money at risk.</p>
          <p>Impact Earnings breaks down complex ideas into practical, understandable education so you can make more informed decisions.</p>
        </div>
        {VIS_FLOW}
      </div>
      <div class="feature flip">
        <div class="feature-copy" data-stagger>
          <span class="step-tag">02</span>
          <h3 class="h3">Explore emerging opportunities</h3>
          <p>Understand automated trading, decentralized finance, AI-driven tools and new financial technologies &mdash; including how they work, where potential value may come from and what risks deserve attention.</p>
          <p><b>Education first. No hype. No guarantees.</b></p>
        </div>
        {VIS_EVAL}
      </div>
      <div class="feature">
        <div class="feature-copy" data-stagger>
          <span class="step-tag">03</span>
          <h3 class="h3">Protect what you build</h3>
          <p>Develop stronger habits around wallets, passwords, devices, self-custody, platform security and scam avoidance.</p>
          <p>Apply an institutional risk mindset to your personal digital-asset activity.</p>
          <p style="margin-top:18px"><a class="link-arrow" href="{SITE['book']}" {EXT}>Join Impact Earnings &mdash; book a free conversation {ARR}</a></p>
          {fine()}
        </div>
        {VIS_SEC}
      </div>
    </div>
  </div>
</section>

<section class="section bg-cream" id="cover">
  <div class="container">
    <div class="section-head stack" data-reveal>
      <h2 class="h2">What we cover</h2>
    </div>
    {topics_list()}
  </div>
</section>

<section class="section bg-white">
  <div class="container founder">
    <figure class="portrait" data-reveal="left">
      <img src="/images/francene.jpg" alt="Francene Loomiller, founder of Impact Earnings" width="854" height="1280" loading="lazy">
      {PORTRAIT_CAP}
    </figure>
    <div>
      <div data-stagger>
        <span class="eyebrow">The founder</span>
        <h2 class="h2">Trust, cultivated over <span class="accent">25 years.</span></h2>
        <p class="lead" style="margin-top:16px">Francene Loomiller has spent more than 25 years working across financial markets, institutional finance, digital assets, education, and emerging opportunities.</p>
        <p class="measure hide-sm" style="margin-top:12px">She began her career in institutional equity trading and research sales, working directly with professional market participants and gaining an inside perspective on how capital, information, risk, and opportunity move through financial systems.</p>
      </div>
      {principles()}
      <div class="btn-row" style="margin-top:28px" data-reveal>
        <a class="btn btn-secondary" href="/about">Meet Francene {ARR}</a>
      </div>
    </div>
  </div>
</section>
""" + cta() + footer()


def page_head(eyebrow, title, body="", aside=""):
    grid = "page-head-grid wide" if aside else "page-head-grid"
    return f"""
<section class="page-head hero">
  <div class="container {grid}">
    <div>
      <span class="eyebrow" data-hero>{eyebrow}</span>
      <h1 class="h1" data-hero style="--d:80">{title}</h1>
      {body}
    </div>
    {aside}
  </div>
</section>
"""


def about():
    return head("About &mdash; Impact Earnings",
                "Francene Loomiller has spent more than 25 years working across financial markets, institutional finance, digital assets, education, and emerging opportunities.",
                "about") + page_head("The founder", 'Trust, cultivated over <span class="accent">25 years.</span>') + f"""
<section class="section bg-white" id="story">
  <div class="container split">
    <div class="sticky-col">
      <figure class="portrait" data-reveal="left">
        <img src="/images/francene.jpg" alt="Francene Loomiller" width="854" height="1280">
        {PORTRAIT_CAP}
      </figure>
      <!-- Helen's note, word for word from the live impactalphagroup.com -->
      <div class="partner" data-reveal>
        <span class="avatar" aria-hidden="true">H</span>
        <div>
          <b>Helen Korb</b>
          <span class="role">Financial Strategy &amp; Operational Excellence</span>
          <p>Helen brings 25+ years in financial analysis, institutional finance, and compliance &mdash; building the forecasting, reporting, and accountability frameworks that keep complex initiatives visible and on track. Her discipline is the counterweight to momentum: commitments are modeled before they are made, timelines are tested against reality, and every partner knows exactly where an initiative stands. Together they draw on a vetted network of lenders, grant strategists, engineers, and technical advisors, engaged as each initiative requires.</p>
        </div>
      </div>
    </div>
    <div>
      <div class="prose" data-stagger>
        <p class="intro">Francene Loomiller has spent more than 25 years working across financial markets, institutional finance, digital assets, education, and emerging opportunities.</p>
        <p>She began her career in institutional equity trading and research sales, working directly with professional market participants and gaining an inside perspective on how capital, information, risk, and opportunity move through financial systems.</p>
        <p>As financial technology evolved, Francene expanded her work into digital assets, blockchain, decentralized finance, automated trading, and investor education. Through Impact Earnings, she helps individuals understand complex ideas in plain language, strengthen their security practices, evaluate new opportunities more carefully, and participate with greater confidence and discernment.</p>
        <p>Her approach is grounded in a simple belief: <b>access alone is not enough.</b> People also need education, context, practical tools, and someone they can trust to ask the questions others may overlook.</p>
        <p>Francene is also the founder of Impact Alpha Group, where she works with leadership teams and strategic partners to advance mission-aligned initiatives in regenerative development, infrastructure, community resilience, environmental innovation, and emerging financial technologies.</p>
        <p>Across both platforms, her consistent strength is cultivating trust, connecting people and ideas, and helping promising opportunities move from conversation toward meaningful action.</p>
      </div>
      {principles()}
      <div class="btn-row" style="margin-top:28px" data-reveal>
        <a class="btn btn-primary" href="{SITE['book']}" {EXT}>Book a Call {ARR}</a>
        <span class="muted" style="font-size:var(--fs-small)">Prefer LinkedIn? <a class="link-arrow" href="{SITE['linkedin']}" {EXT}>Connect with Francene {ARR}</a></span>
      </div>
      {fine(' data-reveal')}
    </div>
  </div>
</section>

<section class="section bg-sage" id="alpha">
  <div class="container">
    <div class="panel split" data-reveal="scale" style="align-items:center">
      <div>
        <span class="eyebrow">Beyond Impact Earnings</span>
        <h2 class="h2">From financial innovation to <span class="accent">real-world impact.</span></h2>
      </div>
      <div>
        <p>Francene also leads Impact Alpha Group, a strategic development and partnership platform supporting complex, mission-aligned initiatives across regenerative development, infrastructure, environmental innovation, community resilience and emerging financial technologies.</p>
        <div class="btn-row" style="margin-top:22px"><a class="btn btn-primary" href="{SITE['sister']}" {EXT}>Explore Impact Alpha Group {ARR}</a></div>
      </div>
    </div>
  </div>
</section>
""" + cta(bg="bg-white") + footer()


def community():
    call_topics = ["Digital assets", "Automation", "Emerging opportunities", "Security", "What&rsquo;s happening in the market"]
    chips = "".join(f"<li>{t}</li>" for t in call_topics)
    body = f"""<p class="lead" data-hero style="--d:160">Join us on Zoom for a relaxed, educational conversation around digital assets, automation, emerging opportunities, security, and what&rsquo;s happening in the market. From time to time, we&rsquo;re also joined by special guests and industry experts who bring additional perspective, insight, and firsthand experience to the conversation.</p>
      <div class="btn-row" data-hero style="--d:240;margin-top:24px">
        <a class="btn btn-primary" href="{SITE['call']}" {EXT}>Join the Community Call {ARR}</a>
        <span class="muted" style="font-size:var(--fs-xs)">Opens call registration</span>
      </div>
      {fine(' data-hero style="--d:280"')}"""
    aside = f"""<div class="vis-card call-card" data-hero style="--d:300" aria-hidden="true">
      <div class="vis-head"><span class="vis-title">Community Call</span><span class="vis-sub zoom">{ICON['video']}Zoom</span></div>
      <ul class="chip-list">{chips}</ul>
      <div class="guest-row">{ICON['people']}<span>Special guests &amp; industry experts</span></div>
    </div>"""
    return head("Community Call &amp; Newsletter &mdash; Impact Earnings",
                "Join us on Zoom for a relaxed, educational conversation around digital assets, automation, emerging opportunities, security, and what's happening in the market.",
                "community") + f'<div id="call"></div>' + page_head("Live session &middot; Free to join", "Join the Community Call", body, aside) + f"""
<section class="section bg-white" id="newsletter">
  <div class="container">
    <div class="feature flip">
      <div class="feature-copy" data-stagger>
        <span class="eyebrow">Free weekly insights</span>
        <h2 class="h2">Not ready to book? Grow with us anyway.</h2>
        <div class="btn-row" style="margin-top:22px"><a class="btn btn-primary" href="{SITE['newsletter']}" {EXT}>Join The Impact Earnings Dispatch {ARR}</a></div>
        <p class="muted" style="margin-top:12px;font-size:var(--fs-xs)">Weekly education on digital assets &amp; aligned capital &middot; unsubscribe anytime</p>
        {fine()}
      </div>
      <div class="vis mist" data-reveal="left">
        <div class="vis-card mail" aria-hidden="true">
          <div class="mail-top"><span class="mail-ic">{ICON['mail']}</span><div><b>The Impact Earnings Dispatch</b><small>Free weekly insights</small></div></div>
          <div class="mail-body"><i style="width:82%"></i><i style="width:94%"></i><i style="width:68%"></i><i class="gap" style="width:88%"></i><i style="width:76%"></i><i style="width:58%"></i></div>
        </div>
      </div>
    </div>
  </div>
</section>
""" + cta() + footer()


def contact():
    return head("Contact &mdash; Impact Earnings",
                "Sometimes the best place to start is a conversation.",
                "contact") + page_head("Get in touch", 'Reach Francene <span class="accent">directly.</span>') + f"""
<section class="section bg-white">
  <div class="container split">
    <div class="panel forest" data-reveal="left" id="book">
      <span class="eyebrow">Book a call</span>
      <h2 class="h2">Chat with Francene</h2>
      <p style="margin-top:12px">Every person comes to this space from a different place. This is simply a chance to connect, learn more about where you are, what you&rsquo;re looking for, and what your goals are &mdash; and see whether there&rsquo;s a natural fit for how I may be able to help.</p>
      {steps(' style="margin-top:18px"')}
      <div class="btn-row" style="margin-top:22px">
        <a class="btn btn-gold" href="{SITE['book']}" {EXT}>Book a call {ARR}</a>
        <span style="font-size:var(--fs-xs)">Opens Francene&rsquo;s calendar</span>
      </div>
      {fine()}
    </div>
    <div>
      <div class="panel sage" data-reveal="right" id="message">
        <form class="form contact-form">
          <div class="form-row">
            <div class="field"><label for="cname">Your name</label><input id="cname" type="text" name="cname" autocomplete="name" required></div>
            <div class="field"><label for="cemail">Your email</label><input id="cemail" type="email" name="cemail" autocomplete="email" required></div>
          </div>
          <div class="field"><label for="cmessage">What would you like to explore?</label><textarea id="cmessage" name="cmessage" rows="5" required></textarea></div>
          <div class="hp" aria-hidden="true"><label for="c_honey">Leave this field empty</label><input type="text" id="c_honey" name="_honey" tabindex="-1" autocomplete="off"></div>
          <button class="btn btn-primary" type="submit">Send message {ARR}</button>
          <p class="form-status" role="status" aria-live="polite"></p>
          <p class="fineprint">We&rsquo;ll only use this to reply to you. <a href="/privacy">Privacy</a> &middot; {LINE}</p>
        </form>
      </div>
      <ul class="info-list" data-stagger id="direct">
        <li>{ICON['mail']}<div><b>Or write directly:</b><a class="link-arrow" href="mailto:{SITE['email']}">{SITE['email']}</a></div></li>
        <li>{ICON['link']}<div><b>Prefer LinkedIn?</b><a class="link-arrow" href="{SITE['linkedin']}" {EXT}>Connect with Francene {ARR}</a></div></li>
        <li>{ICON['video']}<div><b>Live session</b><a class="link-arrow" href="{SITE['call']}" {EXT}>Join the Community Call {ARR}</a></div></li>
      </ul>
      {fine()}
    </div>
  </div>
</section>
""" + footer()


def not_found():
    # System page: the original site had no 404, so this is the one place with new wording.
    body = f"""<div class="btn-row" data-hero style="--d:160;margin-top:8px">
        <a class="btn btn-primary" href="/">Impact Earnings {ARR}</a>
        <a class="btn btn-secondary" href="{SITE['book']}" {EXT}>Book a Call {ARR}</a>
      </div>
      {fine()}"""
    return head("Page not found &mdash; Impact Earnings", "Page not found.", "404") + page_head(
        "404", "Page not found.", body) + footer()


def privacy():
    page = head("Privacy &mdash; Impact Earnings", "How Impact Earnings and Impact Alpha Group handle the information you share through this site.", "privacy")
    if not PRIVACY_APPROVED and LAUNCH:   # keep the draft out of search results even after launch
        page = page.replace("<title>", '<meta name="robots" content="noindex">\n<title>', 1)
    body = privacy_body()
    if PRIVACY_APPROVED:
        body = body.replace(body[body.index('<p class="draft">'):body.index('<p class="updated">')], "")
    return page + page_head("Privacy", "Privacy") + body + footer()


PAGES = {"index.html": home, "about.html": about, "community.html": community,
         "contact.html": contact, "privacy.html": privacy, "404.html": not_found}

if __name__ == "__main__":
    for name, fn in PAGES.items():
        (ROOT / name).write_bytes(fn().encode("utf-8"))
        print("wrote", name)
