import os
import re

with open('css/style.css', 'r') as f:
    css = f.read()

marquee_css = """
/* Infinite Scrolling Marquee */
.marquee-container {
  position: relative;
  overflow: hidden;
  width: 100%;
  white-space: nowrap;
  padding: 1rem 0;
}
.marquee-container::before {
  content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 100px;
  background: linear-gradient(to right, var(--background), transparent); z-index: 2;
}
.marquee-container::after {
  content: ''; position: absolute; right: 0; top: 0; bottom: 0; width: 100px;
  background: linear-gradient(to left, var(--background), transparent); z-index: 2;
}
.marquee-content {
  display: inline-flex;
  align-items: center;
  gap: 6rem;
  padding-left: 6rem; /* equal to gap */
  animation: scroll-left 30s linear infinite;
}
.marquee-logo {
  display: flex;
  align-items: center;
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--primary);
  opacity: 0.6;
  filter: grayscale(100%);
  transition: all 0.3s ease;
}
.marquee-logo:hover {
  opacity: 1;
  filter: grayscale(0%);
  transform: scale(1.05);
}
@keyframes scroll-left {
  0% { transform: translateX(0); }
  100% { transform: translateX(-100%); }
}
"""

if "scroll-left" not in css:
    with open('css/style.css', 'a') as f:
        f.write(marquee_css)


with open('index.html', 'r') as f:
    html = f.read()

old_block = """<p>Trusted by operations teams at top real estate firms</p>
      <div class="logo-grid">
        <h3 style="margin:0; font-weight:800;">APEX CAPITAL</h3>
        <h3 style="margin:0; font-weight:800;">LUMINA REALTY</h3>
        <h3 style="margin:0; font-weight:800;">MERIDIAN LEASING</h3>
        <h3 style="margin:0; font-weight:800;">NEXUS PROPERTIES</h3>
        <h3 style="margin:0; font-weight:800;">VANGUARD FUND</h3>
      </div>"""

logos = """
    <span class="marquee-logo">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="var(--accent)" style="margin-right: 12px;"><path d="M12 2L2 22h20L12 2z"/></svg>
      APEX CAPITAL
    </span>
    <span class="marquee-logo">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="var(--primary)" style="margin-right: 12px;"><rect x="3" y="3" width="18" height="18" rx="4"/></svg>
      LUMINA REALTY
    </span>
    <span class="marquee-logo">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="var(--accent)" style="margin-right: 12px;"><circle cx="12" cy="12" r="10"/></svg>
      MERIDIAN LEASING
    </span>
    <span class="marquee-logo">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="var(--primary)" style="margin-right: 12px;"><path d="M12 2L2 12l10 10 10-10L12 2z"/></svg>
      NEXUS PROPERTIES
    </span>
    <span class="marquee-logo">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="var(--accent)" style="margin-right: 12px;"><path d="M22 12l-10 10L2 12 12 2l10 10z"/></svg>
      VANGUARD FUND
    </span>
"""

new_block = f"""<p style="text-transform: uppercase; letter-spacing: 0.1em; color: var(--secondary); font-size: 0.85rem; margin-bottom: 2rem; font-weight: 600;">Trusted by operations teams at top real estate firms</p>
      <div class="marquee-container">
        <div class="marquee-content">
          {logos}
        </div>
        <div class="marquee-content" aria-hidden="true">
          {logos}
        </div>
      </div>"""

html = html.replace(old_block, new_block)

with open('index.html', 'w') as f:
    f.write(html)

print("Trusted by section updated to scrolling marquee!")
