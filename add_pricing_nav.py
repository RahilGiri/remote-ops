import os
import re

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html") and file != "pricing.html":
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Need to handle subdirectories for the link if needed.
            # But the site seems to use relative links badly in subdirectories?
            # Wait, let's see industries.html. It just uses `href="pricing.html"`.
            # Oh, if it's in `industries/fund-managers.html`, it needs `href="../pricing.html"`.
            # Let's dynamically calculate the prefix based on directory depth.
            depth = filepath.count('/') - 1
            if filepath.startswith('./'):
                depth -= 1
                
            prefix = ""
            if "industries/" in filepath or "services/" in filepath:
                prefix = "../"
            
            pricing_link = f'<li><a href="{prefix}pricing.html">Pricing</a></li>\n                    <li><a href="{prefix}case-studies.html">Case Studies</a></li>'
            
            # Replace Case Studies with Pricing + Case Studies
            search_pattern = f'<li><a href="{prefix}case-studies.html">Case Studies</a></li>'
            
            if search_pattern in content and f'{prefix}pricing.html' not in content:
                content = content.replace(search_pattern, pricing_link)
                with open(filepath, 'w') as f:
                    f.write(content)

print("Pricing link added to nav!")
