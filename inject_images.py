import os
import re

def update_cards(content):
    # Mapping emoji/text to image HTML
    replacements = {
        '<div class="card-icon">📊</div>': '<div class="card-icon" style="width:100%; height:180px; background:none; border:none; border-radius:12px; overflow:hidden;"><img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=800&auto=format&fit=crop" style="width:100%; height:100%; object-fit:cover;" alt="CRM Dashboard"></div>',
        
        '<div class="card-icon">🔍</div>': '<div class="card-icon" style="width:100%; height:180px; background:none; border:none; border-radius:12px; overflow:hidden;"><img src="https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=800&auto=format&fit=crop" style="width:100%; height:100%; object-fit:cover;" alt="Strategy"></div>',
        
        '<div class="card-icon">🤝</div>': '<div class="card-icon" style="width:100%; height:180px; background:none; border:none; border-radius:12px; overflow:hidden;"><img src="https://images.unsplash.com/photo-1557804506-669a67965ba0?q=80&w=800&auto=format&fit=crop" style="width:100%; height:100%; object-fit:cover;" alt="Meeting"></div>',
        
        '<div class="card-icon">✉️</div>': '<div class="card-icon" style="width:100%; height:180px; background:none; border:none; border-radius:12px; overflow:hidden;"><img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=800&auto=format&fit=crop" style="width:100%; height:100%; object-fit:cover;" alt="Email"></div>',
        
        '<div class="card-icon">📱</div>': '<div class="card-icon" style="width:100%; height:180px; background:none; border:none; border-radius:12px; overflow:hidden;"><img src="https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=800&auto=format&fit=crop" style="width:100%; height:100%; object-fit:cover;" alt="Social Media"></div>',
        
        '<div class="card-icon">🏢</div>': '<div class="card-icon" style="width:100%; height:180px; background:none; border:none; border-radius:12px; overflow:hidden;"><img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?q=80&w=800&auto=format&fit=crop" style="width:100%; height:100%; object-fit:cover;" alt="Real Estate"></div>'
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    return content

# Update index.html
with open('index.html', 'r') as f:
    content = f.read()

content = update_cards(content)

# Add images to the VA section
va_replacements = {
    '<h3 class="card-title">Pre-Trained on Real Estate</h3>': '<div style="width:100%; height:140px; border-radius:12px; overflow:hidden; margin-bottom:1.5rem;"><img src="https://images.unsplash.com/photo-1560518883-ce09059eeffa?q=80&w=800&auto=format&fit=crop" style="width:100%; height:100%; object-fit:cover;" alt="Real Estate Docs"></div>\n                        <h3 class="card-title">Pre-Trained on Real Estate</h3>',
    
    '<h3 class="card-title">Fluent in Your Software</h3>': '<div style="width:100%; height:140px; border-radius:12px; overflow:hidden; margin-bottom:1.5rem;"><img src="https://images.unsplash.com/photo-1551434678-e076c223a692?q=80&w=800&auto=format&fit=crop" style="width:100%; height:100%; object-fit:cover;" alt="Software Screen"></div>\n                        <h3 class="card-title">Fluent in Your Software</h3>',
    
    '<h3 class="card-title">US Timezone Alignment</h3>': '<div style="width:100%; height:140px; border-radius:12px; overflow:hidden; margin-bottom:1.5rem;"><img src="https://images.unsplash.com/photo-1417733403748-83bbc7c05140?q=80&w=800&auto=format&fit=crop" style="width:100%; height:100%; object-fit:cover;" alt="Office Clock"></div>\n                        <h3 class="card-title">US Timezone Alignment</h3>'
}

for old, new in va_replacements.items():
    content = content.replace(old, new)

with open('index.html', 'w') as f:
    f.write(content)


# Update services.html
if os.path.exists('services.html'):
    with open('services.html', 'r') as f:
        content = f.read()
    content = update_cards(content)
    with open('services.html', 'w') as f:
        f.write(content)
        
print("Images injected!")
