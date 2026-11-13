# Impact Earnings redesign (impactearnings.com)

The light, multi-page redesign of impactearnings.com. **Not live yet.** It carries the same compliance work as the live site:
- compliant wording,
- disclaimers next to every booking, call, newsletter and contact button,
- an "Important information" footer block,
- a draft privacy page,
- full security headers,
- self-hosted fonts,
- form hardening,
- WCAG 2.1 AA accessibility checks.

Its sister site is [`../alpha-redesign/`](../alpha-redesign/). Both share the same `partials.py`, `assets/site.css`, `assets/site.js` and `assets/gate.js`. Keep those identical: edit them in one folder and copy them to the other.

## Preview locally

```
node _source/serve.mjs 3000
```

Then open http://localhost:3000. The preview server applies `vercel.json`'s headers (the CSP included) and redirects, so a CSP mistake shows up locally exactly as it would in production.

## Editing

The pages are generated:
- **Wording:** edit `_source/build_pages.py` (page bodies) or `_source/site_config.py` (links, nav, disclaimer line, footer block, closing panel).
- **Rebuild:** run `python -I _source/build_pages.py`.
- **Check:** run `python -I _source/copycheck.py`. It confirms every visible sentence matches the live site's compliance-reviewed wording in `../earnings.html`.
- **Rules:** never add claims, figures, results or testimonials that aren't documented. Every new booking, call, newsletter or contact button gets `fine()` (the disclaimer line) next to it.

## Security

- **No inline scripts**, so the CSP is `script-src 'self'`, with no hashes to maintain.
- The only outside connection allowed is the contact form's `fetch` to `https://formsubmit.co`.
- Fonts are self-hosted in `fonts/` (SIL Open Font License).
- **Contact form:** FormSubmit, with a honeypot (`_honey`). The endpoint is `FORM_ENDPOINT` in `assets/site.js`. To hide Francene's email address, swap in FormSubmit's random-string alias (see the repo root README), then copy `site.js` to `../alpha-redesign/` too.
- **Browser storage:** one sessionStorage flag so the intro plays once per visit. No cookies, no analytics. The privacy page says so.

## Launch checklist

1. **Approvals:** Francene approves the wording and the privacy page, and confirms the legal name and the city and state for it.
2. In `_source/site_config.py`, set `LAUNCH = True`. Once the privacy page is approved and its brackets are filled in, set `PRIVACY_APPROVED = True` too. Rebuild.
3. In `vercel.json`, delete the `X-Robots-Tag` header.
4. Helen's testimonial: put her real words in `HELEN_QUOTE` (`build_pages.py`). With `LAUNCH = True` and no quote, the section is left out automatically.
5. Commit this folder. Then in Vercel, open the `impact-earnings` project → Settings → General → **Root Directory** = `earnings-redesign`. The project then deploys this folder with its own `vercel.json`. The old `earnings.html` and the root `vercel.json` stop being used for impactearnings.com.
6. Deploy a preview, run the checks, then promote it to production.
7. After deploy, check the headers:
   ```
   curl -sI https://www.impactearnings.com | grep -i -E "content-security|strict-transport|x-frame|x-robots"
   ```
   There should be no `x-robots-tag`. Also confirm `/webinar`, `/newsletter` and `/chatwithfrancene` still redirect.
