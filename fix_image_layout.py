import os

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()

            old_style = 'style="width: 100%; max-height: 400px; object-fit: contain; background-color: var(--surface); display: block;"'
            
            # Use object-fit: cover with a nice 400px height. It will fill the width perfectly.
            # We'll use object-position: center to keep the focal point.
            new_style = 'style="width: 100%; height: 400px; object-fit: cover; object-position: center 30%; display: block;"'
            
            content = content.replace(f'{old_style} alt="Service Image"', f'{new_style} alt="Service Image"')
            content = content.replace(f'{old_style} alt="Our Story"', f'{new_style} alt="Our Story"')

            with open(filepath, 'w') as f:
                f.write(content)

print("Images set to cover with 400px height!")
