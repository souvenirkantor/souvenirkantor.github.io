import os
import re

dir_path = r'c:\Users\Administrator\Downloads\souvenirkantor.github.io-main\souvenirkantor.github.io-main'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Domain replace
    content = content.replace('https://corporategifts.biz.id', 'https://hampersmalang.web.id')

    # 2. Defer Scripts
    content = content.replace('<script src="assets/vendor/', '<script defer src="assets/vendor/')
    content = content.replace('<script src="assets/js/', '<script defer src="assets/js/')
    # Prevent double defer if script is run twice
    content = content.replace('<script defer defer src=', '<script defer src=')

    # 3. Favicons replace
    favicon_pattern = re.compile(r'<!-- Favicons -->\s*<link[^>]+icon[^>]+>\s*<link[^>]+apple-touch-icon[^>]+>', re.IGNORECASE)
    new_favicons = """<!-- Favicons -->
    <link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon/favicon-2.png">
    <link rel="icon" type="image/png" sizes="16x16" href="assets/img/favicon/favicon-2.png">
    <link rel="apple-touch-icon" sizes="180x180" href="assets/img/favicon/favicon-2.png">
    <meta name="theme-color" content="#ffffff">"""
    
    if favicon_pattern.search(content):
        content = favicon_pattern.sub(new_favicons, content)
    
    # 4. OpenGraph and Twitter
    if 'og:locale' not in content:
        # Extract title, desc, image
        title_match = re.search(r'<meta\s+property="og:title"\s+content="([^"]+)"\s*/>', content)
        desc_match = re.search(r'<meta\s+property="og:description"\s+content="([^"]+)"\s*/>', content)
        img_match = re.search(r'<meta\s+property="og:image"\s+content="([^"]+)"\s*/>', content)

        if title_match and desc_match and img_match:
            t = title_match.group(1)
            d = desc_match.group(1)
            i = img_match.group(1)

            extra_meta = f"""<meta property="og:site_name" content="MerchHub Souvenir" />
    <meta property="og:locale" content="id_ID" />
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{t}" />
    <meta name="twitter:description" content="{d}" />
    <meta name="twitter:image" content="{i}" />"""
            
            # Insert after og:image:height if exists, else after og:image
            height_match = re.search(r'<meta\s+property="og:image:height"\s+content="[^"]+"\s*/>', content)
            if height_match:
                content = content[:height_match.end()] + "\n    " + extra_meta + content[height_match.end():]
            else:
                content = content[:img_match.end()] + "\n    " + extra_meta + content[img_match.end():]

    # 5. PageSpeed - Preconnect / DNS Prefetch
    if '<link rel="dns-prefetch" href="//fonts.googleapis.com">' not in content:
        # Add dns-prefetch before fonts preconnect
        content = content.replace('<!-- Fonts -->', '<!-- PageSpeed Opt -->\n    <link rel="dns-prefetch" href="//fonts.googleapis.com">\n    <!-- Fonts -->')
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

modified_count = 0
for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        if process_file(filepath):
            modified_count += 1
            print(f"Modified: {filename}")

print(f"Total files modified: {modified_count}")
