"""Brand content for the Impact Alpha Group redesign. partials.py and the page
code are shared with the Impact Earnings redesign; only this file (and
build_pages.py's page bodies) differ.

COPY RULE: wording comes from the live site's current (compliance-reviewed)
copy in the repo root (alpha.html). Don't add claims, figures or results.
Every booking and contact button gets LINE next to it.
"""

# Flip to True only when the site goes live: removes the noindex meta tag.
# Also remove the X-Robots-Tag header from vercel.json at the same time.
LAUNCH = False

# Flip to True once Francene approves the privacy policy (removes the draft banner and noindex).
PRIVACY_APPROVED = False

SITE = {
    "name": "Impact Alpha Group",
    "domain": "impactalphagroup.com",
    "logo_word": "IMPACT ALPHA GROUP",
    "loader_word": "IMPACT&nbsp;ALPHA&nbsp;GROUP",
    "tagline": "Where capital meets alignment",
    "book": "https://go.impactearnings.com/chatwithfrancene",
    "book_label": "Book a Call",
    "linkedin": "https://www.linkedin.com/in/franceneloomiller/",
    "email": "francene@impactearnings.com",
    "sister": "https://impactearnings.com",
    "sister_name": "Impact Earnings",
    "copyright": "&copy; 2026 Impact Alpha Group",
}

LINE = ("Advisory services only &mdash; not investment, financial, legal or tax advice, "
        "and not an offer to buy or sell any security.")

IMPORTANT = ("<b>Important information.</b> Impact Alpha Group provides strategic advisory and coordination "
             "services for complex projects, and this site is for general information only. Nothing on this "
             "site is investment, financial, legal, or tax advice, and nothing here is an offer to sell, or a "
             "solicitation of an offer to buy, any security, digital asset, or other investment. Initiatives "
             "described are examples of the kinds of work we support and are subject to independent diligence; "
             "past results don&rsquo;t guarantee future results. Digital assets and early-stage projects are "
             "volatile and involve significant risk, including the loss of some or all of the money put in. Talk "
             "with licensed professionals about your own situation before making financial decisions.")

NAV_ITEMS = [  # original nav labels (Sectors, Approach, About) + Contact from the footer
    ("sectors", "/#sectors", "Sectors"),
    ("approach", "/approach", "Approach"),
    ("about", "/about", "About"),
    ("contact", "/contact", "Contact"),
]

FOOTER_LINKS = [  # original footer labels
    ("Sectors", "/#sectors", False),
    ("Approach", "/approach", False),
    ("About", "/about", False),
    ("Book a call", SITE["book"], True),
    ("Contact", "/contact", False),
    ("Impact Earnings", SITE["sister"], True),
    ("LinkedIn", SITE["linkedin"], True),
    ("Privacy", "/privacy", False),
]

CTA = {
    "eyebrow": "Let&rsquo;s explore alignment",
    "heading": 'Every great outcome starts with <span class="accent">one call.</span>',
    "primary": ("Book a consultation", SITE["book"]),
    "secondary": ("See how we work", "/approach"),
    "fine": f'Prefer LinkedIn? <a class="link-arrow" href="{SITE["linkedin"]}" target="_blank" rel="noopener">Connect with Francene <span class="arr" aria-hidden="true">&rarr;</span></a>',
    "steps": [
        "A 30-minute working conversation &mdash; no pitch, no pressure.",
        "We map the initiative in context &mdash; capital pathways, partners, incentives, constraints.",
        "You leave with a clear read on alignment &mdash; whether or not we engage.",
    ],
}

STORAGE_NOTE = ("This site keeps one small setting in your browser&rsquo;s session storage so the intro animation "
                "plays only once per visit. It contains no personal information, isn&rsquo;t used for tracking, "
                "and is erased when you close the tab.")
