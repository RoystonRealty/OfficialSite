# Royston Realty — website

Static multi-page site for https://roystonrealty.in, hosted free on GitHub Pages. No backend, no paid hosting.

## Pages
- `index.html` — Home
- `services/index.html` — All services, plus one page per service (sales, leasing, land, management, civil-works, interiors, legal)
- `listings.html` — current properties, filled from `assets/data/listings.js`
- `neighbourhoods.html` — coverage map and micro-market profiles
- `guides/` — four client guides (renting out, resale documents, new launches, NRI owners)
- `about.html`, `approach.html`, `faq.html`, `contact.html`
- `404.html` — shown by GitHub Pages for any missing address

## Updating your existing GitHub Pages site
1. Open your existing repository on GitHub.
2. Delete the old `index.html` and old `sitemap.xml` (keep `CNAME`).
3. Upload everything in this folder to the repository root, keeping the folder structure (`assets/`, `services/`, `_tools/`). The easiest way: "Add file → Upload files" and drag the whole unzipped folder contents in.
4. Commit to `main`. The new site is live within a minute or two. Your domain and DNS settings stay as they are.

## Editing content
Every page is plain HTML you can edit directly. The header and footer are repeated on every page, so for site-wide changes (phone number, email, Instagram, a new service) it's easier to edit `_tools/build.py` and run:

    python3 _tools/build.py

That regenerates all pages. The `_tools` folder is not published by GitHub Pages.
Colours and fonts live in `assets/css/site.css` (the `:root` block at the top).

## Adding a listing (no coding needed)
1. Upload the photo to `assets/listings/` on GitHub (landscape, under ~300 KB).
2. Open `assets/data/listings.js`, click the pencil icon, copy the example block, fill it in.
3. Commit. The listing appears on the Listings page and in "Available now" on the home page.
Remove a listing by deleting its block. With no listings, the site shows a "share your brief" message.

## Editing guides and neighbourhoods
The text lives in `_tools/content.py`. Edit it, then run `python3 _tools/build.py`.

## Adding photos later
Put images in `assets/` (compress them to under ~300 KB each) and reference them from the HTML. Good first candidates: a property photo inside the green panel on the home page, and one image at the top of each service page.
