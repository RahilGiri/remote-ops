import os
import re

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html") and ("services/" in root or "industries/" in root or file == "about.html" or file == "how-it-works.html"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()

            # Pattern to match the pull-up card with the blurred background
            # <div class="card" style="padding: 0; ...">
            #   <div style="position: relative; width: 100%; height: 450px; overflow: hidden; background: #0f172a;">
            #       <img src="IMG_URL" ...>
            #       <img src="IMG_URL" ...>
            #   </div>
            #   <div style="padding: 4rem;">
            #       TEXT CONTENT
            #   </div>
            # </div>
            
            pattern = re.compile(
                r'<div class="card" style="padding: 0; overflow: hidden; border: none; box-shadow: 0 30px 60px rgba\(0,0,0,0\.08\);">\s*<div style="position: relative; width: 100%; height: 450px; overflow: hidden; background: #0f172a;">\s*<img src="([^"]+)"[^>]+>\s*<img src="[^"]+"[^>]+>\s*</div>\s*<div style="padding: 4rem;">(.*?)</div>\s*</div>',
                re.DOTALL
            )
            
            def replacer(match):
                img_url = match.group(1)
                text_content = match.group(2)
                
                # In about.html and how-it-works, we might want a simple single column text, or a grid-2
                # But grid-2 always works.
                return f"""<div class="card" style="padding: 4rem; border: none; box-shadow: 0 30px 60px rgba(0,0,0,0.08);">
                    <div class="grid-2" style="align-items: center; gap: 4rem;">
                        <div>
                            {text_content}
                        </div>
                        <div>
                            <div style="border-radius: 16px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                                <img src="{img_url}" style="width: 100%; height: auto; display: block;" alt="Service Image">
                            </div>
                        </div>
                    </div>
                </div>"""

            new_content = pattern.sub(replacer, content)

            with open(filepath, 'w') as f:
                f.write(new_content)

print("Pull-up layout fixed globally!")
