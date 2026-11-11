# Impact Earnings & Impact Alpha Group

Websites for Francene Loomiller's two brands:

- **impactearnings.com**: digital-asset education for individuals (education only, never financial advice). Page: [`earnings.html`](earnings.html).
- **impactalphagroup.com**: strategic advisory and partnerships for builders and institutions. Page: [`alpha.html`](alpha.html).
- **/privacy** on both domains: [`privacy.html`](privacy.html). It's currently a **draft awaiting Francene's approval**; see "Privacy page" below.

Plain HTML, no build step, no dependencies. Fonts are self-hosted in [`fonts/`](fonts/).

## How it's deployed

GitHub `main` deploys to **two Vercel projects**, both connected to this repo:

| Vercel project | Domains | Serves `/` as |
|---|---|---|
| `impact-earnings` | impactearnings.com, www.impactearnings.com | `earnings.html` |
| `impact-alpha-group` | impactalphagroup.com, www.impactalphagroup.com | `alpha.html` |

Both projects use the same [`vercel.json`](vercel.json). Host-based rewrites pick the page, so **a push to `main` updates both sites at once.** Pushing any other branch creates preview deployments on both projects. The `impact-alpha-group-*.vercel.app` preview URLs serve the Alpha page.

Redirects (keep these working): `/webinar`, `/newsletter` and `/chatwithfrancene` on impactearnings.com go to the matching pages on `go.impactearnings.com`. That subdomain is hosted on HighLevel (LeadConnector), not in this repo. `/alpha.html`, `/earnings.html` and `/index.html` redirect to `/`.

`earnings-redesign/` is an unfinished local redesign. It's listed in [`.vercelignore`](.vercelignore), so it's never deployed even if it gets committed.

## Security headers

All headers are set in `vercel.json` for every route:

- `Content-Security-Policy`
- `Strict-Transport-Security: max-age=63072000; includeSubDomains`
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Permissions-Policy` (camera, microphone, geolocation, payment and the rest all off)
- `Cross-Origin-Opener-Policy: same-origin`
- `Cross-Origin-Resource-Policy: same-origin`
- `X-XSS-Protection: 0`

The CSP allows only what the pages use:

- **Same-origin** files: pages, fonts and the photo.
- **Inline styles:** `'unsafe-inline'` is allowed for styles, never for scripts.
- **A `data:` favicon.**
- **The inline script in each page**, pinned by its SHA-256 hash.
- **`fetch` to `https://formsubmit.co`** for the contact form.

Everything else is blocked, including framing by other sites.

> **⚠️ If you edit the `<script>` block in `alpha.html` or `earnings.html`, you must update its hash in `vercel.json`, or that page's JavaScript stops running.** The page still *looks* fine, so this is easy to miss. The loader never lifts, the animations die and the contact form stops working.

Regenerate both hashes, then paste them into the `script-src` directive in `vercel.json` (the order doesn't matter). The command normalizes line endings first, because browsers hash the script with LF endings even when a Windows checkout has CRLF:

```bash
node -e "const fs=require('fs'),c=require('crypto');for(const f of ['alpha.html','earnings.html']){const s=fs.readFileSync(f,'utf8').replace(/\r\n?/g,'\n'),a=s.indexOf('<script>')+8,z=s.indexOf('</script>',a);console.log(f+'  sha256-'+c.createHash('sha256').update(s.slice(a,z),'utf8').digest('base64'))}"
```

Editing the `<style>` block, any `style="..."` attribute, or the page text is safe and needs no hash update. [`.gitattributes`](.gitattributes) keeps every file on LF endings.

After each deploy, check the headers on all four hostnames, and open each site with the browser console open: there should be no CSP errors.

```bash
for d in www.impactearnings.com impactearnings.com impactalphagroup.com www.impactalphagroup.com; do echo "== $d"; curl -sIL "https://$d" | grep -i -E "^HTTP|content-security|strict-transport|x-frame|referrer-policy|permissions-policy|cross-origin-opener"; done
```

## Contact form

The contact form on both sites posts in the page (`fetch`) to **FormSubmit**, which emails the message to francene@impactearnings.com. It sends name, email, message and a hidden `_honey` field. FormSubmit throws away any submission where `_honey` is filled in, which is how it catches simple bots. FormSubmit's captcha can't be used with in-page (AJAX) submissions, so the honeypot is the spam protection.

**To-do: hide the email address in the form URL.** The endpoint is the `FORM_ENDPOINT` constant near the bottom of each page's script, and it still contains Francene's address. To swap it:

1. In Francene's inbox, find the original FormSubmit activation email for francene@impactearnings.com (from FormSubmit, subject mentioning activation or confirmation). It includes a random-string alias you can use in place of the email address.
2. In **both** `earnings.html` and `alpha.html`, change `FORM_ENDPOINT` to `https://formsubmit.co/ajax/<that-random-string>`.
3. Regenerate the CSP hashes (above), deploy a preview, and send one test message to confirm it still arrives.

If the activation email can't be found, FormSubmit sends a fresh activation email the first time a form posts to a new address. Ask FormSubmit support before changing the address the form uses.

## Privacy page

[`privacy.html`](privacy.html) is a **draft**. Before it goes live for real:

1. Cal or Francene confirms the two bracketed items: the legal business name, and the city and state.
2. Francene reads and approves it.
3. Remove the "Draft for review" banner and the `noindex` meta tag, and update "Last updated".

The policy describes exactly what the sites collect:

- the contact form, via FormSubmit,
- newsletter, call registration and booking pages on HighLevel,
- Zoom registration,
- hosting logs at Vercel,
- email at Google Workspace.

The two sites themselves set no cookies and use no analytics or browser storage.

**Keep it accurate.** If you add a tool that collects anything (analytics, a chat widget, a new form provider), update the policy and its date in the same change.

## Content rules (financial-promotion risk)

This is financial and digital-asset education plus advisory work, so the wording is kept conservative:

- **Never** promise returns, income or earnings.
- **Never** recommend buying or selling anything, or predict prices.
- **Never** invite anyone to invest through Francene.
- **Never** state performance figures or deal amounts that aren't documented.
- **Never** imply a license she doesn't hold.

Every page carries a short disclaimer line next to its booking, call, newsletter and contact buttons, plus an "Important information" block in the footer. Keep those whenever you add a new button or section.

## Accessibility notes

- There's a skip link and a `<main>` landmark, and headings run in order.
- Form fields have real labels, and form status messages are announced to screen readers.
- Ambient animation (the canvas, the marquee and the auroras) stops for visitors with "reduce motion" turned on. Everyone else can stop it with the **Pause animations** button in the footer.
- Pages reflow at 320px wide and at 200% zoom.
- Checked with axe-core 4.10.2: no critical, serious or moderate issues.
