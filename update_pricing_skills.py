with open('pricing.html', 'r') as f:
    content = f.read()

# Define the new lists
part_time_list = """<ul class="feature-list" style="margin-bottom: 2.5rem; flex-grow: 1;">
                            <li>22.5 Hours / Week (4.5 hrs/day)</li>
                            <li>Dedicated Real Estate VA</li>
                            <li>CRM & GoHighLevel Support</li>
                            <li>Lead Gen & Investor Outreach</li>
                            <li>Social Media & Marketing</li>
                            <li>US Business Hours</li>
                        </ul>"""

full_time_list = """<ul class="feature-list" style="margin-bottom: 2.5rem; flex-grow: 1;">
                            <li>45 Hours / Week (9 hrs/day)</li>
                            <li>Dedicated Real Estate VA</li>
                            <li>CRM & GoHighLevel Support</li>
                            <li>Lead Gen & Investor Outreach</li>
                            <li>Social Media & Marketing</li>
                            <li>US Business Hours</li>
                        </ul>"""

# I need to use regex or split to replace the ul blocks.
import re

# Replace Part-Time ul block
# It starts with `<ul class="feature-list" style="margin-bottom: 2.5rem; flex-grow: 1;">` and ends with `</ul>` inside the Part-Time card.
# The Part-Time card is the first one. Let's just use regex to replace all feature-lists inside the pricing cards.
# Actually, there are 3 cards. I will just split by `<ul class="feature-list" style="margin-bottom: 2.5rem; flex-grow: 1;">` and rebuild.

parts = content.split('<ul class="feature-list" style="margin-bottom: 2.5rem; flex-grow: 1;">')

# parts[1] is Part-Time list + rest of card
part_time_rest = parts[1].split('</ul>', 1)[1]
new_part_time = part_time_list + part_time_rest

# parts[2] is Full-Time list + rest of card
full_time_rest = parts[2].split('</ul>', 1)[1]
new_full_time = full_time_list + full_time_rest

# parts[3] is Growth Team list + rest of card
growth_rest = parts[3].split('</ul>', 1)[1]
growth_list = """<ul class="feature-list" style="margin-bottom: 2.5rem; flex-grow: 1;">
                            <li>Custom Hours & Team Size</li>
                            <li>Dedicated Real Estate VAs</li>
                            <li>CRM & GoHighLevel Support</li>
                            <li>Lead Gen & Investor Outreach</li>
                            <li>Social Media & Marketing</li>
                            <li>US Business Hours</li>
                        </ul>"""
new_growth = growth_list + growth_rest

new_content = parts[0] + new_part_time + new_full_time + new_growth

with open('pricing.html', 'w') as f:
    f.write(new_content)

print("Pricing skills updated")
