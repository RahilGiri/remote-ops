import os
import re

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()

            # Find the existing image tag we just injected
            pattern = re.compile(r'<img src="([^"]+)" style="width: 100%; height: 400px; object-fit: cover; object-position: center 30%; display: block;" alt="(Service Image|Our Story)">')
            
            # Replace it with the premium blur backdrop container
            def replace_with_blur(match):
                img_url = match.group(1)
                alt_text = match.group(2)
                return f"""<div style="position: relative; width: 100%; height: 450px; overflow: hidden; background: #0f172a;">
    <img src="{img_url}" style="position: absolute; inset: -20px; width: calc(100% + 40px); height: calc(100% + 40px); object-fit: cover; filter: blur(25px); opacity: 0.6; pointer-events: none;" aria-hidden="true">
    <img src="{img_url}" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; padding: 2rem;" alt="{alt_text}">
</div>"""

            new_content = pattern.sub(replace_with_blur, content)

            with open(filepath, 'w') as f:
                f.write(new_content)

print("Premium blur backdrop implemented globally!")
