import os

def create_page(path, title, description, h1, body_content, root_prefix=""):
    
    header = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    
    <!-- SEO & Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <link rel="canonical" href="https://yourdomain.com/{path.replace('index.html', '')}">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- CSS -->
    <link rel="stylesheet" href="{root_prefix}css/style.css">
    <link rel="stylesheet" href="{root_prefix}css/responsive.css">
    <link rel="stylesheet" href="{root_prefix}css/animations.css">
</head>
<body>

    <!-- Top Banner -->
    <div class="top-banner">
        Now accepting new operations clients for Q4. <a href="{root_prefix}book-consultation.html" style="color: var(--primary); text-decoration: underline; margin-left: 0.5rem;">Secure your spot &rarr;</a>
    </div>

    <!-- Navigation -->
    <header>
        <div class="nav-container">
            <a href="{root_prefix}index.html" class="logo">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect x="2" y="3" width="20" height="18" rx="2" stroke="var(--primary)" stroke-width="2"/>
                    <path d="M2 9H22" stroke="var(--primary)" stroke-width="2"/>
                    <path d="M9 21V9" stroke="var(--primary)" stroke-width="2"/>
                </svg>
                Remote<span>Ops</span>
            </a>
            
            <button class="mobile-menu-btn" aria-label="Toggle menu" aria-expanded="false">☰</button>
            
            <nav>
                <ul class="nav-links">
                    <li><a href="{root_prefix}index.html">Home</a></li>
                    <li class="dropdown">
                        <a href="{root_prefix}services.html">Services ▾</a>
                        <ul class="dropdown-menu">
                            <li><a href="{root_prefix}services/crm-gohighlevel.html">CRM & GoHighLevel</a></li>
                            <li><a href="{root_prefix}services/lead-generation.html">Lead Generation</a></li>
                            <li><a href="{root_prefix}services/investor-outreach.html">Investor Outreach</a></li>
                            <li><a href="{root_prefix}services/email-marketing.html">Email Marketing</a></li>
                            <li><a href="{root_prefix}services/social-media.html">Social Media Management</a></li>
                            <li><a href="{root_prefix}services/real-estate-marketing.html">Real Estate Marketing</a></li>
                            <li><a href="{root_prefix}services/operations-support.html">Operations Support</a></li>
                            <li><a href="{root_prefix}services/digital-support.html">Digital Support</a></li>
                        </ul>
                    </li>
                    <li class="dropdown">
                        <a href="{root_prefix}industries.html">Industries ▾</a>
                        <ul class="dropdown-menu">
                            <li><a href="{root_prefix}industries/fund-managers.html">Fund Managers</a></li>
                            <li><a href="{root_prefix}industries/real-estate-investment.html">Real Estate Investment</a></li>
                            <li><a href="{root_prefix}industries/commercial-real-estate.html">Commercial Real Estate</a></li>
                            <li><a href="{root_prefix}industries/leasing.html">Leasing</a></li>
                            <li><a href="{root_prefix}industries/property-management.html">Property Management</a></li>
                            <li><a href="{root_prefix}industries/real-estate-brokers.html">Real Estate Brokers</a></li>
                        </ul>
                    </li>
                    <li><a href="{root_prefix}how-it-works.html">How It Works</a></li>
                    <li><a href="{root_prefix}case-studies.html">Case Studies</a></li>
                    <li><a href="{root_prefix}about.html">About</a></li>
                    <li><a href="{root_prefix}book-consultation.html" class="btn btn-primary" style="padding: 0.75rem 1.5rem;">Book Consultation</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
"""

    footer = f"""
    </main>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <div class="logo" style="color: var(--background); margin-bottom: 1.5rem;">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect x="2" y="3" width="20" height="18" rx="2" stroke="var(--background)" stroke-width="2"/>
                            <path d="M2 9H22" stroke="var(--background)" stroke-width="2"/>
                            <path d="M9 21V9" stroke="var(--background)" stroke-width="2"/>
                        </svg>
                        Remote<span style="color: var(--accent)">Ops</span>
                    </div>
                    <p style="color: #94A3B8; font-size: 1rem;">A Remote Operations & Growth Support Partner for Real Estate & Investment Businesses across the US.</p>
                </div>
                
                <div class="footer-col">
                    <h4>COMPANY</h4>
                    <ul>
                        <li><a href="{root_prefix}about.html">About Our Approach</a></li>
                        <li><a href="{root_prefix}how-it-works.html">How It Works</a></li>
                        <li><a href="{root_prefix}case-studies.html">Client Case Studies</a></li>
                        <li><a href="{root_prefix}contact.html">Contact Us</a></li>
                        <li><a href="{root_prefix}book-consultation.html">Book a Consultation</a></li>
                    </ul>
                </div>
                
                <div class="footer-col">
                    <h4>CORE SERVICES</h4>
                    <ul>
                        <li><a href="{root_prefix}services/crm-gohighlevel.html">CRM & GoHighLevel</a></li>
                        <li><a href="{root_prefix}services/lead-generation.html">Lead Generation</a></li>
                        <li><a href="{root_prefix}services/investor-outreach.html">Investor Outreach</a></li>
                        <li><a href="{root_prefix}services/email-marketing.html">Email Marketing</a></li>
                        <li><a href="{root_prefix}services/social-media.html">Social Media Strategy</a></li>
                        <li><a href="{root_prefix}services/operations-support.html">Operations Support</a></li>
                    </ul>
                </div>
                
                <div class="footer-col">
                    <h4>INDUSTRIES SERVED</h4>
                    <ul>
                        <li><a href="{root_prefix}industries/fund-managers.html">Fund Managers</a></li>
                        <li><a href="{root_prefix}industries/real-estate-investment.html">Real Estate Investment Firms</a></li>
                        <li><a href="{root_prefix}industries/commercial-real-estate.html">Commercial Real Estate</a></li>
                        <li><a href="{root_prefix}industries/property-management.html">Property Management</a></li>
                        <li><a href="{root_prefix}industries/real-estate-brokers.html">Real Estate Brokers</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <div>&copy; <span id="current-year"></span> RemoteOps. All rights reserved. Operating nationwide across the US.</div>
                <div class="footer-links">
                    <a href="mailto:hello@remoteops.example">hello@remoteops.example</a>
                    <a href="tel:+18005550199">(800) 555-0199</a>
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- JavaScript -->
    <script src="{root_prefix}js/navigation.js"></script>
    <script src="{root_prefix}js/animations.js"></script>
    <script src="{root_prefix}js/forms.js"></script>
    <script src="{root_prefix}js/main.js"></script>
</body>
</html>"""

    full_html = header + body_content + footer
    
    if os.path.dirname(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(full_html)
    print(f"Generated enhanced {path}")

pages = {
    "index.html": {
        "title": "RemoteOps | Remote Operations Partner for Real Estate",
        "description": "Remote operations, marketing, CRM, research, outreach, and administrative support for real estate and investment businesses.",
        "root_prefix": "",
        "content": """
        <!-- HERO -->
        <section class="hero section-light">
            <div class="container grid-2">
                <div class="hero-content reveal slide-right">
                    <span class="tag">B2B Operations Partner</span>
                    <h1>You Focus on the Deals. We Handle the Work Behind Them.</h1>
                    <p>Stop drowning in administrative tasks. We provide premium remote operations, CRM management, research, and marketing support exclusively for US-based real estate and investment businesses.</p>
                    <div class="hero-buttons">
                        <a href="book-consultation.html" class="btn btn-primary">Book a Free Consultation</a>
                        <a href="services.html" class="btn btn-outline">Explore Our Services</a>
                    </div>
                    <ul class="feature-list mt-2">
                        <li>Dedicated US-focused support</li>
                        <li>Seamless CRM & GoHighLevel integration</li>
                        <li>Data-driven investor outreach</li>
                    </ul>
                </div>
                <div class="hero-visual reveal slide-left">
                    <div class="image-wrapper">
                        <!-- High quality professional dashboard / analytics image -->
                        <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1000&auto=format&fit=crop" alt="Real Estate CRM Dashboard" class="img-fluid" />
                    </div>
                </div>
            </div>
        </section>

        <!-- LOGO STRIP -->
        <div class="logo-strip reveal fade-in">
            <div class="container">
                <p>Trusted by operations teams at top real estate firms</p>
                <div class="logo-grid">
                    <h3 style="margin:0; font-weight:800;">APEX CAPITAL</h3>
                    <h3 style="margin:0; font-weight:800;">LUMINA REALTY</h3>
                    <h3 style="margin:0; font-weight:800;">MERIDIAN LEASING</h3>
                    <h3 style="margin:0; font-weight:800;">NEXUS PROPERTIES</h3>
                    <h3 style="margin:0; font-weight:800;">VANGUARD FUND</h3>
                </div>
            </div>
        </div>

        <!-- PROBLEM -->
        <section class="section-surface-alt">
            <div class="container grid-2" style="align-items: center;">
                <div class="reveal slide-right">
                    <div class="image-wrapper">
                        <img src="https://images.unsplash.com/photo-1497215728101-856f4ea42174?q=80&w=1000&auto=format&fit=crop" alt="Corporate Office" class="img-fluid" />
                    </div>
                </div>
                <div class="reveal slide-left" style="padding-left: 2rem;">
                    <span class="tag">The Bottleneck</span>
                    <h2>Your Time Should Be Spent on Deals &mdash; Not Repetitive Tasks.</h2>
                    <p>Real estate and investment businesses require massive amounts of supporting work. From updating CRM pipelines to building lead lists, formatting email campaigns, and compiling reports — these tasks eat up hours of your high-value time every single week.</p>
                    <p>We take the operational burden off your plate so you can focus on underwriting, negotiating, and closing.</p>
                    <a href="services.html" class="btn btn-primary mt-1">See What We Can Handle &rarr;</a>
                </div>
            </div>
        </section>

        <!-- SERVICES -->
        <section class="section-light">
            <div class="container">
                <div class="section-header reveal fade-in">
                    <span class="tag">Our Capabilities</span>
                    <h2>Operational Support for the Work Behind the Deal.</h2>
                    <p style="margin-top: 1rem;">We act as an extension of your team, handling the specialized workflows that keep your pipeline moving and your brand visible.</p>
                </div>
                <div class="grid-4 reveal-group">
                    <div class="card reveal-item">
                        <div class="card-icon">📊</div>
                        <h3 class="card-title">CRM & GoHighLevel</h3>
                        <div class="card-content">
                            <p style="font-size: 0.95rem;">Pipeline management, automation, lead entry, and thorough CRM cleanup so no lead slips through.</p>
                        </div>
                        <a href="services/crm-gohighlevel.html" class="card-link">Explore Service &rarr;</a>
                    </div>
                    <div class="card reveal-item">
                        <div class="card-icon">🔍</div>
                        <h3 class="card-title">Lead Generation</h3>
                        <div class="card-content">
                            <p style="font-size: 0.95rem;">Targeted LinkedIn Sales Navigator research, list building, and data verification for outbound campaigns.</p>
                        </div>
                        <a href="services/lead-generation.html" class="card-link">Explore Service &rarr;</a>
                    </div>
                    <div class="card reveal-item">
                        <div class="card-icon">🤝</div>
                        <h3 class="card-title">Investor Outreach</h3>
                        <div class="card-content">
                            <p style="font-size: 0.95rem;">Consistent, professional outreach and follow-up management to keep your calendar booked.</p>
                        </div>
                        <a href="services/investor-outreach.html" class="card-link">Explore Service &rarr;</a>
                    </div>
                    <div class="card reveal-item">
                        <div class="card-icon">✉️</div>
                        <h3 class="card-title">Email Marketing</h3>
                        <div class="card-content">
                            <p style="font-size: 0.95rem;">Beautiful newsletters, automated drip campaigns, and lead nurturing sequences.</p>
                        </div>
                        <a href="services/email-marketing.html" class="card-link">Explore Service &rarr;</a>
                    </div>
                </div>
                <div class="text-center mt-4 reveal fade-in">
                    <a href="services.html" class="btn btn-outline">View All 8 Services</a>
                </div>
            </div>
        </section>

        <!-- NOT JUST A VA -->
        <section class="section-surface">
            <div class="container grid-2" style="align-items: center;">
                <div class="reveal slide-right">
                    <span class="tag">The Difference</span>
                    <h2>More Than Virtual Assistance. We Are an Operations Partner.</h2>
                    <p>Most VA agencies simply complete isolated tasks without understanding the bigger picture of a real estate transaction. We don't just check boxes.</p>
                    <ul class="feature-list">
                        <li><strong>We learn your workflow:</strong> We adapt to your specific processes and preferences.</li>
                        <li><strong>We understand your systems:</strong> Fluent in GoHighLevel, Sales Navigator, and real estate CRMs.</li>
                        <li><strong>We provide proactive reporting:</strong> You never have to guess what was accomplished this week.</li>
                    </ul>
                </div>
                <div class="reveal slide-left">
                    <div class="image-wrapper">
                        <!-- High quality architecture/real estate investment image -->
                        <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1000&auto=format&fit=crop" alt="Commercial Real Estate" class="img-fluid" />
                    </div>
                </div>
            </div>
        </section>

        <!-- TESTIMONIAL -->
        <section class="section-light">
            <div class="container reveal fade-in">
                <div class="testimonial-card">
                    <p class="testimonial-text">"Before RemoteOps, I was spending 15 hours a week just cleaning up our CRM and formatting email blasts for our syndication deals. They completely took over the backend operations, and our outbound volume has tripled while my stress has vanished."</p>
                    <div class="testimonial-author">
                        <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=100&auto=format&fit=crop" alt="Client" class="author-avatar" />
                        <div class="author-info">
                            <h4>Michael T.</h4>
                            <p>Managing Partner, Commercial Real Estate Firm</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- HOW IT WORKS -->
        <section class="section-surface-alt">
            <div class="container text-center reveal fade-in">
                <div class="section-header">
                    <span class="tag">Process</span>
                    <h2>How It Works</h2>
                    <p>A streamlined onboarding process designed for busy professionals.</p>
                </div>
                <div class="grid-4 reveal-group">
                    <div class="card reveal-item" style="border-top: 4px solid var(--accent);">
                        <div style="font-size: 2.5rem; color: var(--accent); font-weight: 800; line-height: 1;">01</div>
                        <h3 class="card-title mt-1">Tell Us What You Need</h3>
                        <p style="font-size: 0.95rem;">Book a quick call to discuss the exact tasks weighing down your week.</p>
                    </div>
                    <div class="card reveal-item" style="border-top: 4px solid var(--accent);">
                        <div style="font-size: 2.5rem; color: var(--accent); font-weight: 800; line-height: 1;">02</div>
                        <h3 class="card-title mt-1">Identify & Delegate</h3>
                        <p style="font-size: 0.95rem;">We'll help you identify the highest-leverage tasks to hand off first.</p>
                    </div>
                    <div class="card reveal-item" style="border-top: 4px solid var(--accent);">
                        <div style="font-size: 2.5rem; color: var(--accent); font-weight: 800; line-height: 1;">03</div>
                        <h3 class="card-title mt-1">Build Your Workflow</h3>
                        <p style="font-size: 0.95rem;">We document the SOPs and integrate directly into your existing tools.</p>
                    </div>
                    <div class="card reveal-item" style="border-top: 4px solid var(--accent);">
                        <div style="font-size: 2.5rem; color: var(--accent); font-weight: 800; line-height: 1;">04</div>
                        <h3 class="card-title mt-1">Execute & Report</h3>
                        <p style="font-size: 0.95rem;">We execute consistently and send you clean, weekly progress reports.</p>
                    </div>
                </div>
                <a href="how-it-works.html" class="btn btn-outline mt-4">Read Detailed Process &rarr;</a>
            </div>
        </section>

        <!-- FINAL CTA -->
        <section class="section-dark text-center" style="position: relative; overflow: hidden;">
            <div class="container reveal fade-in" style="position: relative; z-index: 2;">
                <h2 style="font-size: 3.5rem;">What Could You Delegate This Week?</h2>
                <p class="mb-3" style="font-size: 1.25rem; max-width: 700px; margin-left: auto; margin-right: auto; color: var(--surface);">Tell us what is taking up your time. We’ll discuss where remote support can instantly fit into your business and give you your hours back.</p>
                <div style="display: flex; gap: 1rem; justify-content: center;">
                    <a href="book-consultation.html" class="btn btn-accent" style="padding: 1.25rem 2.5rem; font-size: 1.125rem;">Book a Free Consultation</a>
                </div>
            </div>
        </section>
        """
    }
}

for path, page_data in pages.items():
    create_page(
        path=path,
        title=page_data['title'],
        description=page_data['description'],
        h1="",
        body_content=page_data['content'],
        root_prefix=page_data['root_prefix']
    )

pages_extra = {
    "services.html": {
        "title": "Services | RemoteOps",
        "description": "Premium Remote Support for the Work That Keeps Your Business Moving.",
        "root_prefix": "",
        "content": """
        <section class="hero section-light" style="padding-bottom: 4rem; grid-template-columns: 1fr;">
            <div class="container text-center reveal fade-in">
                <span class="tag">Our Expertise</span>
                <h1 style="max-width: 900px; margin: 0 auto 1.5rem;">Remote Support for the Work That Keeps Your Business Moving.</h1>
                <p style="max-width: 800px; margin: 0 auto;">We don't do everything. We specialize in the exact operational, marketing, and CRM workflows that real estate and investment firms need to scale.</p>
            </div>
        </section>

        <section class="section-surface">
            <div class="container">
                <div class="grid-3 reveal-group">
                    <div class="card reveal-item">
                        <div class="card-icon">📊</div>
                        <h3 class="card-title">CRM & GoHighLevel</h3>
                        <div class="card-content">
                            <p>Keep your pipeline organized and automated. We manage your database so you can manage the relationships.</p>
                            <ul class="feature-list" style="font-size: 0.875rem;">
                                <li>Pipeline management</li>
                                <li>Workflow automation</li>
                                <li>Data cleanup</li>
                            </ul>
                        </div>
                        <a href="services/crm-gohighlevel.html" class="btn btn-outline" style="width:100%; margin-top: 1.5rem;">View Details</a>
                    </div>
                    <div class="card reveal-item">
                        <div class="card-icon">🔍</div>
                        <h3 class="card-title">Lead Generation</h3>
                        <div class="card-content">
                            <p>Find the right prospects and build better lists using advanced tools and manual verification.</p>
                            <ul class="feature-list" style="font-size: 0.875rem;">
                                <li>LinkedIn Sales Navigator</li>
                                <li>Prospect research</li>
                                <li>Contact verification</li>
                            </ul>
                        </div>
                        <a href="services/lead-generation.html" class="btn btn-outline" style="width:100%; margin-top: 1.5rem;">View Details</a>
                    </div>
                    <div class="card reveal-item">
                        <div class="card-icon">🤝</div>
                        <h3 class="card-title">Investor Outreach</h3>
                        <div class="card-content">
                            <p>Consistent outreach without the manual work. We execute your outbound strategy flawlessly.</p>
                            <ul class="feature-list" style="font-size: 0.875rem;">
                                <li>Email sequencing</li>
                                <li>Follow-up tracking</li>
                                <li>Meeting coordination</li>
                            </ul>
                        </div>
                        <a href="services/investor-outreach.html" class="btn btn-outline" style="width:100%; margin-top: 1.5rem;">View Details</a>
                    </div>
                    <div class="card reveal-item">
                        <div class="card-icon">✉️</div>
                        <h3 class="card-title">Email Marketing</h3>
                        <div class="card-content">
                            <p>Stay consistently in front of your network with professional, well-formatted email campaigns.</p>
                            <ul class="feature-list" style="font-size: 0.875rem;">
                                <li>Investor newsletters</li>
                                <li>Deal blasts</li>
                                <li>List segmentation</li>
                            </ul>
                        </div>
                        <a href="services/email-marketing.html" class="btn btn-outline" style="width:100%; margin-top: 1.5rem;">View Details</a>
                    </div>
                    <div class="card reveal-item">
                        <div class="card-icon">📱</div>
                        <h3 class="card-title">Social Media</h3>
                        <div class="card-content">
                            <p>Maintain an active, authoritative presence on LinkedIn and other platforms without spending hours drafting posts.</p>
                            <ul class="feature-list" style="font-size: 0.875rem;">
                                <li>Content calendars</li>
                                <li>Canva graphics</li>
                                <li>Post scheduling</li>
                            </ul>
                        </div>
                        <a href="services/social-media.html" class="btn btn-outline" style="width:100%; margin-top: 1.5rem;">View Details</a>
                    </div>
                    <div class="card reveal-item">
                        <div class="card-icon">🏢</div>
                        <h3 class="card-title">Real Estate Marketing</h3>
                        <div class="card-content">
                            <p>Professional marketing support for individual properties, syndication deals, and fund launches.</p>
                            <ul class="feature-list" style="font-size: 0.875rem;">
                                <li>Digital flyers (OMs)</li>
                                <li>Landing pages</li>
                                <li>Brand consistency</li>
                            </ul>
                        </div>
                        <a href="services/real-estate-marketing.html" class="btn btn-outline" style="width:100%; margin-top: 1.5rem;">View Details</a>
                    </div>
                </div>
            </div>
        </section>

        <section class="section-light">
            <div class="container grid-2" style="align-items: center;">
                <div class="reveal slide-right">
                    <div class="image-wrapper">
                        <img src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=1000&auto=format&fit=crop" alt="Operations Strategy" class="img-fluid" />
                    </div>
                </div>
                <div class="reveal slide-left">
                    <h2>Not sure exactly what you need?</h2>
                    <p>Many of our clients come to us knowing they are overwhelmed, but aren't sure exactly which tasks to delegate first. That's perfectly normal.</p>
                    <p>During our consultation, we will audit your current workflow and recommend a customized support plan that provides the highest immediate ROI for your time.</p>
                    <a href="book-consultation.html" class="btn btn-primary mt-1">Schedule a Workflow Audit</a>
                </div>
            </div>
        </section>
        """
    }
}

for path, page_data in pages_extra.items():
    create_page(
        path=path,
        title=page_data['title'],
        description=page_data['description'],
        h1="",
        body_content=page_data['content'],
        root_prefix=page_data['root_prefix']
    )
