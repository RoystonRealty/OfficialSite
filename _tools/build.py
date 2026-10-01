import os, json, html

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://roystonrealty.in"
WA = "https://wa.me/918123125757"
WA_HELLO = WA + "?text=" + "Hello%20Royston%20Realty%2C%20I%27d%20like%20to%20discuss%20a%20property%20requirement."
IG = "https://www.instagram.com/royston.realty/"
EMAIL = "support@roystonrealty.in"
PHONE = "+91 81231 25757"
TEL = "+918123125757"

I_WA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4C2.7 15.6 2.2 13.8 2.2 12 2.2 6.6 6.6 2.2 12 2.2c2.6 0 5.1 1 6.9 2.9 1.8 1.8 2.9 4.3 2.9 6.9 0 5.4-4.4 9.8-9.8 9.8zm8.3-18.1C18.1 1.5 15.1.3 12 .3 5.5.3.3 5.5.3 12c0 2.1.5 4.1 1.6 5.9L.2 23.7l6-1.6c1.7.9 3.7 1.4 5.7 1.4 6.5 0 11.7-5.2 11.7-11.7 0-3.1-1.2-6.1-3.3-8.3z"/></svg>'
I_IG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1" fill="currentColor" stroke="none"/></svg>'
I_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="1.5"/><path d="m4 7 8 6 8-6"/></svg>'
I_CHEV = '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>'
I_MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h18"/></svg>'

SERVICES = [
    dict(slug="sales", name="Sales & Acquisitions",
         short="Buying and selling premium homes and commercial property, from new launches to resale.",
         title="Buy or sell premium property with one advisor who owns the outcome.",
         lead="Buying or selling premium residential and commercial property is a decision measured in crores and years. We bring curated inventory, including new launches and opportunities that never reach the open market, and valuations built from registered transactions rather than asking prices. From the first viewing to the registrar's office, we negotiate and manage the entire transaction for you.",
         includes=["Curated new-launch, resale and off-market opportunities matched to your brief",
                   "Valuation grounded in real, recent transaction data",
                   "Independent due diligence before you commit",
                   "Negotiation, agreements and registration, handled end to end"],
         who="Families buying a first premium home or upgrading, investors placing capital with a long horizon, and owners who want a fair, well-run sale.",
         related=["legal", "interiors", "leasing"]),
    dict(slug="leasing", name="Leasing & Rentals",
         short="Tenants worth having for owners. Homes and offices worth staying in for everyone else.",
         title="Leasing that protects both sides of the agreement.",
         lead="For owners, we find and vet tenants worth having. For companies and families, we find spaces worth staying in. Our leasing practice spans corporate offices, retail and commercial floors, and premium homes, with documentation that protects both sides and renewals handled before they become urgent.",
         includes=["Office, retail and commercial space for companies and founders",
                   "Premium apartments, villas and independent homes",
                   "Tenant verification, background checks and references",
                   "Lease agreements, registration and renewals"],
         who="Owners of premium apartments and villas, companies and founders looking for office or retail space, and families relocating to Bengaluru.",
         related=["management", "legal", "interiors"]),
    dict(slug="land", name="Land",
         short="Title, approvals and boundaries verified before anything changes hands.",
         title="Land, with the groundwork done first.",
         lead="Land carries the highest upside and the highest risk of any asset class. We do the groundwork first: title chain, approvals, encumbrances, zoning and physical boundaries, so that what you acquire is exactly what you believe you are acquiring. For sellers, we position parcels to the right buyers and developers at a fair, defensible value.",
         includes=["Title, approval, encumbrance and boundary verification",
                   "Fair valuation and an honest view of development potential",
                   "Access to landowners, developers and institutional buyers",
                   "Documentation, conversion and registration, handled"],
         who="Buyers acquiring plots or larger parcels, landowners looking to sell or enter a joint development, and developers aggregating land.",
         related=["legal", "civil-works", "sales"]),
    dict(slug="management", name="Property Management",
         short="Your presence on the ground, with every rupee accounted for each month.",
         title="Own property in Bengaluru without managing it yourself.",
         lead="Ownership should not need your attention every week. Whether you live across the city or across the world, we act as your presence on the ground: collecting rent, coordinating tenants, handling maintenance and inspections, and sending you a clear monthly report with every rupee accounted for.",
         includes=["Rent collection, deposits and tenant coordination",
                   "Scheduled inspections and preventive maintenance",
                   "Vendor management with vetted, priced contractors",
                   "Monthly statements and photo-documented reports"],
         who="Non-resident owners, owners who live outside Bengaluru, and anyone who would rather not take tenant calls themselves.",
         related=["leasing", "civil-works", "legal"]),
    dict(slug="civil-works", name="Civil Works",
         short="Construction and renovation held to a written scope and schedule.",
         title="Construction and renovation, verified rather than assumed.",
         lead="Construction and renovation, managed to specification and to schedule. We work with a small bench of contractors we have used before, hold them to written scopes and milestones, and document progress at every stage, so that quality is checked rather than taken on trust.",
         includes=["Structural, civil and renovation work with vetted contractors",
                   "Written scope, milestones and cost control",
                   "Quality checks and progress documentation at each stage",
                   "Approvals, compliance and handover"],
         who="Owners renovating a home before moving in or leasing it out, and companies building out a new floor.",
         related=["interiors", "management", "land"]),
    dict(slug="interiors", name="Interior Design",
         short="Homes and workplaces taken from first concept to handover.",
         title="A finish that matches the property.",
         lead="A premium property deserves a finish that matches it. Our design practice takes homes and offices from concept to completion: space planning, materials, lighting, furniture and fit-out, coordinated with our civil team so the design you approved is the one that gets built.",
         includes=["Concept, space planning and material palettes",
                   "Turnkey execution for homes and workplaces",
                   "Fit-outs coordinated with our civil works team",
                   "Furniture, lighting and styling to handover"],
         who="Families finishing a new home and teams designing a workplace people want to come back to.",
         related=["civil-works", "sales", "leasing"]),
    dict(slug="legal", name="Legal",
         short="Due diligence, agreements and registration, explained in plain language.",
         title="Paperwork you understand before you sign it.",
         lead="Property in India is only as good as its paperwork. Our legal practice handles due diligence, title verification and documentation with care, explaining what each document means and why it matters, in plain language, before you sign anything.",
         includes=["Title search, encumbrance certificates and due diligence",
                   "Sale, lease and development agreements",
                   "Registration, stamp duty and statutory compliance",
                   "Khata, tax and succession-related documentation"],
         who="Anyone signing a sale, lease or development agreement, and owners sorting out khata, tax or succession paperwork.",
         related=["sales", "land", "leasing"]),
]
SV = {s["slug"]: s for s in SERVICES}

NAV = [("services/index.html", "Services", "services"), ("approach.html", "Approach", "approach"),
       ("neighbourhoods.html", "Neighbourhoods", "neighbourhoods"), ("about.html", "About", "about"),
       ("faq.html", "FAQ", "faq"), ("contact.html", "Contact", "contact")]

AUDIENCE = [
    ("Families & individuals", "Buying a first premium home, upgrading to a villa, or placing family wealth in property with a long horizon. You want honest advice and a firm that stays after the keys change hands."),
    ("Non-resident owners", "You own property in Bengaluru but live elsewhere. You need someone on the ground who treats your asset like their own and reports to you with the clarity you'd expect from a bank."),
    ("Companies & founders", "Offices, retail and commercial floors for growing teams. You want a space that works, terms that protect you, and a fit-out delivered on the date you were promised."),
    ("Landowners & developers", "Acquiring, aggregating or exiting land parcels. You need the title work done before the conversation begins, and counterparties who can actually close."),
]
STEPS = [
    ("Understand", "A private conversation about your brief, budget and timeline. We tell you plainly whether we're the right fit."),
    ("Shortlist", "Vetted options with the numbers laid out: comparable transactions, costs, risks and our honest view of each."),
    ("Close", "Negotiation, agreements, due diligence and registration, handled by us and documented at every stage."),
    ("Stay", "We remain your point of contact after completion, for management, works, interiors or the next decision."),
]
FAQS = [
    ("What does “premium only” mean in practice?", "We work on a limited number of high-value residential, commercial and land mandates at a time, so every client gets senior attention. Fit is decided in the first conversation, not by a price threshold on a website. Tell us about your requirement and we'll tell you honestly whether we're the right firm for it."),
    ("How are your fees structured?", "Fees depend on the service and the scope, and every one of them is put in writing before you commit: the amount, when it is payable and what it covers. No fee appears for the first time at closing."),
    ("I live outside India. Can you manage my property?", "Yes. A large part of our management practice is for non-resident owners. We handle tenants, rent, maintenance and inspections, and you receive a monthly statement with photographs and accounts. We can also coordinate with your bank and tax advisor where needed."),
    ("Do you handle registration and legal work yourselves?", "Our legal practice handles due diligence, agreements, registration and compliance as part of the engagement, so you aren't coordinating between a broker, a lawyer and a registrar. Where a specialist opinion is needed, we bring one in and tell you why."),
    ("Can I engage you for just one service?", "Yes. Many clients start with a single need, such as a lease, a valuation or an interior fit-out, and expand from there. Whether it is one service or all seven, you have one advisor accountable for the outcome."),
    ("How quickly do you respond?", "WhatsApp and email are answered the same working day, usually within a few hours. First conversations are private, without obligation, and can be in person, by call or on video."),
]
AREAS = [
    ("Central & South", "Sadashivanagar, Indiranagar, Koramangala, Jayanagar, Richmond Town, Cooke Town, JP Nagar"),
    ("East", "Whitefield, Sarjapur Road, Bellandur, Varthur, Marathahalli, Brookefield"),
    ("North", "Hebbal, Yelahanka, Jakkur, Thanisandra, Devanahalli, the airport corridor"),
]


def e(s): return html.escape(s, quote=True)


def head(p, title, desc, path, extra=""):
    url = DOMAIN + "/" + ("" if path == "index.html" else path.replace("index.html", ""))
    return f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#1F3A33">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Royston Realty">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/lion-gold.png">
<link rel="icon" type="image/png" sizes="32x32" href="{p}assets/favicon-32.png">
<link rel="apple-touch-icon" href="{p}assets/favicon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500&family=Libre+Caslon+Display&family=Libre+Caslon+Text:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/css/site.css">
{extra}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{p}index.html" aria-label="Royston Realty home"><img src="{p}assets/favicon-180.png" alt="" width="38" height="38"><span>Royston Realty</span></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">{I_MENU}</button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul>
{{NAV}}
      </ul>
      <a class="btn btn--primary" href="{WA_HELLO}" target="_blank" rel="noopener">{I_WA}WhatsApp us</a>
    </nav>
  </div>
</header>
<main id="main">
"""


def nav_html(p, active):
    out = []
    for href, label, key in NAV:
        cur = ' aria-current="page"' if key == active else ""
        out.append(f'        <li><a href="{p}{href}"{cur}>{label}</a></li>')
    return "\n".join(out)


def cta(p, heading="Your property deserves judgement, not just a listing.",
        text="Tell us what you're trying to achieve. If we're the right firm for it, we'll say so, and if we're not, we'll tell you that too."):
    return f"""<section class="section section--green cta">
  <div class="wrap">
    <div><h2>{heading}</h2></div>
    <div>
      <p>{text}</p>
      <div class="actions">
        <a class="btn btn--light" href="{WA_HELLO}" target="_blank" rel="noopener">{I_WA}Talk on WhatsApp</a>
        <a class="btn btn--outline-light" href="{p}contact.html">Send an enquiry</a>
      </div>
    </div>
  </div>
</section>
"""


def foot(p):
    svc = "\n".join(f'          <li><a href="{p}services/{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="{p}assets/lion-cream.png" alt="" width="56" height="56">
        <div class="name">Royston Realty</div>
        <p>Premium property advisory in Bengaluru. Sales, leasing, land, management, works, interiors and legal under one accountable team.</p>
        <div class="social">
          <a href="{IG}" target="_blank" rel="noopener" aria-label="Royston Realty on Instagram">{I_IG}</a>
          <a href="{WA_HELLO}" target="_blank" rel="noopener" aria-label="Message Royston Realty on WhatsApp">{I_WA}</a>
          <a href="mailto:{EMAIL}" aria-label="Email Royston Realty">{I_MAIL}</a>
        </div>
      </div>
      <div>
        <h2>Services</h2>
        <ul>
{svc}
        </ul>
      </div>
      <div>
        <h2>Firm</h2>
        <ul>
          <li><a href="{p}about.html">About</a></li>
          <li><a href="{p}approach.html">Approach</a></li>
          <li><a href="{p}neighbourhoods.html">Neighbourhoods</a></li>
          <li><a href="{p}faq.html">FAQ</a></li>
          <li><a href="{p}contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="tel:{TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{IG}" target="_blank" rel="noopener">@royston.realty</a></li>
          <li>Monday to Saturday, 9:30 am to 7:00 pm IST</li>
        </ul>
      </div>
    </div>
    <div class="foot-base">
      <span>© <span id="year">2026</span> Royston Realty. All rights reserved.</span>
      <span>Bengaluru, Karnataka</span>
    </div>
  </div>
</footer>
<a class="wa-float" href="{WA_HELLO}" target="_blank" rel="noopener" aria-label="Message us on WhatsApp">{I_WA}</a>
<script src="{p}assets/js/site.js" defer></script>
</body>
</html>
"""


def page(path, active, title, desc, body, extra=""):
    depth = path.count("/")
    p = "../" * depth
    h = head(p, title, desc, path, extra).replace("{NAV}", nav_html(p, active))
    full = h + body(p) + foot(p)
    fp = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w").write(full)


def page_head(p, crumbs, h1, lead):
    cr = "".join(f'<li><a href="{p}{href}">{lbl}</a></li>' if href else f'<li aria-current="page">{lbl}</li>' for href, lbl in crumbs)
    return f"""<section class="page-head">
  <div class="wrap">
    <ol class="crumbs">{cr}</ol>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>
"""


def svc_rows(p):
    return "\n".join(f'<li><a href="{p}services/{s["slug"]}.html"><h3>{s["name"]}</h3><p>{s["short"]}</p>{I_CHEV}</a></li>' for s in SERVICES)


def steps_html():
    return "\n".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in STEPS)


def audience_html():
    return "\n".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a, b in AUDIENCE)


def insta(p):
    return f"""<div class="wrap"><div class="insta">
  <div class="insta-id">{I_IG}<div><strong>@royston.realty</strong><p>Homes, launches and updates from across Bengaluru.</p></div></div>
  <a class="btn btn--ghost" href="{IG}" target="_blank" rel="noopener">Follow on Instagram</a>
</div></div>
"""


# ---------- Home ----------
LD = {
    "@context": "https://schema.org", "@type": "RealEstateAgent", "name": "Royston Realty",
    "url": DOMAIN + "/", "logo": DOMAIN + "/assets/lion-gold.png", "image": DOMAIN + "/assets/lion-gold.png",
    "telephone": TEL, "email": EMAIL,
    "address": {"@type": "PostalAddress", "addressLocality": "Bengaluru", "addressRegion": "Karnataka", "addressCountry": "IN"},
    "areaServed": "Bengaluru", "sameAs": [IG],
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "09:30", "closes": "19:00"}],
}


def home(p):
    return f"""<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <h1>Property, handled the way it should be.</h1>
      <p class="lead">A premium property advisory in Bengaluru. One accountable team for buying, selling, leasing, land, management, build-outs, interiors and legal, with every fee and every step put in writing before you commit.</p>
      <div class="actions">
        <a class="btn btn--primary" href="{p}contact.html">Start a private conversation</a>
        <a class="btn btn--ghost" href="{p}services/index.html">View services</a>
      </div>
    </div>
    <figure class="hero-seal">
      <img src="{p}assets/lion-cream.png" alt="The Royston Realty winged lion" width="752" height="760">
      <figcaption><span>Premium mandates only</span><span>Bengaluru</span></figcaption>
    </figure>
  </div>
</section>

<section class="section section--stone">
  <div class="wrap split">
    <h2>Most property firms chase volume. We chose the opposite.</h2>
    <div>
      <p class="statement">We take on a deliberately small number of engagements at a time, so the people working on your brief actually know your brief.</p>
      <p class="muted measure">We came to property from software and brought its habits with us: decisions grounded in transaction data, timelines you can see, documentation at every stage, and a strong dislike of surprises.</p>
      <p><a class="textlink" href="{p}about.html">Read about the firm</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <h2>Seven services, one advisor.</h2>
      <p class="lead">Engage us for a single need or the whole life of a property. Either way, you deal with one advisor who owns the outcome.</p>
    </div>
    <ul class="svc-list">
{svc_rows(p)}
    </ul>
  </div>
</section>

<section class="section section--stone">
  <div class="wrap">
    <h2 class="measure">Four steps. No surprises at the table.</h2>
    <ol class="steps">
{steps_html()}
    </ol>
    <p style="margin-top:48px"><a class="textlink" href="{p}approach.html">See how we work and who we work with</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2 class="measure">Built for people who value their time as much as their property.</h2>
    <div class="grid-4">
{audience_html()}
    </div>
  </div>
</section>
{insta(p)}
{cta(p)}"""


page("index.html", "home", "Royston Realty | Premium property advisory in Bengaluru",
     "Royston Realty is a premium property advisory in Bengaluru. Sales, leasing, land, property management, civil works, interiors and legal from one accountable team, with every fee in writing.",
     home, extra=f'<script type="application/ld+json">{json.dumps(LD)}</script>\n')


# ---------- Services index ----------
def services_index(p):
    return page_head(p, [("index.html", "Home"), (None, "Services")],
                     "From the first search to the final signature, and everything after.",
                     "Seven disciplines, one team. Choose a service to see what's included, who it's for and how an engagement runs.") + f"""
<section class="section" style="padding-top:24px">
  <div class="wrap">
    <ul class="svc-list" style="margin-top:0;border-top:0">
{svc_rows(p)}
    </ul>
  </div>
</section>
{cta(p)}"""


page("services/index.html", "services", "Services | Royston Realty",
     "Sales, leasing, land, property management, civil works, interior design and legal services for premium property in Bengaluru.",
     services_index)


# ---------- Service pages ----------
for s in SERVICES:
    def body(p, s=s):
        inc = "\n".join(f"<li>{x}</li>" for x in s["includes"])
        rel = "\n".join(f'<li><a href="{SV[r]["slug"]}.html">{SV[r]["name"]}</a></li>' for r in s["related"])
        q = s["name"].replace("&", "%26")
        return page_head(p, [("index.html", "Home"), ("services/index.html", "Services"), (None, s["name"])],
                         s["title"], s["short"]) + f"""
<section class="section">
  <div class="wrap svc-body">
    <div>
      <section>
        <p class="statement">{s["lead"]}</p>
      </section>
      <section>
        <h2>What's included</h2>
        <ul class="checks">
{inc}
        </ul>
      </section>
      <section>
        <h2>Who it's for</h2>
        <p class="muted measure">{s["who"]}</p>
      </section>
      <section>
        <h2>How an engagement runs</h2>
        <ol class="steps" style="grid-template-columns:repeat(2,1fr);gap:40px 0;margin-top:32px">
{steps_html()}
        </ol>
      </section>
    </div>
    <aside>
      <div class="aside-card">
        <h3>Discuss {s["name"].lower()}</h3>
        <p>A private first conversation, without obligation. Fees and scope are agreed in writing before any work begins.</p>
        <a class="btn btn--primary" href="../contact.html?service={q}">Send an enquiry</a>
        <a class="btn btn--ghost" href="{WA_HELLO}" target="_blank" rel="noopener" style="margin-top:10px">{I_WA}WhatsApp us</a>
        <hr>
        <p style="margin-bottom:6px;color:var(--ink);font-weight:500">Often paired with</p>
        <ul>
{rel}
        </ul>
      </div>
    </aside>
  </div>
</section>
{cta(p)}"""
    page(f"services/{s['slug']}.html", "services", f"{s['name']} in Bengaluru | Royston Realty",
         f"{s['short']} {s['name']} by Royston Realty, a premium property advisory in Bengaluru.", body)


# ---------- About ----------
def about(p):
    commits = [("Premium only", "We take on select, high-value engagements and nothing else. A smaller portfolio means we know every asset we represent first-hand."),
               ("Built by technologists", "Our team comes from software. Expect clean data, clear timelines and decisions backed by numbers rather than noise."),
               ("Trust, in writing", "Every fee, every step and every document is disclosed before you commit."),
               ("Discretion, always", "Your holdings, requirements and conversations stay confidential. We introduce parties only when both sides have agreed.")]
    donts = ["Flood you with listings that don't match your brief",
             "Quote a fee, then discover another one at closing",
             "Share your details with a counterparty before you've agreed",
             "Promise a timeline we can't document",
             "Take on a mandate we don't have the time to do properly"]
    c = "\n".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a, b in commits)
    d = "\n".join(f"<li>{x}</li>" for x in donts)
    return page_head(p, [("index.html", "Home"), (None, "About")],
                     "Fewer clients. Sharper judgement. Clearer answers.",
                     "Royston Realty is a premium-only property advisory in Bengaluru, run less like a brokerage and more like a family office for your property.") + f"""
<section class="section">
  <div class="wrap split">
    <h2>Why we work this way</h2>
    <div>
      <p class="statement">We take on a deliberately small number of engagements at a time, so that the people working on your brief actually know your brief.</p>
      <p class="muted">We came to property from software, and brought its habits with us: decisions grounded in real transaction data, timelines you can see, documentation at every stage, and a strong dislike of surprises. Where much of the industry runs on phone calls and hearsay, we run on evidence.</p>
      <p class="muted">The result is a firm that advises on what to buy, sell or lease, then stays to manage, build, finish and protect it long after the paperwork is done.</p>
      <ul class="figures">
        <li><strong>7</strong><span>services under one roof</span></li>
        <li><strong>1</strong><span>advisor accountable to you</span></li>
        <li><strong>0</strong><span>undisclosed fees, ever</span></li>
      </ul>
      <blockquote class="pull">Every brief gets our full attention, or we don't take it on.</blockquote>
    </div>
  </div>
</section>
<section class="section section--stone">
  <div class="wrap">
    <h2 class="measure">The commitments we make on every engagement.</h2>
    <div class="grid-2">
{c}
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <h2>What we deliberately don't do</h2>
    <ul class="checks crosses">
{d}
    </ul>
  </div>
</section>
{insta(p)}
{cta(p)}"""


page("about.html", "about", "About | Royston Realty", "Royston Realty is a premium-only property advisory in Bengaluru with a small number of engagements, data-led decisions and every fee in writing.", about)


# ---------- Approach ----------
def approach(p):
    return page_head(p, [("index.html", "Home"), (None, "Approach")],
                     "Four steps. No surprises at the table.",
                     "How an engagement runs from the first conversation to long after completion, and the people we're built to serve.") + f"""
<section class="section">
  <div class="wrap">
    <h2 class="measure">How we work</h2>
    <ol class="steps">
{steps_html()}
    </ol>
  </div>
</section>
<section class="section section--stone">
  <div class="wrap">
    <h2 class="measure">Who we serve</h2>
    <div class="grid-2">
{audience_html()}
    </div>
  </div>
</section>
{cta(p)}"""


page("approach.html", "approach", "Our approach | Royston Realty", "How Royston Realty works: understand, shortlist, close, stay. Built for families, non-resident owners, companies and landowners in Bengaluru.", approach)


# ---------- Neighbourhoods ----------
def hoods(p):
    a = "\n".join(f"<li><h3>{x}</h3><p>{y}</p></li>" for x, y in AREAS)
    return page_head(p, [("index.html", "Home"), (None, "Neighbourhoods")],
                     "Bengaluru, known street by street.",
                     "These are the micro-markets we transact in most and know best. We also take on select mandates elsewhere in Bengaluru and across Karnataka when the brief calls for it.") + f"""
<section class="section" style="padding-top:24px">
  <div class="wrap">
    <ul class="areas" style="margin-top:0;border-top:0">
{a}
    </ul>
    <p class="muted measure" style="margin-top:40px">Looking somewhere not listed here? <a class="textlink" href="{p}contact.html">Tell us the area</a> and we'll say plainly whether we know it well enough to help.</p>
  </div>
</section>
{cta(p)}"""


page("neighbourhoods.html", "neighbourhoods", "Neighbourhoods we cover | Royston Realty", "Royston Realty works across Central, South, East and North Bengaluru: Indiranagar, Koramangala, Whitefield, Sarjapur Road, Hebbal, Devanahalli and more.", hoods)


# ---------- FAQ ----------
FAQ_LD = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}


def faq(p):
    f = "\n".join(f'<details><summary>{q}</summary><div class="answer"><p>{a}</p></div></details>' for q, a in FAQS)
    return page_head(p, [("index.html", "Home"), (None, "FAQ")],
                     "Before we talk.",
                     "The things people usually want to know before the first conversation. Anything else, ask us directly.") + f"""
<section class="section" style="padding-top:24px">
  <div class="wrap">
    <div class="faq measure" style="max-width:56rem;border-top:0">
{f}
    </div>
  </div>
</section>
{cta(p)}"""


page("faq.html", "faq", "Frequently asked questions | Royston Realty", "Fees, non-resident property management, legal work and response times: answers to common questions about Royston Realty.", faq,
     extra=f'<script type="application/ld+json">{json.dumps(FAQ_LD)}</script>\n')


# ---------- Contact ----------
def contact(p):
    opts = "".join(f'<option value="{e(s["name"])}">{s["name"]}</option>' for s in SERVICES) + '<option value="Not sure yet">Not sure yet</option>'
    roles = ["Looking to buy", "Looking to sell", "Looking to rent a home", "Looking to rent an office or commercial space",
             "An owner wanting to lease my property", "An owner needing property management", "Planning construction or interiors", "Something else"]
    ro = "".join(f'<option value="{e(r)}">{r}</option>' for r in roles)
    return page_head(p, [("index.html", "Home"), (None, "Contact")],
                     "Let's talk about your next space.",
                     "Every first conversation is private and without obligation, in person, by call or on video.") + f"""
<section class="section">
  <div class="wrap contact-grid">
    <div>
      <ul class="channels">
        <li><span class="k">Phone</span><a href="tel:{TEL}">{PHONE}</a></li>
        <li><span class="k">WhatsApp</span><a href="{WA_HELLO}" target="_blank" rel="noopener">Message us</a></li>
        <li><span class="k">Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><span class="k">Instagram</span><a href="{IG}" target="_blank" rel="noopener">@royston.realty</a></li>
        <li><span class="k">Hours</span><span>Monday to Saturday, 9:30 am to 7:00 pm IST. Meetings by appointment, at a location of your choosing.</span></li>
      </ul>
      <div class="qr">
        <img src="{p}assets/whatsapp-qr.png" alt="QR code that opens a WhatsApp chat with Royston Realty" width="112" height="112">
        <p>On a computer? Scan this with your phone to open a WhatsApp chat with us.</p>
      </div>
    </div>
    <div class="form-card">
      <h2>Tell us about your requirement</h2>
      <p>This opens WhatsApp with your details filled in. Nothing is stored on this website.</p>
      <form id="enquiry" novalidate>
        <div class="field-row">
          <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required></div>
          <div class="field"><label for="f-phone">Phone (optional)</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
        </div>
        <div class="field"><label for="f-service">Service</label><select id="f-service" name="service">{opts}</select></div>
        <div class="field"><label for="f-role">I am</label><select id="f-role" name="role">{ro}</select></div>
        <div class="field"><label for="f-brief">Your requirement</label><textarea id="f-brief" name="brief" placeholder="Area, budget, size and timeline, whatever you know so far"></textarea></div>
        <p class="form-error" role="alert" aria-live="polite"></p>
        <button class="btn btn--primary" type="submit">{I_WA}Send on WhatsApp</button>
        <p class="form-note">Prefer email? Write to <a class="textlink" href="mailto:{EMAIL}">{EMAIL}</a></p>
      </form>
    </div>
  </div>
</section>
{insta(p)}"""


page("contact.html", "contact", "Contact | Royston Realty", "Talk to Royston Realty on WhatsApp, phone, email or Instagram. Premium property advisory in Bengaluru.", contact)


# ---------- 404 (absolute paths: GitHub serves it at any depth) ----------
def nf(p):
    return f"""<section class="section not-found"><div class="wrap">
  <h1 style="margin-bottom:24px">This page isn't here.</h1>
  <p class="lead">The link may be old, or the address mistyped. Everything is still a click away.</p>
  <div class="actions"><a class="btn btn--primary" href="/">Go to the home page</a><a class="btn btn--ghost" href="/services/">View services</a></div>
</div></section>
"""


h = head("/", "Page not found | Royston Realty", "This page could not be found.", "404.html", '<meta name="robots" content="noindex">\n').replace("{NAV}", nav_html("/", ""))
open(os.path.join(OUT, "404.html"), "w").write(h + nf("/") + foot("/"))

# ---------- sitemap / robots ----------
pages = ["", "services/", *[f"services/{s['slug']}.html" for s in SERVICES], "about.html", "approach.html", "neighbourhoods.html", "faq.html", "contact.html"]
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in pages:
    sm.append(f"  <url><loc>{DOMAIN}/{u}</loc><lastmod>2026-10-01</lastmod><priority>{'1.0' if u == '' else '0.8'}</priority></url>")
sm.append("</urlset>")
open(os.path.join(OUT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
print("built", len(pages) + 1, "pages")
