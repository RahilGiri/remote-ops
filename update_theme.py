import os

css_content = """
:root {
  /* Colors - Modern Slate & Royal Blue Theme */
  --primary: #0F172A;
  --primary-light: #1E293B;
  --secondary: #475569;
  --background: #FFFFFF;
  --surface: #F8FAFC;
  --surface-alt: #F1F5F9;
  --muted: #64748B;
  --accent: #2563EB;
  --accent-hover: #1D4ED8;
  --accent-light: #EFF6FF;
  --text-main: #0F172A;
  --text-light: #F8FAFC;
  --border: #E2E8F0;
  
  /* Typography */
  --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
  
  /* Layout */
  --container-width: 1280px;
  --nav-height: 85px;
  --radius-sm: 8px;
  --radius-md: 16px;
  --radius-lg: 24px;
  
  /* Shadows - Softer & More Modern */
  --shadow-sm: 0 1px 2px 0 rgba(15, 23, 42, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(15, 23, 42, 0.08), 0 2px 4px -1px rgba(15, 23, 42, 0.04);
  --shadow-lg: 0 12px 20px -3px rgba(15, 23, 42, 0.08), 0 4px 6px -2px rgba(15, 23, 42, 0.04);
  --shadow-xl: 0 25px 30px -5px rgba(15, 23, 42, 0.08), 0 10px 10px -5px rgba(15, 23, 42, 0.03);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: var(--font-sans);
  background-color: var(--background);
  color: var(--text-main);
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
  color: var(--primary);
  line-height: 1.15;
  font-weight: 800;
  margin-bottom: 1.25rem;
  letter-spacing: -0.03em;
}

h1 { font-size: 3.5rem; }
h2 { font-size: 2.75rem; letter-spacing: -0.02em; }
h3 { font-size: 1.5rem; letter-spacing: -0.01em; }

p { color: var(--secondary); margin-bottom: 1.5rem; font-size: 1.125rem; }

a { color: var(--accent); text-decoration: none; transition: all 0.3s ease; }
a:hover { color: var(--accent-hover); }

/* Layout */
.container { max-width: var(--container-width); margin: 0 auto; padding: 0 2rem; }
section { padding: 8rem 0; }
.section-light { background-color: var(--background); }
.section-surface { background-color: var(--surface); }
.section-surface-alt { background-color: var(--surface-alt); }
.section-dark { background-color: var(--primary); color: var(--text-light); }
.section-dark h1, .section-dark h2, .section-dark h3 { color: var(--text-light); }
.section-dark p { color: #94A3B8; }

/* Top Banner */
.top-banner {
  background: linear-gradient(90deg, #1D4ED8, #2563EB);
  color: #FFFFFF;
  text-align: center;
  padding: 0.75rem;
  font-size: 0.9rem;
  font-weight: 500;
  position: relative;
  z-index: 1001;
}

/* Header & Nav */
header {
  position: sticky;
  top: 0; left: 0; width: 100%; height: var(--nav-height);
  background-color: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  z-index: 1000;
  transition: all 0.3s ease;
}
.nav-container { display: flex; justify-content: space-between; align-items: center; height: 100%; max-width: var(--container-width); margin: 0 auto; padding: 0 2rem; }
.logo { font-size: 1.5rem; font-weight: 800; color: var(--primary); display: flex; align-items: center; gap: 0.5rem; }
.logo span { color: var(--accent); }
.nav-links { display: flex; gap: 2.5rem; list-style: none; align-items: center; }
.nav-links li { position: relative; }
.nav-links a { color: var(--secondary); font-weight: 600; font-size: 0.95rem; }
.nav-links a:hover { color: var(--accent); }
.nav-links a.btn-primary { color: var(--background); }
.nav-links a.btn-primary:hover { color: var(--background); }

/* Dropdown */
.dropdown-menu {
  position: absolute; top: 100%; left: -20px;
  background: var(--background); min-width: 280px;
  box-shadow: var(--shadow-xl); border: 1px solid var(--border);
  border-radius: var(--radius-md); padding: 1rem 0;
  opacity: 0; visibility: hidden; transform: translateY(15px);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.dropdown:hover .dropdown-menu { opacity: 1; visibility: visible; transform: translateY(0); }
.dropdown-menu li { padding: 0; }
.dropdown-menu a { display: block; padding: 0.75rem 1.5rem; font-size: 0.95rem; color: var(--secondary); border-left: 3px solid transparent; font-weight: 500; }
.dropdown-menu a:hover { background-color: var(--surface); color: var(--accent); border-left-color: var(--accent); }

/* Buttons */
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  padding: 1rem 2rem; border-radius: var(--radius-sm);
  font-weight: 600; font-size: 1rem; text-align: center;
  cursor: pointer; transition: all 0.3s ease; border: none; gap: 0.5rem;
}
.btn-primary { background-color: var(--accent); color: var(--background); box-shadow: 0 4px 14px 0 rgba(37, 99, 235, 0.39); }
.btn-primary:hover { background-color: var(--accent-hover); transform: translateY(-2px); box-shadow: 0 6px 20px rgba(37, 99, 235, 0.23); color: var(--background); }
.btn-outline { background-color: transparent; color: var(--primary); border: 2px solid var(--border); }
.btn-outline:hover { border-color: var(--primary); background-color: var(--surface); color: var(--primary); }
.btn-accent { background-color: var(--background); color: var(--primary); }
.btn-accent:hover { background-color: var(--surface); color: var(--primary); transform: translateY(-2px); }

/* Footer */
footer { background-color: var(--primary); color: var(--text-light); padding: 6rem 0 2rem; }
.footer-grid { display: grid; grid-template-columns: 2fr 1.5fr 1.5fr 1.5fr; gap: 4rem; margin-bottom: 4rem; }
.footer-col h4 { color: var(--background); font-size: 1rem; margin-bottom: 1.5rem; letter-spacing: 0.05em; text-transform: uppercase; }
.footer-col ul { list-style: none; }
.footer-col ul li { margin-bottom: 0.875rem; }
.footer-col ul a { color: #94A3B8; transition: color 0.3s ease; font-size: 0.95rem; font-weight: 400; }
.footer-col ul a:hover { color: var(--background); }
.footer-bottom { border-top: 1px solid rgba(255, 255, 255, 0.1); padding-top: 2rem; display: flex; justify-content: space-between; align-items: center; color: #94A3B8; font-size: 0.875rem; }
.footer-links { display: flex; gap: 2rem; }
.footer-links a { color: #94A3B8; }
.footer-links a:hover { color: var(--background); }

/* Cards & Grid */
.grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 4rem; }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.5rem; }
.grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; }

.card {
  background: var(--background); border: 1px solid var(--border);
  border-radius: var(--radius-md); padding: 2.5rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
  height: 100%; display: flex; flex-direction: column;
}
.card:hover { transform: translateY(-8px); box-shadow: var(--shadow-xl); border-color: var(--accent); }
.card-icon { width: 64px; height: 64px; background-color: var(--accent-light); border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center; margin-bottom: 2rem; color: var(--accent); font-size: 1.75rem; }
.card-title { font-size: 1.35rem; margin-bottom: 1rem; }
.card-content { flex-grow: 1; }
.card-content p { font-size: 1rem; }
.card-link { display: inline-flex; align-items: center; gap: 0.5rem; font-weight: 600; font-size: 0.95rem; margin-top: 1.5rem; color: var(--accent); }
.card-link:hover { color: var(--accent-hover); }

/* Feature List */
.feature-list { list-style: none; margin-top: 1.5rem; }
.feature-list li { position: relative; padding-left: 2rem; margin-bottom: 1rem; color: var(--secondary); font-size: 1rem; }
.feature-list li::before {
  content: '✓'; position: absolute; left: 0;
  color: var(--accent); font-weight: bold;
  background: var(--accent-light);
  width: 20px; height: 20px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.75rem; top: 2px;
}

/* Utilities */
.text-center { text-align: center; }
.mt-1 { margin-top: 1rem; } .mt-2 { margin-top: 2rem; } .mt-3 { margin-top: 3rem; } .mt-4 { margin-top: 4rem; }
.mb-1 { margin-bottom: 1rem; } .mb-2 { margin-bottom: 2rem; } .mb-3 { margin-bottom: 3rem; } .mb-4 { margin-bottom: 4rem; }
.section-header { max-width: 800px; margin: 0 auto 4rem; text-align: center; }
.tag {
  display: inline-block; padding: 0.35rem 1.25rem;
  background-color: var(--accent-light); color: var(--accent);
  border-radius: 20px; font-size: 0.85rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1.5rem;
}

/* Images & Media */
.img-fluid { width: 100%; height: 100%; object-fit: cover; aspect-ratio: 4/3; border-radius: var(--radius-md); box-shadow: var(--shadow-xl); }
.image-wrapper { position: relative; border-radius: var(--radius-md); overflow: hidden; }
.image-wrapper::after { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: var(--radius-md); box-shadow: inset 0 0 0 1px rgba(0,0,0,0.05); pointer-events: none; }

/* Hero Section */
.hero { padding-top: 5rem; padding-bottom: 8rem; background: linear-gradient(180deg, var(--surface) 0%, #FFFFFF 100%); }
.hero .grid-2 { align-items: center; grid-template-columns: 1.3fr 1fr; gap: 4rem; }
.hero-content p { font-size: 1.25rem; margin-bottom: 2.5rem; color: var(--secondary); }
.hero-buttons { display: flex; gap: 1.5rem; margin-top: 2rem; }
.logo-strip { border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); padding: 4rem 0; background: var(--background); }
.logo-strip p { text-align: center; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600; margin-bottom: 2.5rem; color: var(--muted); }
.logo-grid { display: flex; justify-content: space-between; align-items: center; opacity: 0.4; filter: grayscale(100%); gap: 2rem; flex-wrap: wrap; }

/* Testimonials */
.testimonial-card { background: var(--background); padding: 4rem; border-radius: var(--radius-lg); box-shadow: var(--shadow-xl); border-top: 4px solid var(--accent); text-align: center; }
.testimonial-text { font-size: 1.5rem; font-weight: 500; color: var(--primary); margin-bottom: 2.5rem; line-height: 1.5; }
.testimonial-author { display: flex; align-items: center; justify-content: center; gap: 1rem; }
.author-avatar { width: 64px; height: 64px; border-radius: 50%; background-color: var(--surface); object-fit: cover; }
.author-info h4 { margin: 0; font-size: 1.125rem; }
.author-info p { margin: 0; font-size: 0.95rem; color: var(--muted); }

/* Forms */
.form-group { margin-bottom: 1.5rem; }
.form-label { display: block; margin-bottom: 0.5rem; font-weight: 500; color: var(--primary); font-size: 0.95rem; }
.form-control { width: 100%; padding: 0.875rem 1rem; border: 1px solid var(--border); border-radius: var(--radius-sm); font-family: var(--font-sans); font-size: 1rem; background-color: var(--background); transition: all 0.3s ease; }
.form-control:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 4px var(--accent-light); }
textarea.form-control { resize: vertical; min-height: 120px; }

.mobile-menu-btn { display: none; background: none; border: none; font-size: 1.5rem; color: var(--primary); cursor: pointer; }
"""

with open("css/style.css", "w") as f:
    f.write(css_content)

print("Updated style.css")
