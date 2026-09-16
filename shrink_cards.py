with open('case-studies.html', 'r') as f:
    content = f.read()

# Replace image height 180px with 120px
content = content.replace('height:180px;', 'height:120px;')

# Reduce card padding by adding inline style
content = content.replace('<div class="card reveal-item">', '<div class="card reveal-item" style="padding: 1.5rem;">')

# Make the h2 smaller
content = content.replace('<h2 class="mt-1">', '<h2 class="mt-1" style="font-size: 1.25rem; margin-bottom: 0.5rem;">')

# Make paragraphs smaller and reduce margins
content = content.replace('<p><strong>Challenge:</strong>', '<p style="font-size: 0.85rem; margin-bottom: 0.5rem; line-height: 1.4;"><strong>Challenge:</strong>')
content = content.replace('<p><strong>Support:</strong>', '<p style="font-size: 0.85rem; margin-bottom: 0.5rem; line-height: 1.4;"><strong>Support:</strong>')
content = content.replace('<p><strong>Outcome:</strong>', '<p style="font-size: 0.85rem; margin-bottom: 0; line-height: 1.4;"><strong>Outcome:</strong>')

with open('case-studies.html', 'w') as f:
    f.write(content)

print("Case studies shrunk!")
