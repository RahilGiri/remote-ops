import os
import glob

def get_header(root_prefix=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RemoteOps | Operations Partner</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- CSS -->
    <link rel="stylesheet" href="{root_prefix}css/style.css?v=2">
    <link rel="stylesheet" href="{root_prefix}css/responsive.css?v=2">
    <link rel="stylesheet" href="{root_prefix}css/animations.css?v=2">
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

def get_footer(root_prefix=""):
    return f"""    </main>

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

def upgrade_file(filepath):
    # skip index and services which are already upgraded fully via enhance.py
    if filepath == "./index.html" or filepath == "./services.html":
        return
        
    with open(filepath, 'r') as f:
        content = f.read()
        
    if "<main>" not in content or "</main>" not in content:
        return
        
    main_start = content.find("<main>") + 6
    main_end = content.find("</main>")
    
    body_content = content[main_start:main_end]
    
    root_prefix = "../" if "/" in filepath[2:] else ""
    
    new_content = get_header(root_prefix) + body_content + get_footer(root_prefix)
    
    # Also replace any old image styles inside the body content to have proper spacing
    new_content = new_content.replace('<ul>', '<ul class="feature-list">')
    
    with open(filepath, 'w') as f:
        f.write(new_content)
        
    print(f"Upgraded {filepath}")

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            upgrade_file(os.path.join(root, file))

