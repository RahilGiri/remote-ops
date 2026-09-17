import os

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
                
            if 'background: #0f172a;' not in content:
                continue

            # Manually split and replace
            parts = content.split('<div class="card" style="padding: 0; overflow: hidden; border: none; box-shadow: 0 30px 60px rgba(0,0,0,0.08);">')
            if len(parts) > 1:
                new_content = parts[0]
                for part in parts[1:]:
                    if '<div style="position: relative; width: 100%; height: 450px; overflow: hidden; background: #0f172a;">' in part:
                        # Extract image url
                        img_start = part.find('<img src="') + 10
                        img_end = part.find('"', img_start)
                        img_url = part[img_start:img_end]
                        
                        # Extract text padding section
                        text_start = part.find('<div style="padding: 4rem;">') + 28
                        text_end = part.find('</div>\n                </div>', text_start)
                        
                        if text_end == -1:
                            text_end = part.find('</div>\n            </div>', text_start) # fallback
                        if text_end == -1:
                            text_end = part.find('</div>\n</div>', text_start) # fallback2
                            
                        if text_end != -1:
                            text_content = part[text_start:text_end].strip()
                            
                            replacement = f"""<div class="card" style="padding: 4rem; border: none; box-shadow: 0 30px 60px rgba(0,0,0,0.08);">
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
                            rest_of_part = part[text_end + len('</div>\n                </div>'):]
                            new_content += replacement + rest_of_part
                        else:
                            new_content += '<div class="card" style="padding: 0; overflow: hidden; border: none; box-shadow: 0 30px 60px rgba(0,0,0,0.08);">' + part
                    else:
                        new_content += '<div class="card" style="padding: 0; overflow: hidden; border: none; box-shadow: 0 30px 60px rgba(0,0,0,0.08);">' + part
                content = new_content

            with open(filepath, 'w') as f:
                f.write(content)

print("Pull-up layout fixed robustly!")
