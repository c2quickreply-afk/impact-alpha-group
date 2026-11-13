"""Brand content for this site. partials.py and the page code are shared with the
Impact Alpha Group redesign; only this file (and build_pages.py's page bodies)
differ between the two.

COPY RULE: wording comes from the live site's current (compliance-reviewed)
copy in the repo root (earnings.html). Don't add claims. Every booking, call,
newsletter and contact button gets LINE next to it.
"""

# Flip to True only when the site goes live: removes the noindex meta tag.
# Also remove the X-Robots-Tag header from vercel.json at the same time.
LAUNCH = False

# Flip to True once Francene approves the privacy policy (removes the draft banner and noindex).
PRIVACY_APPROVED = False

SITE = {
    "name": "Impact Earnings",
    "domain": "impactearnings.com",
    "logo_word": "IMPACT EARNINGS",
    "loader_word": "IMPACT&nbsp;EARNINGS",
    "tagline": "Where opportunity meets understanding",
    "book": "https://go.impactearnings.com/chatwithfrancene",
    "book_label": "Book a Call",
    "call": "https://us02web.zoom.us/meeting/register/nwRPTHkJT4OhX2Ibz0celw",
    "newsletter": "https://go.impactearnings.com/home-303039",
    "linkedin": "https://www.linkedin.com/in/franceneloomiller/",
    "email": "francene@impactearnings.com",
    "sister": "https://impactalphagroup.com",
    "sister_name": "Impact Alpha Group",
    "copyright": "&copy; 2026 Impact Earnings &middot; Impact Alpha Group",
}

# The short disclaimer line, next to every booking / call / newsletter / contact button.
LINE = "Education only &mdash; not investment, financial, legal or tax advice."

# The fuller block in every footer (same wording as the live site).
IMPORTANT = ("<b>Important information.</b> Impact Earnings provides education and information only; "
             "Impact Alpha Group provides advisory and coordination services. Nothing on this site, in our "
             "newsletter, on our calls, or in a conversation with Francene is investment, financial, legal, or "
             "tax advice, and nothing here is an offer, solicitation, or recommendation to buy or sell any "
             "security, digital asset, or other investment. Digital assets are highly volatile, and you can lose "
             "some or all of the money you put in. Past results, including any examples discussed, don&rsquo;t "
             "guarantee future results. Always do your own research and talk with a licensed professional about "
             "your own situation before making financial decisions.")

NAV_ITEMS = [  # original nav labels
    ("about", "/about", "About"),
    ("community", "/community#newsletter", "Newsletter"),
    ("community", "/community#call", "Call"),
    ("contact", "/contact", "Contact"),
]

FOOTER_LINKS = [  # (label, href, external)
    ("About", "/about", False),
    ("Impact Alpha Group", SITE["sister"], True),
    ("Book a call", SITE["book"], True),
    ("Newsletter", "/community#newsletter", False),
    ("Call", "/community#call", False),
    ("Contact", "/contact", False),
    ("LinkedIn", SITE["linkedin"], True),
    ("Privacy", "/privacy", False),
]

CTA = {
    "eyebrow": "Let&rsquo;s start a conversation",
    "heading": 'Sometimes the best place to start is <span class="accent">a conversation.</span>',
    "primary": ("Book a Call", SITE["book"]),
    "secondary": ("Join the Community Call", SITE["call"]),
    "fine": f'Not ready to book? Grow with us anyway. <a class="link-arrow" href="{SITE["newsletter"]}" target="_blank" rel="noopener">Join The Impact Earnings Dispatch <span class="arr" aria-hidden="true">&rarr;</span></a>',
    "steps": [
        "A free 30-minute conversation &mdash; no pitch, no pressure.",
        "We talk about where you are, what you&rsquo;re exploring, and what you&rsquo;d like to accomplish.",
        "Together, we&rsquo;ll see what makes sense, whether there&rsquo;s a natural fit, and what your best next step may be.",
    ],
}

# Browser storage this site uses (for the privacy page). Keep in sync with assets/.
STORAGE_NOTE = ("This site keeps one small setting in your browser&rsquo;s session storage so the intro animation "
                "plays only once per visit. It contains no personal information, isn&rsquo;t used for tracking, "
                "and is erased when you close the tab.")
