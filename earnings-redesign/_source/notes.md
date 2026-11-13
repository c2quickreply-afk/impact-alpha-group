# Impact Earnings redesign: notes

## What it does (one sentence)
Impact Earnings teaches people, in plain language, how digital assets, crypto security, automated trading and new financial technology actually work, led by Francene Loomiller, who has 25+ years in financial markets. It's education only, never financial advice.

## Who it's for / main action
- Individuals who are curious or cautious about digital assets and want to understand them before they put money at risk.
- Main action: **book a free 30-minute conversation** (go.impactearnings.com/chatwithfrancene).
- Secondary actions: join the live Community Call on Zoom, subscribe to The Impact Earnings Dispatch, or send a message.

## Pages
The old site is a single page (`/`) with anchors (#earnings, #topics, #about, #newsletter, #book, #alpha-group, #contact). The live host also redirects /webinar, /newsletter and /chatwithfrancene to GoHighLevel, so none of those paths get pages here.

| Old | New | Content |
|---|---|---|
| `/` | `/` | Hero, credentials strip, thesis, three approach rows (Understand / Explore / Protect), five topics, founder teaser, how to start (3 steps) + CTA |
| `/#about` | `/about` | Francene's full bio, three principles, Impact Alpha Group, LinkedIn |
| `/#newsletter` + call card | `/community` | Community Call (Zoom) + The Impact Earnings Dispatch |
| `/#book`, `/#contact` | `/contact` | Book a call, contact form (FormSubmit, unchanged), email, LinkedIn |

## Hero concept
A light, realistic "live session" window: Francene teaching a clearly labeled illustrative market-cycle chart, with floating cards for the topics covered and her line "Access alone is not enough." It shows what you actually get: experienced, plain-language education.

## Palette
- Forest 900 (anchor) `#0e2419` · Forest 950 `#08170f` · Forest 700 `#1f4a35` · Emerald `#2c7a55`
- Gold (brand) `#d9b671` · Gold ink (text on light) `#8a6a2a`
- White `#ffffff` · Warm off-white `#faf7f0` · Sage `#eef3ee` · Mist `#e6eee9`
- Ink `#14231b` · Text `#33433a` · Muted `#5d6d64` · Line `#dde5df`
- Purple: none (all violet tokens, gradients and orbs removed)

## Loader (recorded from the original)
- Files: `_source/loader/loader.{html,css,js}`, frames in `_source/loader/frames/orig_*`.
- Marks draw via stroke-dashoffset 600→0 over 1.9s `cubic-bezier(.83,0,.17,1)`. Inner petals start at 0s, octagons at 0.2s, big petals at 0.4s.
- Wordmark (Spline Sans Mono 11px, .42em tracking) rises from translateY(120%) over 1s `cubic-bezier(.19,1,.22,1)`, starting at 0.4s.
- Bar fills scaleX 0→1 over 2s ease-io, starting at 0.2s.
- Emblem "pop" at 2.05s: scale 1→1.14→1 over 0.7s `cubic-bezier(.34,1.56,.64,1)`, with a gold drop-shadow glow.
- End trigger: `window.load` + 2650ms → `.done` (opacity/visibility .8s ease-io). Under reduced motion, load + 100ms.
- New: shows on the first page of a visit only (sessionStorage), has a hard fallback so it always dismisses, and a CSS failsafe in case JS never runs.


## Revision 2 (2026-11-06)

- All copy restored to the original wording, word for word (checked by `copycheck.py`). Invented headings, breadcrumbs and "On this page" boxes were removed.
- `/learn` was removed: with only the original wording it duplicated the homepage. Its content (three pillars plus What we cover) lives on `/`.
- Nav uses the original labels: About, Newsletter, Call, Contact, Book a Call.
- Square corners everywhere (radius tokens set to 0).
- Hero visual rebuilt as a Zoom-style call window, with no "Live" badge and no attributed quote card.
- Removed the decorative rings from the closing CTA panel.

## Revision 3 (2026-11-06)

- Corners softened slightly: radius tokens 3/5/8px, buttons and chips 4px.
- Hero slide is now "How an automated strategy works" (market data, AI model, your rules, execution), replacing the market-cycle chart.
- The mission heading and its summary line were removed (repetitive). That section now opens with "The Community Call / Free to join. Open to everyone." plus the original Zoom sentence. The user asked for the free-to-join wording; it is allow-listed in copycheck.py.
- The checklist visual is reframed from "Before you participate" to "What we work through on the call", with states going from Up next to Covered.
- Added a testimonial band under the founder block for Helen Korb, showing a dashed placeholder until her real words arrive. Set `HELEN_QUOTE` in build_pages.py. Never write it for her.
