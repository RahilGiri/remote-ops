import os
import re

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()

            prefix = ""
            if "services/" in filepath or "industries/" in filepath:
                prefix = "../"

            # Replace title
            content = content.replace("<title>RemoteOps", "<title>Remote Operations")
            
            # Replace copyright text
            content = content.replace("RemoteOps. All rights reserved", "Remote Operations. All rights reserved")
            
            # Replace header logo
            header_logo_pattern = re.compile(r'<a href="[^"]*index\.html" class="logo">.*?</a>', re.DOTALL)
            new_header_logo = f'<a href="{prefix}index.html" class="logo"><img src="{prefix}images/logo.png" alt="Remote Operations Logo" style="height: 48px; width: auto;"></a>'
            content = header_logo_pattern.sub(new_header_logo, content)

            # Replace footer logo
            # The footer logo is inside a <div class="logo"> ... </div>
            footer_logo_pattern = re.compile(r'<div class="logo"[^>]*>.*?</div>', re.DOTALL)
            new_footer_logo = f'<div class="logo" style="margin-bottom: 1.5rem; background: white; padding: 0.5rem; border-radius: 8px; display: inline-block;"><img src="{prefix}images/logo.png" alt="Remote Operations Logo" style="height: 40px; width: auto; display: block;"></div>'
            content = footer_logo_pattern.sub(new_footer_logo, content)
            
            # Replace any other raw "RemoteOps" text with "Remote Operations"
            # But be careful not to break URLs or emails like hello@remoteops.example
            # So let's only replace "RemoteOps" if it's not inside a URL or email.
            # Easiest way: just replace "RemoteOps" -> "Remote Operations" and then fix the emails back.
            content = content.replace("RemoteOps", "Remote Operations")
            content = content.replace("remoteoperations.example", "remoteops.example") # fix email domain
            content = content.replace("Remote Operations.", "Remote Operations.")

            with open(filepath, 'w') as f:
                f.write(content)

print("Logos and company name updated globally!")
