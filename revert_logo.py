import os
import re

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()

            prefix = ""
            if "services/" in filepath or "industries/" in filepath:
                prefix = "../"

            # Fix Header
            old_header_pattern = re.compile(r'<a href="[^"]*index\.html" class="logo">.*?</a>', re.DOTALL)
            new_header_logo = f'<a href="{prefix}index.html" class="logo"><img src="{prefix}images/logo_clean.png" alt="Remote Operations Logo" style="height: 48px; width: auto; display: block;"></a>'
            content = old_header_pattern.sub(new_header_logo, content)

            # Fix Footer
            old_footer_pattern = re.compile(r'<div class="logo" style="margin-bottom: 1\.5rem; background: white; padding: 0\.5rem; border-radius: 8px; display: inline-block; overflow: hidden; height: 50px; width: 180px; display: flex; align-items: center; justify-content: center;"><img src="[^"]*images/logo\.png" alt="Remote Operations Logo" style="height: 120px; width: auto; display: block; margin: -40px -20px;"></div>', re.DOTALL)
            new_footer_logo = f'<div class="logo" style="margin-bottom: 1.5rem; background: white; padding: 0.75rem 1rem; border-radius: 8px; display: inline-block;"><img src="{prefix}images/logo_clean.png" alt="Remote Operations Logo" style="height: 40px; width: auto; display: block;"></div>'
            content = old_footer_pattern.sub(new_footer_logo, content)

            with open(filepath, 'w') as f:
                f.write(content)

print("Logo reverted to clean transparent version!")
