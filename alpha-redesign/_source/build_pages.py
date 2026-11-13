"""Writes the Impact Alpha Group pages from partials.py + the page bodies below.
Run from alpha-redesign/:  python -I _source/build_pages.py

COPY RULE: every sentence outside the illustrative alignment map is copied word
for word from the live site's compliance-reviewed copy (repo root alpha.html).
No deal figures, results or investor language. Every booking and contact
button gets the disclaimer line (fine()) next to it.
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
    "map": f'<svg {_S}><path d="M3 6l6-3 6 3 6-3v15l-6 3-6-3-6 3z"/><path d="M9 3v15M15 6v15"/></svg>',
    "mail": f'<svg {_S}><path d="M3 5h18v14H3z"/><path d="M3.5 6.5L12 13l8.5-6.5"/></svg>',
    "link": f'<svg {_S}><path d="M3 3h18v18H3z"/><path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/></svg>',
    "cal": f'<svg {_S}><path d="M3 5h18v16H3z"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
}
TICK = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 6.2l2.3 2.3L9.5 3.8"/></svg>'

PILLARS = [
    ("Strategic development &amp; positioning", "Clarifying the initiative's value and shaping narratives that speak directly to stakeholder priorities."),
    ("Capital pathways &amp; financing readiness", "Helping project teams understand and prepare for financing options &mdash; private lending, equity, impact capital, grants, incentives, and tax-credit programs."),
    ("Partnership &amp; stakeholder alignment", "Relationships that begin with a single introduction and evolve into long-term shared objectives."),
    ("Executive communications &amp; documentation", "Executive summaries, proposals, and financing and partner materials made clear, credible, and decision-ready."),
    ("Organizational excellence &amp; accountability", "Reporting, financial visibility, workflows, and follow-through that keep every commitment in view."),
]

SECTORS = [
    ("SECTOR 01", "Community &amp; economic development", "Workforce and attainable housing, mixed-use, and civic infrastructure &mdash; coordinating capital sources, incentive programs, and stakeholders so development creates durable value for the communities it touches.", "Development &middot; Public-Private"),
    ("SECTOR 02", "Sustainable infrastructure", "Regenerative construction, energy and advanced building systems, and environmental restoration &mdash; projects where sustainability is structural to the capital thesis, not a marketing layer on top of it.", "Infrastructure &middot; Regenerative"),
    ("SECTOR 03", "Carbon finance", "Carbon markets and environmental assets &mdash; structuring credits, offsets, and green incentives directly into a project's capital stack, where they change the economics.", "Markets &middot; Environmental"),
]

AREAS = ["Regenerative development", "Carbon finance", "Sustainable infrastructure", "Workforce &amp; attainable housing",
         "Microgrid energy", "Community development", "Environmental restoration", "Mixed-use development",
         "Capital pathways", "Strategic partnerships", "Stakeholder alignment", "Grants &amp; tax credits",
         "Blended finance", "Mission-aligned capital", "Emerging technologies"]

WORK = [  # the live site's compliant "kinds of work" cards
    ("Early-stage initiatives", "Strategic positioning and stakeholder alignment for initiatives in their earliest stages of development, including international carbon-finance work.", "Strategic development"),
    ("Housing &amp; development", "Financing readiness, partner coordination, and incentive planning for housing and mixed-use development.", "Financing readiness"),
    ("Cross-border initiatives", "Partner and stakeholder alignment for large-scale climate, water-restoration, infrastructure, and community-development work.", "Partnership alignment"),
    ("25+ years", "Spanning institutional client development, digital-asset communities, and mission-driven organizations.", "Career experience"),
]


def topics_list(items):
    rows = []
    for i, (t, d) in enumerate(items):
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
    items = [("Trust", "earned over time"), ("Alignment", "shared purpose"), ("Stewardship", "long-term care"),
             ("Excellence", "clear systems"), ("Service", "the measure")]
    return '<div class="principles five" data-stagger>\n' + "\n".join(
        f'          <div class="principle"><b>{b}</b><span>{s}</span></div>' for b, s in items) + "\n        </div>"


PORTRAIT_CAP = "<figcaption><b>Francene Loomiller</b><small>Founder &middot; Impact Alpha Group</small></figcaption>"

# ----------------------------------------------------------------------------
# Hero visual: an initiative alignment map (illustrative; labels are not claims)
# ----------------------------------------------------------------------------
NODES = [  # (label, caption, x%, y%)
    ("Leadership", "Leadership sets the vision and makes the decisions that carry it.", 50, 12),
    ("Strategic partners", "Strategic partners commit to shared objectives.", 78, 31),
    ("Public agencies", "Public agencies and incentive programs come into view.", 78, 69),
    ("Financing options", "Financing options are mapped and prepared for: grants, lending, tax credits.", 50, 88),
    ("Technical advisors", "Engineers and technical advisors test the plan against reality.", 22, 69),
    ("Community", "Community benefit is designed in from the start.", 22, 31),
]
STAGES = ["Vision", "Positioning", "Financing readiness", "Partnerships", "Implementation"]


def amap():
    lines = "".join(f'<line class="am-line" x1="50" y1="50" x2="{x}" y2="{y}"/>' for _, _, x, y in NODES)
    nodes = "\n".join(
        f'              <div class="am-node" style="--x:{x}%;--y:{y}%" data-cap="{c}"><i>{TICK}</i><b>{l}</b></div>'
        for l, c, x, y in NODES)
    stages = "".join(f'<span class="am-stage">{s}</span>' for s in STAGES)
    return f"""<div class="hero-visual" id="heroVisual">
        <div class="amap" id="amap" data-hero style="--d:250" role="img" aria-label="Illustration: an initiative at the center, with leadership, strategic partners, public agencies, financing options, technical advisors and the community being brought into alignment, from vision through implementation">
          <div class="amap-bar" aria-hidden="true">
            <span class="amap-title">{ICON['map']}Initiative alignment map</span>
            <span class="tag-illus">Illustrative</span>
          </div>
          <div aria-hidden="true">
            <div class="am-board">
              <svg class="am-lines" viewBox="0 0 100 100" preserveAspectRatio="none">{lines}</svg>
              <div class="am-core"><b>Your initiative</b><small>Vision &rarr; implementation</small></div>
{nodes}
            </div>
            <div class="am-stages">{stages}</div>
            <div class="am-foot"><p id="amDetail" data-start="Every initiative starts with its stakeholders, in context.">Every initiative starts with its stakeholders, in context.</p></div>
            <p class="am-note">Teaching example of how alignment comes together. Not a specific project.</p>
          </div>
        </div>
      </div>"""


# ----------------------------------------------------------------------------
# Pages
# ----------------------------------------------------------------------------
HOME_DESC = ("Impact Alpha Group provides strategic development and partnership advisory for complex, mission-driven "
             "projects &mdash; community and economic development, sustainable infrastructure, workforce housing, and "
             "carbon finance. Led by Francene Loomiller. Advisory only, not investment advice.")


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


def home():
    sectors = "\n".join(f"""      <article class="sector">
        <span class="k">{k}</span>
        <h3 class="h3">{t}</h3>
        <p>{d}</p>
        <span class="tag">{tag}</span>
      </article>""" for k, t, d, tag in SECTORS)
    chips = "".join(f"<li>{a}</li>" for a in AREAS)
    return head("Impact Alpha Group &mdash; Where Capital Meets Alignment", HOME_DESC, "home", og=True) + f"""
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-copy">
        <span class="eyebrow" data-hero style="--d:0">Institutional Advisory &middot; Complex Capital Projects</span>
        <h1 class="h1" data-hero style="--d:80">Where capital meets <span class="accent">alignment.</span></h1>
        <p class="lead" data-hero style="--d:180">Impact Alpha Group is a strategic development and partnership firm for complex, mission-driven capital projects &mdash; aligning the relationships, financing readiness, and disciplined follow-through that help large-scale initiatives move from vision through implementation. Led by Francene Loomiller.</p>
        <div class="btn-row" data-hero style="--d:280">
          <a class="btn btn-primary" href="{SITE['book']}" {EXT}>Book a consultation {ARR}</a>
          <a class="btn btn-secondary" href="/approach">See how we work</a>
        </div>
        <p class="hero-note" data-hero style="--d:380">{ICON['shield']}{LINE}</p>
      </div>
      {amap()}
    </div>
  </div>
  <div class="creds">
    <div class="container">
      <div class="creds-grid" data-stagger>
        <div class="cred"><p class="cred-num"><span data-count="25">25</span><span class="suf">+</span></p><p class="cred-label">Years in financial markets</p></div>
        <div class="cred"><p class="cred-num"><span data-count="3">3</span></p><p class="cred-label">Focus sectors &middot; community, infrastructure, carbon</p></div>
        <div class="cred"><p class="cred-num">Advisory</p><p class="cred-label">Strategy, partnerships &amp; stakeholder coordination</p></div>
        <div class="cred"><p class="cred-num">Selective</p><p class="cred-label">Every engagement begins with alignment</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-sage">
  <div class="container thesis">
    <div data-reveal>
      <span class="eyebrow">The thesis</span>
      <p class="thesis-lede">Capital is powerful. <span class="accent">Alignment is everything.</span></p>
    </div>
    <div>
      <p class="statement" id="statement" data-em="alignment">In complex initiatives, the greatest constraint is rarely money &mdash; it&rsquo;s aligning leadership, capital partners, strategic partners, and the many stakeholders needed to move a vision forward. But alignment doesn&rsquo;t happen on paper.</p>
      <p class="lead" style="margin-top:20px" data-reveal>It&rsquo;s built through trust, strong relationships, clear communication, and a shared commitment to the vision and the path forward. When those elements come together, momentum builds and opportunities begin to take shape. That&rsquo;s where we come in.</p>
      <div class="thesis-tail" data-stagger>
        <span class="pill">{ICON['check']}Trust</span><span class="pill">{ICON['check']}Alignment</span><span class="pill">{ICON['check']}Stewardship</span><span class="pill">{ICON['check']}Execution</span>
      </div>
    </div>
  </div>
</section>

<section class="section bg-white" id="sectors">
  <div class="container">
    <div class="section-head">
      <div data-reveal>
        <span class="eyebrow">Where we work</span>
        <h2 class="h2">Three arenas. One discipline: <span class="accent">alignment.</span></h2>
      </div>
      <div class="section-aside" data-reveal style="--d:120">
        <p class="lead">Complex capital projects fail in the seams &mdash; between funders and builders, incentives and timelines, public mandates and private returns. We work in the sectors where those seams matter most, and we hold them together.</p>
      </div>
    </div>
    <div class="sectors" data-stagger>
{sectors}
    </div>
    <div class="chip-cloud" data-reveal>
      <ul class="chip-list">{chips}</ul>
    </div>
    <div class="btn-row" style="margin-top:28px" data-reveal>
      <a class="link-arrow" href="/approach">See how we work {ARR}</a>
      <span class="muted" style="font-size:var(--fs-xs)">Advisory only &middot; every engagement begins with alignment</span>
    </div>
  </div>
</section>

<section class="section bg-cream">
  <div class="container founder">
    <figure class="portrait" data-reveal="left">
      <img src="/images/francene.jpg" alt="Francene Loomiller, founder of Impact Alpha Group" width="854" height="1280" loading="lazy">
      {PORTRAIT_CAP}
    </figure>
    <div>
      <div data-stagger>
        <span class="eyebrow">The people</span>
        <h2 class="h2">Trust, cultivated over <span class="accent">25 years.</span></h2>
        <p class="lead" style="margin-top:16px"><b>Francene operates at the intersection of capital, relationships, and execution.</b> She began her career in institutional equity trading and sales, building more than twenty-five years of experience across financial markets &mdash; where sound judgment, disciplined execution, and trusted relationships were essential.</p>
      </div>
      {principles()}
      <div class="btn-row" style="margin-top:28px" data-reveal>
        <a class="btn btn-secondary" href="/about">Meet Francene {ARR}</a>
      </div>
    </div>
  </div>
</section>
""" + cta() + footer()


def approach():
    work = "\n".join(f'      <div class="work"><b>{t}</b><p>{d}</p><span class="tag">{tag}</span></div>' for t, d, tag in WORK)
    body = '<p class="lead" data-hero style="--d:160">We begin with the initiative in context &mdash; vision, stakeholders, financing needs, constraints &mdash; then coordinate the financing readiness, partnerships, communications, and follow-through that help large-scale initiatives move from vision through implementation. Five pillars, one discipline.</p>'
    return head("Approach &mdash; Impact Alpha Group",
                "We begin with the initiative in context, then coordinate the financing readiness, partnerships, communications, and follow-through that help large-scale initiatives move from vision through implementation.",
                "approach") + page_head("The approach", 'Where builders and aligned partners <span class="accent">converge.</span>', body) + f"""
<section class="section bg-white">
  <div class="container">
    {topics_list(PILLARS)}
    <div class="work-grid" data-stagger>
{work}
    </div>
    <div class="btn-row" style="margin-top:32px" data-reveal>
      <a class="btn btn-primary" href="{SITE['book']}" {EXT}>Book a consultation {ARR}</a>
      <a class="btn btn-secondary" href="#start">See how a call works</a>
    </div>
    {fine(' data-reveal')}
  </div>
</section>
""" + cta() + footer()


def about():
    return head("About &mdash; Impact Alpha Group",
                "Francene operates at the intersection of capital, relationships, and execution.",
                "about") + page_head("The people", 'Trust, cultivated over <span class="accent">25 years.</span>') + f"""
<section class="section bg-white" id="story">
  <div class="container split">
    <div class="sticky-col">
      <figure class="portrait" data-reveal="left">
        <img src="/images/francene.jpg" alt="Francene Loomiller" width="854" height="1280">
        {PORTRAIT_CAP}
      </figure>
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
        <p class="intro"><b>Francene operates at the intersection of capital, relationships, and execution.</b> She began her career in institutional equity trading and sales, building more than twenty-five years of experience across financial markets &mdash; where sound judgment, disciplined execution, and trusted relationships were essential.</p>
        <p>Her work later expanded into nonprofit leadership through Schoolyard Crop, an environmental education initiative that brought edible gardens and systems thinking into schools &mdash; strengthening her commitment to community engagement, partnership development, and creating pathways for people to participate more meaningfully in the systems shaping their lives.</p>
        <p>She ultimately returned to the financial markets through digital assets, blockchain ecosystems, and emerging financial technologies &mdash; rooted in a desire to help level the playing field by expanding access to education, technology, and opportunities that have historically been difficult for individuals and communities to reach.</p>
        <p>Across traditional finance, private capital, digital assets, technology, and mission-driven enterprise, her consistent strength is cultivating trust quickly and building durable relationships. Many of the partnerships she coordinates begin with a single introduction &mdash; and evolve into long-term strategic alignment.</p>
      </div>
      {principles()}
      <div class="btn-row" style="margin-top:28px" data-reveal>
        <a class="btn btn-primary" href="{SITE['book']}" {EXT}>Book a consultation {ARR}</a>
        <span class="muted" style="font-size:var(--fs-small)">Prefer LinkedIn? <a class="link-arrow" href="{SITE['linkedin']}" {EXT}>Connect with Francene {ARR}</a></span>
      </div>
      {fine(' data-reveal')}
    </div>
  </div>
</section>

<section class="section bg-sage" id="individuals">
  <div class="container">
    <div class="panel split" data-reveal="scale" style="align-items:center">
      <div>
        <span class="eyebrow">For individuals</span>
        <h2 class="h2">A separate path for <span class="accent">individual exploration.</span></h2>
      </div>
      <div>
        <p>Impact Alpha Group is focused on institutional initiatives, complex projects, and strategic partnerships. Francene&rsquo;s work also includes a separate educational platform for individuals, entrepreneurs, and professionals who want to better understand digital assets, emerging financial technologies, and new models of participation in the evolving financial economy.</p>
        <p style="margin-top:12px">Through Impact Earnings, she shares educational resources, market perspectives, and technology demonstrations with her community &mdash; education only, distinct from Impact Alpha Group&rsquo;s institutional advisory services, but informed by the same principles: relationships, education, thoughtful due diligence, and responsible participation.</p>
        <div class="btn-row" style="margin-top:22px"><a class="btn btn-primary" href="{SITE['sister']}" {EXT}>Explore Impact Earnings {ARR}</a></div>
      </div>
    </div>
  </div>
</section>
""" + cta(bg="bg-white") + footer()


def contact():
    return head("Contact &mdash; Impact Alpha Group",
                "Reach Francene directly. A 30-minute working conversation, no pitch, no pressure.",
                "contact") + page_head("Get in touch", 'Reach Francene <span class="accent">directly.</span>') + f"""
<section class="section bg-white">
  <div class="container split">
    <div id="book">
      <div class="book-cards" data-stagger>
        <a class="book-card" href="{SITE['book']}" {EXT}>
          <span class="k">For project sponsors</span>
          <h2 class="h3">Bring us your <span class="accent">initiative.</span></h2>
          <p>You&rsquo;re developing something complex &mdash; community, construction, or carbon &mdash; and the capital stack, partners, or incentives need coordination.</p>
          <span class="go">Opens Francene&rsquo;s calendar {ARR}</span>
        </a>
        <a class="book-card alt" href="{SITE['book']}" {EXT}>
          <span class="k">For institutional partners</span>
          <h2 class="h3">Partner with <span class="accent">alignment.</span></h2>
          <p>You represent an institution, public agency, or mission-aligned organization &mdash; and want to explore strategic partnerships around complex projects.</p>
          <span class="go">Opens Francene&rsquo;s calendar {ARR}</span>
        </a>
      </div>
      {steps(' style="margin-top:22px" data-theme="light"')}
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
      </ul>
    </div>
  </div>
</section>
""" + footer()


def privacy():
    page = head("Privacy &mdash; Impact Alpha Group", "How Impact Alpha Group and Impact Earnings handle the information you share through this site.", "privacy")
    if not PRIVACY_APPROVED and LAUNCH:
        page = page.replace("<title>", '<meta name="robots" content="noindex">\n<title>', 1)
    body = privacy_body()
    if PRIVACY_APPROVED:
        body = body.replace(body[body.index('<p class="draft">'):body.index('<p class="updated">')], "")
    return page + page_head("Privacy", "Privacy") + body + footer()


def not_found():
    body = f"""<div class="btn-row" data-hero style="--d:160;margin-top:8px">
        <a class="btn btn-primary" href="/">Impact Alpha Group {ARR}</a>
        <a class="btn btn-secondary" href="{SITE['book']}" {EXT}>Book a Call {ARR}</a>
      </div>
      {fine()}"""
    return head("Page not found &mdash; Impact Alpha Group", "Page not found.", "404") + page_head("404", "Page not found.", body) + footer()


PAGES = {"index.html": home, "approach.html": approach, "about.html": about,
         "contact.html": contact, "privacy.html": privacy, "404.html": not_found}

if __name__ == "__main__":
    for name, fn in PAGES.items():
        (ROOT / name).write_bytes(fn().encode("utf-8"))
        print("wrote", name)
