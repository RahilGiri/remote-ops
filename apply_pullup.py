import os

files_to_update = ['case-studies.html', 'industries.html', 'services.html']
for filepath in files_to_update:
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Replace the first container after the hero
    # On these pages, it's usually <section class="section-surface">\n            <div class="container
    # Let's target exactly that.
    content = content.replace(
        '<section class="section-surface">\n            <div class="container',
        '<section class="section-surface" style="padding-top: 0;">\n            <div class="container pull-up'
    )
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Pull-up effect applied")
