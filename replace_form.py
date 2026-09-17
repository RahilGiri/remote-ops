import re

with open('book-consultation.html', 'r') as f:
    html = f.read()

form_html = """
        <h3 class="mb-1 text-center">Request a Consultation</h3>
        <p class="text-center" style="color: var(--secondary); margin-bottom: 2rem; font-size: 0.95rem;">Fill out the form below and our team will reach out to schedule your introductory call.</p>
        
        <form id="consultationForm" action="#" method="POST" onsubmit="event.preventDefault(); alert('Form successfully submitted! We will contact you shortly.');">
          <div class="form-group">
            <label class="form-label" for="fullName">Full Name *</label>
            <input type="text" id="fullName" class="form-control" required placeholder="John Doe">
          </div>
          
          <div class="form-group">
            <label class="form-label" for="email">Work Email *</label>
            <input type="email" id="email" class="form-control" required placeholder="john@example.com">
          </div>
          
          <div class="form-group">
            <label class="form-label" for="phone">Phone Number</label>
            <input type="tel" id="phone" class="form-control" placeholder="(555) 000-0000">
          </div>
          
          <div class="form-group">
            <label class="form-label" for="industry">Industry</label>
            <select id="industry" class="form-control">
              <option value="" disabled selected>Select your industry...</option>
              <option value="broker">Real Estate Broker</option>
              <option value="fund">Fund Manager / Syndicator</option>
              <option value="property">Property Management</option>
              <option value="other">Other</option>
            </select>
          </div>
          
          <div class="form-group" style="margin-bottom: 2rem;">
            <label class="form-label" for="message">What processes are you looking to outsource?</label>
            <textarea id="message" class="form-control" rows="4" placeholder="e.g. CRM management, lead generation, formatting OMs..."></textarea>
          </div>
          
          <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Request</button>
        </form>
"""

# Replace everything inside the card
old_card_content_regex = re.compile(r'<h3 class="mb-1 text-center">Schedule a Time</h3>.*?Use Contact Form</a>\s*</div>', re.DOTALL)
html = old_card_content_regex.sub(form_html, html)

with open('book-consultation.html', 'w') as f:
    f.write(html)

print("Form successfully injected!")
