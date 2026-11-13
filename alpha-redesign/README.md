# Impact Alpha Group redesign (impactalphagroup.com)

The light, multi-page redesign of impactalphagroup.com, built on the same design system as [`../earnings-redesign/`](../earnings-redesign/). **Not live yet.**

It carries the live site's compliance work:
- compliant wording, with no deal figures, results or investor language,
- the advisory-only disclaimer next to every booking and contact button,
- an "Important information" footer block,
- a draft privacy page,
- full security headers,
- self-hosted fonts,
- form hardening,
- WCAG 2.1 AA accessibility checks.

Both redesigns share `partials.py`, `assets/site.css`, `assets/site.js` and `assets/gate.js`. Keep them identical: edit them in one folder and copy them to the other.

## Preview locally

```
node _source/serve.mjs 3001
```

Then open http://localhost:3001. The preview server applies `vercel.json`'s headers (the CSP included) and redirects.

## Editing

- **Wording:** edit `_source/build_pages.py` (page bodies) or `_source/site_config.py` (links, nav, disclaimer line, footer block, closing panel).
- **Rebuild:** run `python -I _source/build_pages.py`.
- **Check:** run `python -I _source/copycheck.py`. It confirms every visible sentence matches the live site's compliance-reviewed wording in `../alpha.html`.
- **The alignment map** in the hero is a labeled illustration. Its node labels and captions are teaching text, not claims about real projects.
- **Rules:** never add deal sizes, amounts raised, track records or "investor" wording unless Francene has documentation and a securities-aware lawyer has reviewed it.

## Security

Same as the Earnings redesign:
- `script-src 'self'`, no inline scripts,
- the only outside connection is FormSubmit for the contact form,
- self-hosted fonts,
- a honeypot on the form,
- one sessionStorage flag for the intro animation, no cookies, no analytics.

## Launch checklist

1. **Approvals:** Francene approves the wording and the privacy page, and confirms the legal name and the city and state.
2. In `_source/site_config.py`, set `LAUNCH = True` (and `PRIVACY_APPROVED = True` once approved). Rebuild.
3. In `vercel.json`, delete the `X-Robots-Tag` header.
4. Commit this folder. Then in Vercel, open the `impact-alpha-group` project → Settings → General → **Root Directory** = `alpha-redesign`.
5. **Fix `www.impactalphagroup.com` first:** add it to the `impact-alpha-group` project's domains, redirecting to the main address. It currently has no certificate, so visitors who type "www." get a security warning.
6. Deploy a preview, run the checks, then promote it to production.
7. After deploy, check the headers:
   ```
   curl -sI https://impactalphagroup.com | grep -i -E "content-security|strict-transport|x-frame|x-robots"
   ```
   There should be no `x-robots-tag`.
