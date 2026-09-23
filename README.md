# Impact Alpha — Where Capital Meets Alignment

Marketing site for **Impact Alpha** — home to the **Impact Earnings** and **Impact Alpha
Group** tracks — the capital-strategy and education practice led by Francene Loomiller.

Deployed via Vercel from this repository to impactearnings.com and impactalphagroup.com.

The entire site is a single self-contained file — [`index.html`](index.html) — with no build
step and no dependencies beyond Google Fonts. Open it in a browser, or serve it with any
static host.

## Structure

- **Track 01 — Impact Earnings**: digital-asset education for individuals (education only,
  never financial advice).
- **Track 02 — Impact Alpha Group**: advisory and strategic partnerships for builders and
  institutions.
- Both tracks route to cal.com booking links.

## Security headers

Security headers are set in [`vercel.json`](vercel.json) — they are response headers only and
change nothing about how the site looks or behaves.

The Content-Security-Policy allows exactly what the pages use: Google Fonts
(`fonts.googleapis.com` / `fonts.gstatic.com`), the contact form's `fetch` to `formsubmit.co`,
and a `data:` favicon. Everything else is denied.

> **⚠️ If you edit the `<script>` block in `alpha.html` or `earnings.html`, you must update the
> CSP hash or that page's JavaScript will stop running.** The page will still look correct, so
> the breakage is easy to miss — scroll animations and the contact form would silently fail.

Regenerate the hashes and paste them into the `script-src` directive in `vercel.json`:

```bash
node -e "const fs=require('fs'),c=require('crypto');for(const f of ['alpha.html','earnings.html']){const b=fs.readFileSync(f),s=b.toString('binary'),a=s.indexOf('<script>')+8,z=s.indexOf('</script>',a);console.log(f+'  sha256-'+c.createHash('sha256').update(b.slice(a,z)).digest('base64'))}"
```

Editing the `<style>` block or any `style="..."` attribute is safe and needs no update.

After deploying, confirm the headers are live and the console is free of CSP errors:

```bash
curl -sI https://impactalphagroup.com | grep -i -E "content-security|strict-transport|x-frame"
```

## Before launch

Search `index.html` for `REPLACE` comments and swap in:

1. Francene's real **cal.com** links (2 buttons + 2 booking cards).
2. A real **LinkedIn** URL (footer + booking section).
3. A newsletter/email-list backend for the subscribe form.
