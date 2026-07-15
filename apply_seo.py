import os
import re

dir_path = r'd:\souvenirkantor.github.io-main\souvenirkantor.github.io-main'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Domain replace
    content = content.replace('https://hampersmalang.web.id', 'https://corporategifts.biz.id')
    content = content.replace('https://corporataegifts.biz.id', 'https://corporategifts.biz.id')
    content = content.replace('https://corporategfts.biz.id', 'https://corporategifts.biz.id')

    # 2. Defer Scripts
    content = content.replace('<script src="assets/vendor/', '<script defer src="assets/vendor/')
    content = content.replace('<script src="assets/js/', '<script defer src="assets/js/')
    content = content.replace('<script defer defer src=', '<script defer src=')

    # 3. Favicons replace
    favicon_pattern1 = re.compile(r'<!-- Favicons -->.*?<meta name="theme-color" content="#ffffff">', re.IGNORECASE | re.DOTALL)
    favicon_pattern2 = re.compile(r'<!-- Favicons -->.*?<!-- Fonts -->', re.IGNORECASE | re.DOTALL)
    
    new_favicons = """<!-- Favicons -->
    <link rel="icon" type="image/png" sizes="32x32" href="https://corporategifts.biz.id/assets/img/favicon/favicon-2.png">
    <link rel="icon" type="image/png" sizes="16x16" href="https://corporategifts.biz.id/assets/img/favicon/favicon-2.png">
    <link rel="apple-touch-icon" sizes="180x180" href="https://corporategifts.biz.id/assets/img/favicon/favicon-2.png">
    <link rel="shortcut icon" href="https://corporategifts.biz.id/assets/img/favicon/favicon-2.png">
    <link rel="icon" type="image/x-icon" href="https://corporategifts.biz.id/assets/img/favicon/favicon-2.png">
    <meta name="theme-color" content="#ffffff">"""
    
    if favicon_pattern1.search(content):
        content = favicon_pattern1.sub(new_favicons, content)
    elif favicon_pattern2.search(content):
        content = favicon_pattern2.sub(new_favicons + "\n    <!-- Fonts -->", content)
    
    # 4. Robots & AEO/GEO
    robots_old = re.compile(r'<meta name="robots" content="[^"]+" />', re.IGNORECASE)
    robots_new = """<!-- SEO & GEO (Generative Engine Optimization) -->
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1, noarchive" />
    <meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
    <meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />"""
    
    # Clean up any existing SEO & GEO block to avoid duplication
    content = re.sub(r'<!-- SEO & GEO \(Generative Engine Optimization\) -->\s*<meta name="robots"[^>]+>\s*<meta name="googlebot"[^>]+>\s*<meta name="bingbot"[^>]+>', '', content)
    content = re.sub(r'<meta name="googlebot"[^>]+>\s*', '', content)
    content = re.sub(r'<meta name="bingbot"[^>]+>\s*', '', content)

    if robots_old.search(content):
        content = robots_old.sub(robots_new, content)
    elif '<title>' in content:
        content = content.replace('<title>', robots_new + '\n    <title>')

    # 5. OpenGraph & Twitter
    if 'og:locale' not in content:
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
            
            height_match = re.search(r'<meta\s+property="og:image:height"\s+content="[^"]+"\s*/>', content)
            if height_match:
                content = content[:height_match.end()] + "\n    " + extra_meta + content[height_match.end():]
            else:
                content = content[:img_match.end()] + "\n    " + extra_meta + content[img_match.end():]

    # 6. PageSpeed Opt
    if '<!-- PageSpeed Opt -->' not in content:
        ps_opt = """<!-- PageSpeed Opt -->
    <link rel="dns-prefetch" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>"""
        if '<!-- Fonts -->' in content:
            content = content.replace('<!-- Fonts -->', ps_opt + '\n    <!-- Fonts -->')
    else:
        # If PageSpeed Opt exists, make sure preconnect is there
        if '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' not in content:
            content = content.replace('<link rel="dns-prefetch" href="https://fonts.googleapis.com">', '<link rel="dns-prefetch" href="https://fonts.googleapis.com">\n    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

modified_count = 0
for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        try:
            if process_file(filepath):
                modified_count += 1
                # print(f"Modified: {filename}")
        except Exception as e:
            print(f"Error on {filename}: {e}")

print(f"Total files modified: {modified_count}")
