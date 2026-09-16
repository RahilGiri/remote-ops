import os
import re

# Premium Image Mapping
new_images = {
    # Homepage Main Hero - Abstract/Data (instead of standard building)
    'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab': 'https://images.unsplash.com/photo-1573164713988-8665fc963095', # Actually, 1573164713988 is a beautiful skyscraper. Let's use 1600596542815 for home.
    
    # Let's just do a mass replace of the specific Unsplash IDs with better ones
    # Dashboard -> Clean abstract stats or high-end dashboard
    '1551288049-bebda4e38f71': '1551288049-bebda4e38f71', # Keep this, it's good
    
    # Strategy -> Abstract network / tech
    '1552664730-d307ca884978': '1504384308090-c894fdcc538d', 
    
    # Meeting -> High-end boardroom
    '1557804506-669a67965ba0': '1497366216548-37526070297c',
    
    # Email -> Clean workspace
    '1516321318423-f06f85e504b3': '1499951360447-b19be8fe80f5',
    
    # Social Media -> Abstract liquid/color
    '1611162617474-5b21e879e113': '1618005182384-a83a8bd57fbe',
    
    # Real Estate -> Modern mansion
    '1512917774080-9991f1c4c750': '1600596542815-ffad4c1539a9',
    
    # Case study 1 (meeting)
    '1556761175-5973dc0f32e7': '1556761175-5973dc0f32e7', # keep
    
    # Case study 3 (instagram) -> abstract tech
    '1611162616305-c69b3fa7fbe0': '1558655146-d493478cb2c5'
}

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Replace images
    for old_id, new_id in new_images.items():
        content = content.replace(old_id, new_id)
        
    # Inject <span class="tag">Overview</span> into subpage heroes if not present
    # Matches <div class="container text-center reveal fade-in">\n                <h1>
    if '<div class="container text-center reveal fade-in">' in content:
        if '<span class="tag">Overview</span>' not in content:
            content = content.replace(
                '<div class="container text-center reveal fade-in">\n                <h1>',
                '<div class="container text-center reveal fade-in">\n                <span class="tag" style="margin-bottom: 2rem;">Overview</span>\n                <h1>'
            )
            
    with open(filepath, 'w') as f:
        f.write(content)

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            process_file(os.path.join(root, file))

print("Premium upgrades applied!")
