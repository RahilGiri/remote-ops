import os

files_to_update = ['case-studies.html', 'industries.html', 'services.html']
for filepath in files_to_update:
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r') as f:
        content = f.read()
        
    content = content.replace(
        '<section class="section-surface" style="padding-top: 0;">\n            <div class="container pull-up',
        '<section class="section-surface">\n            <div class="container'
    )
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Pull-up reverted")
