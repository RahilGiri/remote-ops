import os

replacements = {
    'Part-Time': 'Part Time',
    'Full-Time': 'Full Time',
    'US-based': 'US based',
    'US-focused': 'US focused',
    'Data-driven': 'Data driven',
    'Pre-Trained': 'Pre Trained',
    'hand-holding': 'hand holding',
    'fast-paced': 'fast paced',
    '10-20': '10 to 20',
    '20-40': '20 to 40',
    'in-house': 'in house',
    'Long-term': 'Long term',
    'Month-to-month': 'Month to month',
    'Follow-up': 'Follow up',
    'Follow-ups': 'Follow ups',
    '555-0199': '555 0199',
    'CRM-focused': 'CRM focused',
    'high-value': 'high value',
    'Non-Disclosure': 'Non Disclosure',
    'Pre-trained': 'Pre trained',
    'lock-in': 'lock in',
    'part-time': 'part time',
    'full-time': 'full time',
    'Month-To-Month': 'Month To Month'
}

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            for old, new in replacements.items():
                content = content.replace(old, new)
                
            with open(filepath, 'w') as f:
                f.write(content)

print("Dashes removed from visible text!")
