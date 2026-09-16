import re

with open('case-studies.html', 'r') as f:
    content = f.read()

images = {
    'Case Study 1': 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?q=80&w=800&auto=format&fit=crop', # meeting/handshake
    'Case Study 2': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800&auto=format&fit=crop', # dashboard
    'Case Study 3': 'https://images.unsplash.com/photo-1611162616305-c69b3fa7fbe0?q=80&w=800&auto=format&fit=crop', # instagram/social
    'Case Study 4': 'https://images.unsplash.com/photo-1563986768494-4dee2763ff3f?q=80&w=800&auto=format&fit=crop' # email/laptop
}

for title, url in images.items():
    search_str = f'<h3 style="color: var(--accent); font-size: 1rem; text-transform: uppercase; letter-spacing: 0.05em;">{title}</h3>'
    img_html = f'<div style="width:100%; height:200px; border-radius:12px; overflow:hidden; margin-bottom:1.5rem;"><img src="{url}" style="width:100%; height:100%; object-fit:cover;" alt="{title}"></div>\n                        {search_str}'
    content = content.replace(search_str, img_html)

with open('case-studies.html', 'w') as f:
    f.write(content)

print("Case study images injected!")
