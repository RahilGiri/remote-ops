import os
import glob

# Re-usable header/footer extracted from an existing service page
def get_shell(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    parts = content.split('<main>')
    head = parts[0]
    tail = parts[1].split('</main>')[1]
    return head, tail

try:
    head, tail = get_shell('services/crm-gohighlevel.html')
except Exception:
    head, tail = "", ""

# Data for 14 pages
pages_data = {
    "services/crm-gohighlevel.html": {
        "cat": "Operations Service", "title": "CRM & GoHighLevel", "sub": "We manage, clean, and automate your GoHighLevel and CRM workflows so you can focus on closing deals.",
        "img1": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1600&auto=format&fit=crop",
        "img2": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=800&auto=format&fit=crop",
        "s1_title": "End to End CRM Management",
        "s1_text": "A messy CRM means lost revenue. Our dedicated real estate virtual assistants are highly trained in GoHighLevel, Salesforce, Hubspot, and Follow Up Boss. We ensure every lead is tracked, tagged, and followed up with systematically.",
        "features1": ["Database Cleanup & Deduplication", "Pipeline Building & Management", "Contact Tagging & Segmentation"],
        "features2": ["Automated Follow Up Workflows", "Form & Funnel Integration", "Weekly Analytics Reporting"],
        "s2_title": "Stop Letting Deals Slip Through the Cracks.",
        "s2_t1": "Real estate professionals spend up to 30% of their week just doing data entry and trying to figure out who they need to call next.",
        "s2_t2": "By handing off your CRM management to RemoteOps, you get a pristine database, automated lead nurturing, and a clear daily dashboard of who is ready to buy or sell."
    },
    "services/lead-generation.html": {
        "cat": "Growth Service", "title": "Lead Generation", "sub": "Data driven prospect research and list building to fill your pipeline with highly qualified real estate opportunities.",
        "img1": "https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=1600&auto=format&fit=crop",
        "img2": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=800&auto=format&fit=crop",
        "s1_title": "Targeted Lead Research",
        "s1_text": "Finding the right deals and investors requires hours of tedious research. We take over the heavy lifting of identifying, verifying, and organizing contact information for property owners, fund managers, and potential buyers.",
        "features1": ["Commercial Real Estate Prospecting", "Off Market Property Owner Lookup", "LinkedIn Sales Navigator Research"],
        "features2": ["Data Scraping & Verification", "List Scrubbing & Formatting", "Direct Import to your CRM"],
        "s2_title": "Fuel Your Outreach with Accurate Data.",
        "s2_t1": "There is nothing worse than wasting hours cold calling wrong numbers or emailing bounced addresses.",
        "s2_t2": "Our VAs are experts at using premium tools to verify contact information so your sales team can spend 100% of their time talking to actual decision makers."
    },
    "services/investor-outreach.html": {
        "cat": "Growth Service", "title": "Investor Outreach", "sub": "Consistent, professional outreach and follow up management to keep your capital raising calendar booked.",
        "img1": "https://images.unsplash.com/photo-1557804506-669a67965ba0?q=80&w=1600&auto=format&fit=crop",
        "img2": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=800&auto=format&fit=crop",
        "s1_title": "Systematic Capital Raising Support",
        "s1_text": "Raising capital requires extreme consistency. We act as an extension of your investor relations team, handling the initial touchpoints, scheduling meetings, and ensuring no potential LP is ever forgotten.",
        "features1": ["Cold Email Campaign Management", "LinkedIn Direct Messaging", "Meeting Scheduling & Calendar Ops"],
        "features2": ["Investor Follow up Tracking", "Pitch Deck Distribution", "Investor Update Formatting"],
        "s2_title": "Build Relationships. We'll Handle the Logistics.",
        "s2_t1": "You need to be on the phone and in the room pitching your fund or syndication. You shouldn't be formatting mail merges.",
        "s2_t2": "RemoteOps ensures your outreach engine never stops running, even when you are traveling, touring properties, or closing deals."
    },
    "services/email-marketing.html": {
        "cat": "Marketing Service", "title": "Email Marketing", "sub": "Design, schedule, and send professional email campaigns, newsletters, and property blasts.",
        "img1": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1600&auto=format&fit=crop",
        "img2": "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?q=80&w=800&auto=format&fit=crop",
        "s1_title": "Professional Campaign Management",
        "s1_text": "Keep your buyers, sellers, and investors engaged with high quality email marketing. Our team handles the design, copy formatting, list segmentation, and deployment of your critical communications.",
        "features1": ["Monthly Newsletter Formatting", "New Listing Email Blasts", "Investor Update Deployment"],
        "features2": ["List Segmentation & Hygiene", "A/B Testing Subject Lines", "Open & Click Rate Reporting"],
        "s2_title": "Stay Top of Mind Automatically.",
        "s2_t1": "Your email list is your most valuable asset, but only if you use it consistently. We make sure your communications go out on time, every time.",
        "s2_t2": "Whether it is a Mailchimp blast to 10,000 brokers or a highly targeted GoHighLevel drip campaign to 50 LPs, we handle the execution."
    },
    "services/social-media.html": {
        "cat": "Marketing Service", "title": "Social Media Management", "sub": "Maintain a dominant brand presence on LinkedIn, Instagram, and Facebook without lifting a finger.",
        "img1": "https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=1600&auto=format&fit=crop",
        "img2": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=800&auto=format&fit=crop",
        "s1_title": "Consistent Multi Platform Presence",
        "s1_text": "In modern real estate, if you aren't posting, you don't exist. We manage your content calendar, design professional graphics in Canva, and schedule posts across all your major social channels.",
        "features1": ["Content Calendar Creation", "Canva Graphic Design", "Post Scheduling (Hootsuite/Buffer)"],
        "features2": ["Just Listed/Just Sold Graphics", "LinkedIn Thought Leadership", "Community Engagement & Replies"],
        "s2_title": "Build Authority While You Sleep.",
        "s2_t1": "Creating social media content is incredibly time consuming. Our trained VAs take your raw ideas, property photos, and deal announcements and turn them into polished posts.",
        "s2_t2": "We ensure your firm looks active, successful, and professional to anyone researching you online."
    },
    "services/real-estate-marketing.html": {
        "cat": "Marketing Service", "title": "Real Estate Marketing", "sub": "Specialized marketing support for property listings, offering memorandums, and broker deliverables.",
        "img1": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?q=80&w=1600&auto=format&fit=crop",
        "img2": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=800&auto=format&fit=crop",
        "s1_title": "Premium Property Marketing",
        "s1_text": "Speed to market is everything. When you win a listing or acquire a property, our team acts fast to build flyers, setup the single property website, and distribute the marketing materials.",
        "features1": ["Offering Memorandum (OM) Formatting", "Property Flyer & Brochure Design", "Single Property Website Updates"],
        "features2": ["LoopNet & CoStar Listing Entry", "Virtual Tour Uploads", "Marketing Package Assembly"],
        "s2_title": "Impress Clients with Speed and Quality.",
        "s2_t1": "Don't let administrative bottlenecks delay your listings from going live. We provide the rapid marketing support brokers and investors need.",
        "s2_t2": "Hand us the property photos and the basic stats, and we will deliver a comprehensive, branded marketing package ready for distribution."
    },
    "services/operations-support.html": {
        "cat": "Operations Service", "title": "Operations Support", "sub": "Administrative and back office support to keep your firm running smoothly and efficiently.",
        "img1": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=1600&auto=format&fit=crop",
        "img2": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?q=80&w=800&auto=format&fit=crop",
        "s1_title": "Reliable Back Office Execution",
        "s1_text": "Every real estate firm has unique operational tasks that don't fit neatly into a box. From document formatting to inbox management, our VAs handle the critical day to day operations.",
        "features1": ["Inbox & Calendar Management", "Document Formatting & Filing", "Data Entry & Spreadsheet Management"],
        "features2": ["Expense Tracking & Receipt Logging", "Vendor Coordination", "Ad Hoc Administrative Tasks"],
        "s2_title": "Get Your Time Back.",
        "s2_t1": "The most successful real estate professionals delegate ruthlessly. If a task doesn't directly generate revenue, you shouldn't be doing it.",
        "s2_t2": "Our operations support gives you leverage. We handle the paperwork and the inbox so you can handle the negotiations and the strategy."
    },
    "services/digital-support.html": {
        "cat": "Operations Service", "title": "Digital Support", "sub": "Website updates, basic tech support, and software integration for modern real estate teams.",
        "img1": "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?q=80&w=1600&auto=format&fit=crop",
        "img2": "https://images.unsplash.com/photo-1551434678-e076c223a692?q=80&w=800&auto=format&fit=crop",
        "s1_title": "Seamless Technology Management",
        "s1_text": "Keep your digital presence up to date without calling an expensive developer. Our team can manage your WordPress or Wix site, update team bios, and connect your software tools.",
        "features1": ["Basic Website Updates (WordPress/Wix)", "Team Bio & Roster Management", "Zapier Automation Setup"],
        "features2": ["Software Tool Onboarding", "Digital File Organization", "Dashboard Creation"],
        "s2_title": "Your Tech Stack, Optimized.",
        "s2_t1": "Real estate teams use more software than ever before. But software is only useful if it is properly maintained.",
        "s2_t2": "We help you connect the dots between your CRM, your website, and your lead sources using tools like Zapier, ensuring data flows seamlessly."
    },
    
    # Industries
    "industries/fund-managers.html": {
        "cat": "Industry Expertise", "title": "Fund Managers", "sub": "Specialized operational support for private equity, debt funds, and syndicators.",
        "img1": "https://images.unsplash.com/photo-1579532537598-459ecdaf39cc?q=80&w=1600&auto=format&fit=crop",
        "img2": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800&auto=format&fit=crop",
        "s1_title": "Scale Your AUM Without Scaling Overhead",
        "s1_text": "Fund managers need to focus on acquisitions and LP relations. We handle the CRM updates, the pitch deck formatting, and the routine investor communications.",
        "features1": ["LP Database Management", "Capital Call Communication Formatting", "Pitch Deck Design (Canva/PPT)"],
        "features2": ["Target Acquisition Research", "Investor Portal Updates", "Weekly Reporting Dashboards"],
        "s2_title": "Institutional Grade Support.",
        "s2_t1": "We understand the terminology and the stakes involved in managing outside capital.",
        "s2_t2": "Our VAs provide the meticulous attention to detail required to keep your investor data secure, organized, and perfectly formatted."
    },
    "industries/real-estate-investment.html": {
        "cat": "Industry Expertise", "title": "Real Estate Investment", "sub": "Support for flippers, wholesalers, and buy and hold investment firms.",
        "img1": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?q=80&w=1600&auto=format&fit=crop",
        "img2": "https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=800&auto=format&fit=crop",
        "s1_title": "Keep Your Deal Funnel Full",
        "s1_text": "Finding off market deals is a numbers game. We provide the research, data scraping, and initial outreach required to keep your acquisitions team busy.",
        "features1": ["Skip Tracing & Data Entry", "Motivated Seller List Building", "Cold Email Outreach Campaigns"],
        "features2": ["CRM Pipeline Management", "Comps Research Preparation", "Contract Formatting"],
        "s2_title": "Outsource the Grind.",
        "s2_t1": "Pulling lists, skip tracing, and sending direct mail is exhausting and keeps you away from underwriting deals.",
        "s2_t2": "Let our trained virtual assistants handle the top of the funnel so you can focus on negotiating the contracts."
    },
    "industries/commercial-real-estate.html": {
        "cat": "Industry Expertise", "title": "Commercial Real Estate", "sub": "Marketing and operational leverage for CRE brokers and agencies.",
        "img1": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1600&auto=format&fit=crop",
        "img2": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=800&auto=format&fit=crop",
        "s1_title": "Win More Listings. Close Faster.",
        "s1_text": "Commercial brokers need speed and professionalism. We build your Offering Memorandums (OMs), update CoStar/LoopNet, and research potential buyers.",
        "features1": ["OM and Flyer Design", "CoStar & LoopNet Updates", "Buyer & Tenant Prospecting"],
        "features2": ["CRM Maintenance", "Email Blast Execution", "Market Report Formatting"],
        "s2_title": "Your Dedicated Back Office.",
        "s2_t1": "Top producing CRE brokers don't build their own brochures. They have a team behind them.",
        "s2_t2": "RemoteOps provides you with a dedicated virtual marketing and operations assistant for a fraction of the cost of a full time in house hire."
    },
    "industries/leasing.html": {
        "cat": "Industry Expertise", "title": "Leasing", "sub": "Support for commercial and residential leasing teams.",
        "img1": "https://images.unsplash.com/photo-1554469384-e58fac16e23a?q=80&w=1600&auto=format&fit=crop",
        "img2": "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?q=80&w=800&auto=format&fit=crop",
        "s1_title": "Keep Occupancy High",
        "s1_text": "Managing a high volume of leasing inquiries requires extreme organization. We monitor your inbox, pre qualify leads, and manage your showing calendar.",
        "features1": ["Inbound Inquiry Response", "Tenant Pre Qualification", "Calendar & Showing Scheduling"],
        "features2": ["Listing Syndication Updates", "Lease Agreement Formatting", "Follow Up Drip Campaigns"],
        "s2_title": "Never Miss a Lead.",
        "s2_t1": "When a prospective tenant reaches out, they expect an immediate response. If you don't reply, the next building will.",
        "s2_t2": "We ensure every single Zillow, Apartments.com, or direct inquiry is entered into your CRM and immediately followed up with."
    },
    "industries/property-management.html": {
        "cat": "Industry Expertise", "title": "Property Management", "sub": "Administrative leverage for property management companies.",
        "img1": "https://images.unsplash.com/photo-1464938050520-ef2270bb8ce8?q=80&w=1600&auto=format&fit=crop",
        "img2": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=800&auto=format&fit=crop",
        "s1_title": "Streamline Your Property Operations",
        "s1_text": "Property management is death by a thousand cuts. We take over the repetitive administrative tasks like vendor dispatching, notice formatting, and data entry.",
        "features1": ["Work Order Data Entry", "Vendor Coordination", "Tenant Notice Formatting"],
        "features2": ["AppFolio / Buildium Updates", "Lease Renewal Tracking", "Utility Transfer Support"],
        "s2_title": "Reduce Property Manager Burnout.",
        "s2_t1": "Property managers are overworked. By offloading the digital administrative tasks to a RemoteOps VA, they can focus on tenant relations and physical property issues.",
        "s2_t2": "We integrate directly into your existing property management software to provide seamless back office support."
    },
    "industries/real-estate-brokers.html": {
        "cat": "Industry Expertise", "title": "Real Estate Brokers", "sub": "Growth and transaction support for residential real estate teams.",
        "img1": "https://images.unsplash.com/photo-1573164713988-8665fc963095?q=80&w=1600&auto=format&fit=crop",
        "img2": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=800&auto=format&fit=crop",
        "s1_title": "Scale Your Real Estate Team",
        "s1_text": "Top producing agents need leverage. We provide the marketing, CRM, and administrative support necessary to help you double your transaction volume.",
        "features1": ["GoHighLevel & CRM Management", "Social Media Content Creation", "Newsletter Deployment"],
        "features2": ["Listing Presentation Formatting", "Database Nurturing", "Client Onboarding Prep"],
        "s2_title": "Focus on the Client.",
        "s2_t1": "Your clients pay for your local market expertise and negotiation skills, not your ability to format a newsletter.",
        "s2_t2": "A dedicated RemoteOps Virtual Assistant acts as your personal marketing and operations director, executing your strategy flawlessly."
    }
}

template = """
    <main>
        <section class="hero section-light">
            <div class="container text-center reveal fade-in">
                <span class="tag" style="margin-bottom: 2rem;">{cat}</span>
                <h1>{title}</h1>
                <p>{sub}</p>
            </div>
        </section>

        <section class="section-surface" style="padding-top: 0;">
            <div class="container pull-up reveal fade-in">
                <div class="card" style="padding: 0; overflow: hidden; border: none; box-shadow: 0 30px 60px rgba(0,0,0,0.08);">
                    <div style="height: 350px; background: url('{img1}') center/cover;"></div>
                    <div style="padding: 4rem;">
                        <h2 style="margin-bottom: 1.5rem; font-size: 2.25rem;">{s1_title}</h2>
                        <p style="font-size: 1.15rem; color: var(--secondary); line-height: 1.8; margin-bottom: 3rem;">{s1_text}</p>
                        
                        <div class="grid-2">
                            <ul class="feature-list">
                                {f1}
                            </ul>
                            <ul class="feature-list">
                                {f2}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="section-light">
            <div class="container">
                <div class="grid-2" style="align-items: center; gap: 5rem;">
                    <div class="reveal slide-right">
                        <h2 style="font-size: 2.25rem; margin-bottom: 1.5rem;">{s2_title}</h2>
                        <p style="color: var(--secondary); font-size: 1.15rem; line-height: 1.7; margin-bottom: 1.5rem;">{s2_t1}</p>
                        <p style="color: var(--secondary); font-size: 1.15rem; line-height: 1.7; margin-bottom: 2rem;">{s2_t2}</p>
                        <a href="../book-consultation.html" class="btn btn-primary">Book a Free Consultation</a>
                    </div>
                    <div class="reveal slide-left">
                        <div style="border-radius: 16px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                            <img src="{img2}" style="width: 100%; display: block;" alt="Professional Service">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="section-surface">
            <div class="container text-center reveal fade-in">
                <h2 style="margin-bottom: 2rem; font-size: 2.5rem;">Ready to optimize your operations?</h2>
                <p style="color: var(--secondary); font-size: 1.25rem; margin-bottom: 3rem; max-width: 600px; margin-left: auto; margin-right: auto;">Join the top performing real estate teams who trust RemoteOps to handle their CRM, marketing, and back office workflows.</p>
                <a href="../pricing.html" class="btn btn-outline" style="margin-right: 1rem;">View Pricing</a>
                <a href="../book-consultation.html" class="btn btn-primary">Get Started Today</a>
            </div>
        </section>
    </main>
"""

if head and tail:
    for filepath, data in pages_data.items():
        if not os.path.exists(filepath): continue
        
        f1_html = "".join([f"<li>{x}</li>" for x in data["features1"]])
        f2_html = "".join([f"<li>{x}</li>" for x in data["features2"]])
        
        main_html = template.format(
            cat=data["cat"],
            title=data["title"],
            sub=data["sub"],
            img1=data["img1"],
            img2=data["img2"],
            s1_title=data["s1_title"],
            s1_text=data["s1_text"],
            f1=f1_html,
            f2=f2_html,
            s2_title=data["s2_title"],
            s2_t1=data["s2_t1"],
            s2_t2=data["s2_t2"]
        )
        
        with open(filepath, 'w') as f:
            f.write(head + main_html + tail)
            
    print("All 14 service and industry pages enhanced with massive detail and custom designs!")
else:
    print("Could not find shell")
