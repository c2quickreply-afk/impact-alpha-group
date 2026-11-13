// Zero-dependency local preview server that behaves like Vercel for this site:
// clean URLs (/about -> about.html), plus the headers (CSP included) and
// redirects from ../vercel.json, re-read on every request. So a CSP mistake
// shows up locally exactly as it would in production.
//   node _source/serve.mjs [port]
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const PORT = +(process.argv[2] || process.env.PORT || 3000);
const TYPES = { ".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8", ".js": "text/javascript; charset=utf-8",
  ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp",
  ".ico": "image/x-icon", ".json": "application/json", ".txt": "text/plain; charset=utf-8", ".woff2": "font/woff2" };
// Never served (mirrors .vercelignore).
const PRIVATE = /^\/(_source|\.vercelignore|\.gitattributes|README|vercel\.json)/i;

function config() {
  try { return JSON.parse(fs.readFileSync(path.join(ROOT, "vercel.json"), "utf8")); } catch { return {}; }
}

function resolve(p) {
  if (PRIVATE.test(p) || p.split("/").some(seg => seg.startsWith("."))) return null;
  if (p.endsWith(".html")) return { redirect: p.replace(/(index)?\.html$/, "") || "/" };   // cleanUrls
  const abs = path.join(ROOT, p);
  if (!abs.startsWith(ROOT)) return null;
  const tries = p.endsWith("/") ? [path.join(abs, "index.html")] : [abs, abs + ".html", path.join(abs, "index.html")];
  for (const f of tries) { try { if (fs.statSync(f).isFile()) return { file: f }; } catch {} }
  return null;
}

http.createServer((req, res) => {
  const c = config();
  const p = decodeURIComponent(req.url.split("?")[0]);
  for (const h of c.headers || []) {
    if (new RegExp("^" + h.source.replace("(.*)", ".*") + "$").test(p)) for (const kv of h.headers) res.setHeader(kv.key, kv.value);
  }
  res.setHeader("Cache-Control", "no-cache");
  const red = (c.redirects || []).find(r => r.source === p);
  if (red) { res.writeHead(red.permanent ? 308 : 307, { Location: red.destination }); return res.end(); }
  const r = resolve(p);
  if (r && r.redirect) { res.writeHead(308, { Location: r.redirect }); return res.end(); }
  const file = r ? r.file : path.join(ROOT, "404.html");
  res.writeHead(r ? 200 : 404, { "Content-Type": TYPES[path.extname(file).toLowerCase()] || "application/octet-stream" });
  fs.createReadStream(file).pipe(res);
}).listen(PORT, () => console.log(`Preview: http://localhost:${PORT}`));
