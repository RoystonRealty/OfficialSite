# Royston Realty — website

Static site for https://roystonrealty.in. No build step, no backend, no cost to host.

Files
- index.html — the whole site (HTML, CSS and a little JS in one file)
- assets/ — logo variants, favicons, WhatsApp QR
- CNAME — tells GitHub Pages which domain to serve

Deploy on GitHub Pages (free)
1. Create a public GitHub repository, e.g. `roystonrealty`.
2. Upload every file in this folder to the repository root (keep the assets/ folder).
3. Repository → Settings → Pages → Source: "Deploy from a branch" → Branch: main, folder: / (root) → Save.
4. Same page → Custom domain: roystonrealty.in → Save. Tick "Enforce HTTPS" once the DNS check passes (can take up to an hour).

GoDaddy DNS (My Products → roystonrealty.in → DNS)
- Delete any existing A record for "@" and any "Domain Connect"/parking records.
- Add 4 A records, Name @ , TTL 600:
  185.199.108.153
  185.199.109.153
  185.199.110.153
  185.199.111.153
- Add a CNAME record: Name www → Value <your-github-username>.github.io

Editing later
- Copy, phone, email: edit index.html directly. Every change pushed to main goes live within a minute or two.
- Photos: drop images into assets/ and reference them from index.html.
