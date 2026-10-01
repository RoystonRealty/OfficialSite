# Content for neighbourhoods and guides. Edit text here, then run build.py.

# (name, x km east of MG Road, y km north of MG Road, one-line profile)
ZONES = [
    ("Central & South", "c", [
        ("Sadashivanagar", -3.0, 4.2, "One of the city's oldest and quietest addresses: large plots, bungalows and established families near Sankey Tank."),
        ("Richmond Town", 0.0, -1.4, "Leafy, central lanes a few minutes from MG Road and the business district."),
        ("Cooke Town", 2.6, 2.6, "Quiet streets of older bungalows and low-rise homes beside Frazer Town."),
        ("Indiranagar", 4.2, 0.4, "100 Feet Road and 12th Main, on the metro, with independent houses and boutique low-rise apartments."),
        ("Koramangala", 2.2, -4.2, "The startup district, with a mix of apartments, independent homes and offices across its blocks."),
        ("Jayanagar", -1.6, -6.0, "Planned, tree-lined and settled. A long-standing choice for families who want to stay put."),
        ("JP Nagar", -1.0, -9.0, "Residential and well connected, close to Bannerghatta Road and the metro."),
    ]),
    ("East", "e", [
        ("Marathahalli", 9.0, -0.8, "The Outer Ring Road junction, with steady rental demand from nearby tech parks."),
        ("Brookefield", 12.0, 0.6, "Apartments close to ITPL, popular with working professionals."),
        ("Whitefield", 15.0, 1.4, "Tech parks, international schools and gated communities, now on the metro."),
        ("Varthur", 14.0, -4.2, "A newer belt of villa communities and larger homes."),
        ("Bellandur", 8.2, -6.2, "Apartments along the Outer Ring Road tech corridor."),
        ("Sarjapur Road", 10.5, -9.2, "Gated communities, villas and schools, with strong demand from families."),
    ]),
    ("North", "n", [
        ("Hebbal", 0.2, 9.0, "The lakefront gateway to the airport road, close to Manyata Tech Park."),
        ("Thanisandra", 4.4, 10.2, "Newer apartment projects a short drive from Manyata."),
        ("Jakkur", 1.6, 13.0, "Lake views, the aerodrome and a growing number of villa projects."),
        ("Yelahanka", -1.2, 16.8, "Spacious and calmer, with independent homes and planned layouts."),
    ]),
]
DEVANAHALLI = "Devanahalli and the airport corridor: plotted developments, land and long-horizon investments."

ROUTER = [
    ("Rent a home", "Premium apartments, villas and independent homes, shortlisted to your brief.", "services/leasing.html"),
    ("Lease out my property", "Tenants verified, agreement registered, rent handled.", "services/leasing.html"),
    ("Buy a home", "New launches and resale, valued from registered transactions.", "services/sales.html"),
    ("Sell a property", "Priced from real data, marketed discreetly, closed end to end.", "services/sales.html"),
    ("Manage it from abroad", "Rent, tenants, repairs and a monthly statement with photos.", "services/management.html"),
    ("Find office space", "Offices, retail and commercial floors on terms that protect you.", "services/leasing.html"),
]

GUIDES = [
    dict(slug="renting-out-your-home", audience="For owners",
         title="Renting out your home in Bengaluru: an owner's checklist",
         summary="How to prepare, price, choose a tenant and write an agreement that protects you.",
         sections=[
             ("Prepare the home before you list it", [
                 "Tenants for premium homes compare carefully, and the first visit decides most of it. Repaint where needed, deep clean, fix every tap and switch, and service the appliances you are leaving behind.",
                 "Take good photographs in daylight, with lights on and curtains open. Listings with clear photos get more serious enquiries and fewer wasted visits.",
             ]),
             ("Price from what actually rented", [
                 "Asking rents on portals are often well above what homes in the same tower actually rent for. Look at recent closed rents for similar size, floor and furnishing in your project, and price close to them. A home that rents in two weeks usually earns more over the year than one that sits empty for two months at a higher ask.",
             ]),
             ("Choose the tenant, not just the offer", [
                 "Verify identity documents, current employer and, where possible, a reference from the previous landlord. Meet the people who will live in the home.",
                 "Bengaluru City Police asks owners to complete tenant verification. It takes little time and gives you a record if anything goes wrong later.",
             ]),
             ("Put everything in the agreement", [
                 "Most residential leases in Bengaluru run for 11 months. Leases of a year or longer must be registered, and stamp duty applies to rental agreements either way, so pay it rather than skipping it.",
                 "Write down the rent, deposit, lock-in period, notice period, annual increase, who pays maintenance, and what will be deducted from the deposit at exit (painting and cleaning are common). Vague clauses are where most disputes start.",
             ]),
             ("Hand over properly", [
                 "Make an inventory of furniture, fittings and appliances with photographs, and note the electricity and water meter readings on the day of handover. Both sides sign it. This one page settles most deposit arguments before they begin.",
             ]),
         ],
         service="leasing"),
    dict(slug="buying-resale-documents", audience="For buyers",
         title="Buying a resale flat in Bengaluru: the documents to check",
         summary="Title, khata, EC, occupancy certificate and the other papers that decide whether a resale is safe.",
         sections=[
             ("Why resale needs more checking", [
                 "A resale home has a history: previous owners, loans, society dues and sometimes approvals that were never completed. The price can be right and the home can be beautiful, and the paperwork can still make it a bad purchase. Check before you pay any token amount.",
             ]),
             ("The title chain", [
                 "Ask for the current sale deed and the earlier deeds that show how the property passed from owner to owner, ideally going back several decades for the land. Every link should be unbroken, and every owner should have had the right to sell.",
                 "If the seller is acting through a power of attorney, confirm the document is registered, still valid and actually covers a sale.",
             ]),
             ("Encumbrance certificate", [
                 "The encumbrance certificate (EC) from the sub-registrar's office shows registered transactions on the property, including mortgages. In Karnataka it can be requested online through the Kaveri portal. It should match the title chain and show no loan or claim you haven't been told about.",
             ]),
             ("Khata and property tax", [
                 "The khata records the property in the city's books and is needed for tax, utilities and future sale. An A khata means the property is fully compliant; a B khata usually points to an approval gap. Bengaluru has been moving properties to e-khata, so ask for the current record and check the details match the deed.",
                 "Ask for recent property tax receipts to confirm nothing is outstanding.",
             ]),
             ("Approvals and completion", [
                 "Check the sanctioned building plan, and make sure the building has an occupancy certificate (OC). Without an OC, you may face trouble with utility connections, loans and resale later.",
             ]),
             ("Loans, society dues and the final value", [
                 "If the seller still has a home loan, the bank must be paid and must release the original documents before or at registration. Ask the society or association for a no-dues letter covering maintenance.",
                 "Finally, compare the price against recent registered sales in the same project, not against other asking prices. Registration happens at the sub-registrar's office, with stamp duty and registration charges set by the state, so confirm the current rates when you plan your budget.",
             ]),
         ],
         service="sales"),
    dict(slug="new-launch-checklist", audience="For buyers",
         title="Buying at a new launch: what to verify before you book",
         summary="RERA registration, builder track record, the agreement for sale and the costs that aren't on the brochure.",
         sections=[
             ("Start with RERA", [
                 "Every residential project of meaningful size must be registered with Karnataka RERA before it is marketed. Look the project up on the Karnataka RERA website and read what the builder has declared: the registration number, approvals, the promised completion date and the phases covered. If it isn't registered, don't book.",
                 "Under RERA, a builder can't take more than 10% of the price as an advance before an agreement for sale is registered, and carpet area is the area you are sold. Both protect you, so use them.",
             ]),
             ("Look at what the builder has already delivered", [
                 "A brochure shows intent. A finished project shows ability. Visit one or two of the builder's completed projects, ask residents about delivery delays, construction quality and how the association handover went.",
             ]),
             ("Read the agreement for sale", [
                 "Check the payment plan (construction-linked plans tie payments to visible progress), the completion date, the penalty if possession is late, the specifications, and exactly which car park and common areas you are getting.",
             ]),
             ("Count the full cost", [
                 "The headline price is rarely the final one. Ask for a written cost sheet that includes car parking, club membership, maintenance deposits, legal and documentation charges, stamp duty and registration, and GST, which applies to homes bought under construction but not to completed ones with an occupancy certificate.",
             ]),
             ("Launch pricing and timing", [
                 "Early bookings are often priced lower, and that discount is real. So is the risk of a long wait. Weigh the saving against the rent you will keep paying until possession, and against the builder's record on dates.",
             ]),
         ],
         service="sales"),
    dict(slug="nri-owners-guide", audience="For owners abroad",
         title="Owning in Bengaluru, living abroad: a guide for NRI owners",
         summary="Rent, tax deducted at source, power of attorney, upkeep and what to plan for when you sell.",
         sections=[
             ("Renting while you are away", [
                 "Most of the work of a rental happens on the ground: showing the home, checking tenants, handing over keys, fixing a leak at short notice. Decide early who will do it, whether that's family, a friend or a manager, and put that arrangement in writing.",
             ]),
             ("Rent and tax deducted at source", [
                 "When a tenant pays rent to a non-resident owner, the tenant is required to deduct tax at source before paying and deposit it with the government. Many tenants don't know this, so explain it at the start and build it into the agreement. Rent is usually received into an NRO account, and you can claim credit for the tax deducted when you file your return. Ask your chartered accountant about the details for your situation.",
             ]),
             ("Power of attorney", [
                 "A specific power of attorney lets someone in India sign on your behalf for a defined purpose, such as a lease or a sale. If you sign it abroad, it usually needs to be attested at an Indian embassy or consulate, or apostilled, and then stamped once it arrives in India. Keep its scope narrow and specific.",
             ]),
             ("Keep the property in good order", [
                 "Pay property tax and association maintenance on time, both can be done online, and keep receipts. Arrange an inspection at least once or twice a year, with photographs, so small problems don't become expensive ones.",
             ]),
             ("When you sell", [
                 "Sale proceeds can be repatriated within limits set by the Reserve Bank of India, and the paperwork includes certification from a chartered accountant. Capital gains tax applies, and the buyer must deduct tax at source when paying a non-resident seller. Plan this with your accountant months before you list the home, not after you find a buyer.",
             ]),
         ],
         service="management"),
]
