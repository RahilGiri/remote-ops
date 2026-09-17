import os

with open('css/style.css', 'r') as f:
    css = f.read()

old_banner_css = """.top-banner {
  background: linear-gradient(90deg, #1D4ED8, #2563EB);
  color: #FFFFFF;
  text-align: center;
  padding: 0.75rem;
  font-size: 0.9rem;
  font-weight: 500;
  letter-spacing: 0.02em;
}"""

new_banner_css = """.top-banner {
  background: linear-gradient(90deg, #1D4ED8, #2563EB);
  color: #FFFFFF;
  text-align: center;
  padding: 0.75rem 1rem;
  font-size: 0.9rem;
  font-weight: 500;
  letter-spacing: 0.02em;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}"""

if "flex-wrap" not in css:
    css = css.replace(old_banner_css, new_banner_css)
    with open('css/style.css', 'w') as f:
        f.write(css)

