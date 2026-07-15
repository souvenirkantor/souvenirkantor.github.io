import os
import glob
import re

def get_mini_post_html(article):
    return f"""                                <a class="mini-post"
                                    href="{article['url']}">
                                    <img src="{article['img']}"
                                        alt="{article['title']}">
                                    <div>
                                        <div class="mini-title">{article['title']}</div>
                                        <div class="mini-meta">{article['meta']}</div>
                                    </div>
                                </a>"""

def main():
    # Regex patterns to extract metadata
    title_re = re.compile(r'<h1 class="post-title">(.*?)</h1>')
    img_re = re.compile(r'<figure class="post-cover">\s*<img src="(.*?)"')
    img_fallback_re = re.compile(r'<meta property="og:image"\s*content=".*?/(assets/img/blog/.*?)"', re.DOTALL)
    date_re = re.compile(r'<time datetime=".*?">(\d+)\s+([A-Za-z]+)\s+\d{4}</time>')
    datetime_attr_re = re.compile(r'<time datetime="([^"]+)">')
    time_re = re.compile(r'(\d+)\s+menit baca')
    
    html_files = glob.glob('*.html')
    articles_data = {}
    
    # Extract metadata for all HTML files
    for f in html_files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        title_match = title_re.search(content)
        if not title_match:
            continue # Skip non-articles (like contact.html)
            
        title = title_match.group(1).strip()
        
        img_match = img_re.search(content)
        if img_match:
            img = img_match.group(1).strip()
        else:
            img_fb = img_fallback_re.search(content)
            img = img_fb.group(1).strip() if img_fb else "assets/img/blog/default.webp"
            
        date_match = date_re.search(content)
        if date_match:
            day = date_match.group(1)
            month = date_match.group(2)[:3]
            date_str = f"{day} {month}"
        else:
            date_str = "14 Jul"
            
        t_match = time_re.search(content)
        read_time = f"{t_match.group(1)} min" if t_match else "8 min"
            
        dt_match = datetime_attr_re.search(content)
        dt_str = dt_match.group(1) if dt_match else "2000-01-01"

        articles_data[f] = {
            'url': f,
            'title': title,
            'img': img,
            'meta': f"{date_str} • {read_time}",
            'datetime': dt_str
        }

    # Sort articles based on datetime (newest first).
    ordered_files = sorted(articles_data.keys(), key=lambda x: articles_data[x]['datetime'], reverse=True)
            
    print(f"Total articles found: {len(ordered_files)}")
    
    # Update HTML files
    sidebar_pattern = re.compile(
        r'<div class="widget">\s*<h3 class="widget-title">Artikel Terkait</h3>.*?</aside>',
        re.DOTALL
    )
    
    updated_files = 0
    num_articles = len(ordered_files)
    
    for f in html_files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        if not sidebar_pattern.search(content):
            continue
            
        selected_articles = []
        if f in ordered_files:
            idx = ordered_files.index(f)
            
            # Select the 3 articles published immediately before this one.
            # We use idx + 1, idx + 2, idx + 3, wrapping around if necessary.
            selected_indices = []
            for i in range(1, 4):
                next_idx = (idx + i) % num_articles
                selected_indices.append(next_idx)
                
            selected_articles = [articles_data[ordered_files[x]] for x in selected_indices]
        else:
            # For non-article pages (like index.html), just show the 3 newest articles
            if num_articles >= 3:
                selected_articles = [articles_data[ordered_files[0]], articles_data[ordered_files[1]], articles_data[ordered_files[2]]]
            
        # Generate new HTML
        mini_posts_html = "\n".join([get_mini_post_html(a) for a in selected_articles])
        
        new_widget_html = f"""<div class="widget">
                            <h3 class="widget-title">Artikel Terkait</h3>
                            <div class="mini-list">
{mini_posts_html}
                            </div>
                        </div>
                    </aside>"""
        
        new_content = sidebar_pattern.sub(new_widget_html, content)
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            updated_files += 1

    print(f"Updated sidebar in {updated_files} files.")

if __name__ == "__main__":
    main()
