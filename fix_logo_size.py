import os

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()

            # Fix header logo
            # Old: style="height: 48px; width: auto;"
            # New: style="height: 140px; width: auto; margin: -46px -30px;"
            content = content.replace(
                'style="height: 48px; width: auto;"', 
                'style="height: 140px; width: auto; margin: -46px -20px; mix-blend-mode: multiply;"'
            )
            
            # Fix footer logo
            # Old: style="height: 40px; width: auto; display: block;"
            # New: style="height: 120px; width: auto; display: block; margin: -40px -20px; mix-blend-mode: multiply;"
            content = content.replace(
                'style="height: 40px; width: auto; display: block;"',
                'style="height: 120px; width: auto; display: block; margin: -40px -20px;"'
            )
            
            # Also footer logo container needs to hide overflow if we are scaling it out
            content = content.replace(
                'display: inline-block;">',
                'display: inline-block; overflow: hidden; height: 50px; width: 180px; display: flex; align-items: center; justify-content: center;">'
            )

            with open(filepath, 'w') as f:
                f.write(content)

print("Logo size increased globally!")
