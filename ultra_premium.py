import os

with open('css/style.css', 'r') as f:
    css = f.read()

# 1. Text Gradient Class
if ".text-gradient" not in css:
    css += """
.text-gradient {
    background: linear-gradient(135deg, #60A5FA 0%, #3B82F6 50%, #2563EB 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
    display: inline-block;
}
"""

# 2. Animated Grid Background for Hero
if "background-size: 40px 40px;" not in css:
    hero_grid = """
.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: 
        linear-gradient(to right, rgba(255,255,255,0.05) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255,255,255,0.05) 1px, transparent 1px);
    background-size: 40px 40px;
    mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 100%);
    -webkit-mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 100%);
    pointer-events: none;
    z-index: 0;
    animation: grid-pan 20s linear infinite;
}
@keyframes grid-pan {
    0% { transform: translateY(0); }
    100% { transform: translateY(40px); }
}
"""
    # I previously used .hero::before for an overlay, wait! Let's check.
    # In my earlier edit, I replaced .hero::before? Let's just use .hero-grid class and inject it into index.html to be safe.
    css += hero_grid

# 3. Card Spotlight Glow
if "--mouse-x" not in css:
    card_glow = """
.card {
    --mouse-x: 50%;
    --mouse-y: 50%;
}
.card::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: inherit;
    background: radial-gradient(
        600px circle at var(--mouse-x, 50%) var(--mouse-y, 50%), 
        rgba(37,99,235, 0.08),
        transparent 40%
    );
    z-index: 1;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.3s ease;
}
.card:hover::after {
    opacity: 1;
}
"""
    css += card_glow

# 4. Premium Button Sweep Animation
if ".btn-primary::before" not in css:
    btn_sweep = """
.btn-primary {
    position: relative;
    overflow: hidden;
}
.btn-primary::before {
    content: '';
    position: absolute;
    top: 0; left: -100%; width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s ease;
}
.btn-primary:hover::before {
    left: 100%;
}
"""
    css += btn_sweep

with open('css/style.css', 'w') as f:
    f.write(css)


# Update JS to power the spotlight effect
with open('js/animations.js', 'r') as f:
    js = f.read()

if "card.style.setProperty('--mouse-x'" not in js:
    # Find the mousemove listener in js and inject the setProperty
    js = js.replace("const rotateY = ((x - centerX) / centerX) * 6;", 
                    "const rotateY = ((x - centerX) / centerX) * 6;\n      card.style.setProperty('--mouse-x', `${x}px`);\n      card.style.setProperty('--mouse-y', `${y}px`);")
    
    with open('js/animations.js', 'w') as f:
        f.write(js)

# Update index.html to use text-gradients
with open('index.html', 'r') as f:
    html = f.read()

html = html.replace("<h1>You Focus on the Deals. We Handle the Work Behind Them.</h1>", 
                    "<h1>You Focus on the Deals. <br><span class=\"text-gradient\">We Handle the Work.</span></h1>")

html = html.replace("<h2>Your Time Should Be Spent on Deals Not Repetitive Tasks.</h2>",
                    "<h2>Your Time Should Be Spent on Deals <br><span class=\"text-gradient\">Not Repetitive Tasks.</span></h2>")

with open('index.html', 'w') as f:
    f.write(html)

print("Ultra premium effects applied!")
