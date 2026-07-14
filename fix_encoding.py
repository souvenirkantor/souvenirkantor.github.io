import re

with open('blog.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Fix the mojibake read-more arrow
content = re.sub(r'Baca Selengkapnya\s*[^\s\<]+', 'Baca Selengkapnya &rarr;', content)

# Check if there are any unclosed divs
# We won't do a full HTML parse, but we can make sure it looks fine.

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(content)
