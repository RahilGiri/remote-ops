import re

with open('case-studies.html', 'r') as f:
    html = f.read()

featured_html = """
    <section class="section-surface" style="padding-top: 4rem; padding-bottom: 2rem;">
    <div class="container reveal fade-in" style="max-width: 1000px;">
      
      <!-- Featured Case Study -->
      <div class="card reveal-item" style="padding: 0; margin-bottom: 4rem; overflow: hidden; border: 1px solid var(--border);">
        <div class="grid-2" style="gap: 0;">
          <!-- Image Side -->
          <div style="width: 100%; height: 100%; min-height: 300px;">
            <img src="https://images.unsplash.com/photo-1560518883-ce09059eeffa?q=80&w=1200&auto=format&fit=crop" style="width: 100%; height: 100%; object-fit: cover;" alt="Real Estate Firm Success">
          </div>
          
          <!-- Content Side -->
          <div style="padding: 3rem; display: flex; flex-direction: column; justify-content: center;">
            <div style="display: inline-block; padding: 4px 12px; background: rgba(37,99,235,0.1); color: var(--primary); font-size: 0.85rem; font-weight: 700; border-radius: 20px; margin-bottom: 1rem; width: fit-content;">FEATURED SUCCESS STORY</div>
            <h2 style="font-size: 2rem; margin-bottom: 1rem; line-height: 1.2;">Scaling Commercial Leasing Operations</h2>
            <p style="color: var(--secondary); margin-bottom: 2rem;">How a top-tier commercial real estate firm reclaimed their senior brokers' time by offloading property marketing, OM formatting, and CRM lead entry to a dedicated RemoteOps VA.</p>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; border-top: 1px solid var(--border); padding-top: 1.5rem;">
              <div>
                <div class="text-gradient" style="font-size: 2.5rem; font-weight: 800; line-height: 1;">25+</div>
                <div style="font-size: 0.85rem; font-weight: 600; color: var(--muted); margin-top: 0.5rem; text-transform: uppercase;">Hours Saved / Week</div>
              </div>
              <div>
                <div class="text-gradient" style="font-size: 2.5rem; font-weight: 800; line-height: 1;">100%</div>
                <div style="font-size: 0.85rem; font-weight: 600; color: var(--muted); margin-top: 0.5rem; text-transform: uppercase;">CRM Data Accuracy</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <h3 style="text-align: center; margin-bottom: 3rem; font-size: 2rem;">More Success Stories</h3>
      <div class="grid-2 reveal-group">
"""

# Replace the `<section class="section-surface">` up to `<div class="grid-2 reveal-group">`
pattern = re.compile(r'<section class="section-surface">.*?<div class="grid-2 reveal-group">', re.DOTALL)
html = pattern.sub(featured_html, html)

with open('case-studies.html', 'w') as f:
    f.write(html)

print("Case studies page redesigned!")
