import os
import re

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            modified = False
            
            # Fix case-studies.html images
            if "height:120px;" in content and "object-fit:cover;" in content:
                content = content.replace("height:120px;", "height:auto; aspect-ratio:16/9;")
                content = content.replace("object-fit:cover;", "object-fit:contain; background-color:#f8fafc;")
                modified = True
                
            # Fix the background div in service/industry pages
            if "background: url(" in content and "center/cover;" in content and "height: 350px;" in content:
                pattern = r'<div style="height: 350px; background: url\(\'(.*?)\'\) center/cover;"></div>'
                replacement = r'<img src="\1" style="width: 100%; height: auto; display: block;" alt="Service Image">'
                content = re.sub(pattern, replacement, content)
                modified = True
                
            # Fix about.html image
            if "height: 400px; background: url" in content:
                pattern2 = r'<div style="height: 400px; background: url\(\'(.*?)\'\) center/cover;"></div>'
                replacement2 = r'<img src="\1" style="width: 100%; height: auto; display: block;" alt="Our Story">'
                content = re.sub(pattern2, replacement2, content)
                modified = True

            if modified:
                with open(filepath, 'w') as f:
                    f.write(content)

print("Images updated to scale without cropping!")
