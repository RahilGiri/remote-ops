import re

with open('industries.html', 'r') as f:
    content = f.read()

images = {
    'Fund Managers': 'https://images.unsplash.com/photo-1579532537598-459ecdaf39cc?q=80&w=800&auto=format&fit=crop',
    'Real Estate Investment': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?q=80&w=800&auto=format&fit=crop',
    'Commercial Real Estate': 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=800&auto=format&fit=crop',
    'Leasing': 'https://images.unsplash.com/photo-1554469384-e58fac16e23a?q=80&w=800&auto=format&fit=crop',
    'Property Management': 'https://images.unsplash.com/photo-1464938050520-ef2270bb8ce8?q=80&w=800&auto=format&fit=crop',
    'Real Estate Brokers': 'https://images.unsplash.com/photo-1573164713988-8665fc963095?q=80&w=800&auto=format&fit=crop'
}

for title, url in images.items():
    img_html = f'<div style="width:100%; height:180px; border-radius:12px; overflow:hidden; margin-bottom:1.5rem;"><img src="{url}" style="width:100%; height:100%; object-fit:cover;" alt="{title}"></div>\n                        <h3 class="card-title">{title}</h3>'
    content = content.replace(f'<h3 class="card-title">{title}</h3>', img_html)

with open('industries.html', 'w') as f:
    f.write(content)

print("Industry images injected!")
