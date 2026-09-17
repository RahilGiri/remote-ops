import os
import re

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()

            # The massive images have style="width: 100%; height: auto; display: block;"
            # We want to change them to limit their height and contain them so they don't crop.
            
            # For the banner images (which are directly inside the .card padding 0)
            old_style = 'style="width: 100%; height: auto; display: block;"'
            new_style = 'style="width: 100%; max-height: 400px; object-fit: contain; background-color: var(--surface); display: block;"'
            
            # Only replace the ones that are Service Images or Our Story
            content = content.replace(f'{old_style} alt="Service Image"', f'{new_style} alt="Service Image"')
            content = content.replace(f'{old_style} alt="Our Story"', f'{new_style} alt="Our Story"')
            
            # Case studies might also be huge? 
            # In redesign_case_studies.py I wrote:
            # <img src="..." style="width: 100%; height: 100%; object-fit: cover;" alt="Real Estate Firm Success">
            # The case study is restricted by min-height: 300px, but it's flexed by the text next to it. That's fine.

            with open(filepath, 'w') as f:
                f.write(content)

print("Massive images constrained!")
