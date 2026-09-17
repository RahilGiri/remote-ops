import os

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()

            # Fix banner link color
            old_link = 'style="color: var(--primary); text-decoration: underline; margin-left: 0.5rem;"'
            new_link = 'style="color: white; font-weight: 700; text-decoration: underline; margin-left: 0.5rem;"'
            content = content.replace(old_link, new_link)
            
            # Make the banner flex so it wraps nicely on mobile
            old_banner = 'class="top-banner" style="background: var(--primary); color: white; text-align: center; padding: 0.5rem; font-size: 0.875rem;"'
            new_banner = 'class="top-banner" style="background: var(--primary); color: white; text-align: center; padding: 0.5rem 1rem; font-size: 0.875rem; display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 0.25rem;"'
            content = content.replace(old_banner, new_banner)

            with open(filepath, 'w') as f:
                f.write(content)

print("Banner fixed globally!")
