import os

with open('css/style.css', 'r') as f:
    css = f.read()

# 1. Glassmorphism Header
old_header = """header {
  background-color: var(--surface);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 1000;
}"""
new_header = """header {
  background-color: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(0,0,0,0.05);
  position: sticky;
  top: 0;
  z-index: 1000;
  transition: all 0.3s ease;
}"""
css = css.replace(old_header, new_header)

# 2. Hero Animated Glow
if '.hero::after' not in css:
    hero_glow = """
.hero::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 60vw;
  height: 60vw;
  background: radial-gradient(circle, rgba(37,99,235,0.15) 0%, rgba(0,0,0,0) 70%);
  transform: translate(-50%, -50%);
  pointer-events: none;
  z-index: 0;
  animation: pulse-glow 8s infinite alternate;
}
@keyframes pulse-glow {
  0% { transform: translate(-50%, -50%) scale(1); opacity: 0.5; }
  100% { transform: translate(-50%, -50%) scale(1.1); opacity: 1; }
}
"""
    css += hero_glow

# 3. Button Premium Glow Hover
old_btn_hover = """.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}"""
new_btn_hover = """.btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 25px -5px rgba(37, 99, 235, 0.25), 0 8px 10px -6px rgba(37, 99, 235, 0.1);
}"""
css = css.replace(old_btn_hover, new_btn_hover)

# 4. Enhance Card Hover to be even smoother
old_card_hover = """.card:hover { 
  box-shadow: 0 30px 60px -15px rgba(15, 23, 42, 0.15), 0 10px 20px -10px rgba(37, 99, 235, 0.1); 
  border-color: rgba(37, 99, 235, 0.3);
  transform: translateY(-10px) rotateX(2deg); 
}"""
new_card_hover = """.card:hover { 
  box-shadow: 0 40px 80px -15px rgba(15, 23, 42, 0.12), 0 15px 25px -10px rgba(37, 99, 235, 0.15); 
  border-color: rgba(37, 99, 235, 0.4);
  /* The 3D JS will handle the transform dynamically now! */
}"""
css = css.replace(old_card_hover, new_card_hover)

with open('css/style.css', 'w') as f:
    f.write(css)

print("CSS enhanced with premium effects!")
