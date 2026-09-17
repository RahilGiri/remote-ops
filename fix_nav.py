import os
import re

nav_template = """    <nav>
      <ul class="nav-links">
        <li><a href="{prefix}index.html">Home</a></li>
        <li class="dropdown">
        <a href="{prefix}services.html">Services ▾</a>
        <ul class="dropdown-menu">
          <li><a href="{prefix}services/crm-gohighlevel.html">CRM & GoHighLevel</a></li>
          <li><a href="{prefix}services/lead-generation.html">Lead Generation</a></li>
          <li><a href="{prefix}services/investor-outreach.html">Investor Outreach</a></li>
          <li><a href="{prefix}services/email-marketing.html">Email Marketing</a></li>
          <li><a href="{prefix}services/social-media.html">Social Media Management</a></li>
          <li><a href="{prefix}services/real-estate-marketing.html">Real Estate Marketing</a></li>
          <li><a href="{prefix}services/operations-support.html">Operations Support</a></li>
          <li><a href="{prefix}services/digital-support.html">Digital Support</a></li>
        </ul>
        </li>
        <li class="dropdown">
        <a href="{prefix}industries.html">Industries ▾</a>
        <ul class="dropdown-menu">
          <li><a href="{prefix}industries/fund-managers.html">Fund Managers</a></li>
          <li><a href="{prefix}industries/real-estate-investment.html">Real Estate Investment</a></li>
          <li><a href="{prefix}industries/commercial-real-estate.html">Commercial Real Estate</a></li>
          <li><a href="{prefix}industries/leasing.html">Leasing</a></li>
          <li><a href="{prefix}industries/property-management.html">Property Management</a></li>
          <li><a href="{prefix}industries/real-estate-brokers.html">Real Estate Brokers</a></li>
        </ul>
        </li>
        <li><a href="{prefix}how-it-works.html">How It Works</a></li>
        <li><a href="{prefix}pricing.html">Pricing</a></li>
        <li><a href="{prefix}case-studies.html">Case Studies</a></li>
        <li><a href="{prefix}about.html">About</a></li>
        <li><a href="{prefix}book-consultation.html" class="btn btn-primary" style="padding: 0.75rem 1.5rem;">Book Consultation</a></li>
      </ul>
    </nav>"""

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Determine prefix
            prefix = ""
            if "services/" in filepath or "industries/" in filepath:
                prefix = "../"
                
            new_nav = nav_template.format(prefix=prefix)
            
            # Replace existing nav block
            # Matches from <nav> up to </nav>
            pattern = re.compile(r'<nav>.*?</nav>', re.DOTALL)
            content = pattern.sub(new_nav, content)
            
            with open(filepath, 'w') as f:
                f.write(content)

print("Navigation standardized globally!")
