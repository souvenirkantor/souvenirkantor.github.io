import re
from datetime import datetime

# Read a base template article
with open("jasa-hampers-kantor-malang.html", "r", encoding="utf-8") as f:
    template = f.read()

# Details for the new article
title = "Hampers Kantor Custom Logo Perusahaan di Malang"
description = "Hampers kantor custom logo membantu memperkuat identitas brand perusahaan setiap kali hampers diterima. Proses custom logo mencakup posisi, teknik, dan warna."
keywords = "Hampers Kantor Custom Logo, Hampers Korporat Malang, Souvenir Perusahaan Custom, Branding Hampers Kantor"
url_slug = "hampers-kantor-custom-logo-perusahaan-di-malang"
hero_img = "assets/img/blog/Corporate-gift-box-in-modern-boardroom.webp"
date_str_iso = datetime.now().strftime("%Y-%m-%d")
date_str_display = f"{datetime.now().day} {datetime.now().strftime('%B')} {datetime.now().year}" 

# Replace metadata
template = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', template, flags=re.DOTALL)
template = re.sub(r'<meta name="description"\s*content=".*?">', f'<meta name="description" content="{description}">', template, flags=re.DOTALL)
template = re.sub(r'<meta name="keywords"\s*content=".*?">', f'<meta name="keywords" content="{keywords}">', template, flags=re.DOTALL)
template = re.sub(r'<link rel="canonical" href=".*?" />', f'<link rel="canonical" href="https://corporategifts.biz.id/{url_slug}" />', template)
template = re.sub(r'<meta property="og:url"\s*content=".*?" />', f'<meta property="og:url" content="https://corporategifts.biz.id/{url_slug}" />', template)
template = re.sub(r'<meta property="og:title"\s*content=".*?" />', f'<meta property="og:title" content="{title}" />', template)
template = re.sub(r'<meta property="og:description"\s*content=".*?" />', f'<meta property="og:description" content="{description}" />', template)
template = re.sub(r'<meta property="og:image"\s*content=".*?" />', f'<meta property="og:image" content="https://corporategifts.biz.id/{hero_img}" />', template)
template = re.sub(r'<meta property="og:image:secure_url"\s*content=".*?" />', f'<meta property="og:image:secure_url" content="https://corporategifts.biz.id/{hero_img}" />', template)
template = re.sub(r'<meta property="og:image:alt"\s*content=".*?" />', f'<meta property="og:image:alt" content="{title}" />', template)
template = re.sub(r'<meta name="twitter:title"\s*content=".*?" />', f'<meta name="twitter:title" content="{title}" />', template)
template = re.sub(r'<meta name="twitter:description"\s*content=".*?" />', f'<meta name="twitter:description" content="{description}" />', template)
template = re.sub(r'<meta name="twitter:image"\s*content=".*?" />', f'<meta name="twitter:image" content="https://corporategifts.biz.id/{hero_img}" />', template)

# Replace the hero image ONLY ONCE to avoid destroying body images later
template = re.sub(r'<figure class="post-cover">\s*<img src=".*?"', f'<figure class="post-cover">\n      <img src="{hero_img}"', template, count=1)

# JSON-LD replace
json_ld_new = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Article",
      "@id": "https://corporategifts.biz.id/{url_slug}",
      "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "https://corporategifts.biz.id/{url_slug}"
      }},
      "headline": "{title}",
      "description": "{description}",
      "image": "https://corporategifts.biz.id/{hero_img}",
      "author": {{
        "@type": "Person",
        "name": "Nayla Putri",
        "url": "https://corporategifts.biz.id/profil/nayla-putri",
        "image": "https://corporategifts.biz.id/assets/img/person/nayla-putri.webp"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Pusat Souvenir & Merchandise Kantor",
        "url": "https://corporategifts.biz.id",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://corporategifts.biz.id/assets/img/favicon/favicon-1.png",
          "width": 250,
          "height": 60
        }}
      }},
      "datePublished": "{date_str_iso}",
      "dateModified": "{date_str_iso}",
      "articleSection": "Souvenir & Corporate Gifts",
      "keywords": [
        "Hampers Kantor Custom Logo",
        "Hampers Korporat Malang",
        "Souvenir Perusahaan Custom",
        "Branding Hampers Kantor"
      ],
      "inLanguage": "id-ID",
      "url": "https://corporategifts.biz.id/{url_slug}"
    }},
    {{
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "Apa itu hampers kantor custom logo?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Hampers kantor custom logo adalah hampers korporat yang disertai pencetakan logo perusahaan pada kemasan maupun produk di dalamnya."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Di bagian mana saja logo perusahaan bisa dicetak?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Logo dapat dicetak pada kemasan luar, label produk, kartu ucapan, maupun produk fungsional di dalam hampers."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Apa manfaat utama custom logo pada hampers kantor?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Custom logo membantu memperkuat brand recall dan mencerminkan profesionalisme perusahaan kepada penerima hampers."
          }}
        }}
      ]
    }}
  ]
}}
</script>"""

template = re.sub(
    r'<script type="application/ld\+json">.*?</script>',
    json_ld_new,
    template,
    flags=re.DOTALL
)

new_content = f"""
    <!-- ✅ Poin Penting -->
    <blockquote class="highlight-quote">
      <p><b>Poin Penting:</b></p>
      <ul>
        <li>Custom logo dapat diterapkan pada kemasan, kartu ucapan, atau produk di dalam hampers.</li>
        <li>Proses custom logo mencakup desain, teknik cetak, dan penyesuaian warna brand.</li>
        <li>Custom logo memperkuat brand recall dan kesan profesional perusahaan.</li>
        <li>Pemilihan teknik cetak disesuaikan dengan material produk dan kemasan.</li>
        <li>corporategifts.biz.id menyediakan layanan hampers custom logo untuk perusahaan di Malang.</li>
      </ul>
    </blockquote>

    <!-- ✅ Daftar Isi -->
    <aside class="post-toc">
      <h3 id="toc-toggle">
        Daftar Isi
        <span class="toggle-icon">▼</span>
      </h3>
      <ul id="toc-list"></ul>
    </aside>

    <h2 id="apa-itu">Apa Itu Hampers Kantor Custom Logo?</h2>
    <p>Hampers kantor custom logo merujuk pada hampers yang dirancang dengan menyertakan elemen visual identitas perusahaan, seperti logo, warna brand, atau tagline, pada bagian kemasan maupun produk. Elemen ini membedakan hampers korporat dari hampers pada umumnya karena secara langsung merepresentasikan perusahaan pengirim.</p>
    
    <h2 id="bagian-cetak">Bagian Mana Saja yang Bisa Dicetak Logo?</h2>
    <p>Logo perusahaan dapat diaplikasikan pada berbagai bagian hampers, mulai dari box kemasan luar, label produk, kartu ucapan, hingga produk fungsional seperti tumbler atau notebook yang berada di dalam hampers. Setiap bagian memberikan efek branding yang berbeda tergantung tingkat visibilitas produk tersebut bagi penerima.</p>

    <h2 id="proses-pembuatan">Bagaimana Proses Pembuatan Hampers Custom Logo?</h2>
    <p>Proses pembuatan hampers custom logo umumnya melalui beberapa tahap yang saling berkaitan untuk memastikan hasil akhir sesuai identitas brand perusahaan.</p>
    
    <h3>Konsultasi Desain dan Penentuan Posisi Logo</h3>
    <p>Tahap awal mencakup diskusi mengenai file logo, warna brand, serta posisi logo yang diinginkan pada kemasan maupun produk.</p>

    <h3>Pemilihan Teknik Pencetakan</h3>
    <p>Teknik pencetakan disesuaikan dengan material yang digunakan, misalnya teknik emboss untuk material kulit atau kayu, cetak digital untuk kemasan kertas, atau laser engraving untuk produk logam.</p>
    
    <figure class="post-cover">
      <img src="assets/img/blog/Corporate-elegance-in-a-refined-office.webp" alt="Keanggunan korporat di kantor yang mewah" />
    </figure>

    <h3>Proof Desain Sebelum Produksi Massal</h3>
    <p>Sebelum produksi dalam jumlah besar dilakukan, biasanya disediakan contoh desain atau proof untuk memastikan hasil cetak logo sudah sesuai dengan ekspektasi perusahaan.</p>
    
    <h3>Produksi dan Finishing</h3>
    <p>Setelah desain disetujui, tahap produksi massal dilakukan dengan pengecekan kualitas pada setiap unit untuk menjaga konsistensi hasil cetak logo di seluruh hampers.</p>

    <div class="callout success">
      <blockquote>
        <b>Baca juga:&nbsp;<a href="peran-souvenir-dalam-branding-perusahaan.html" target="_blank">Peran Souvenir dalam Membangun Branding dan Identitas Perusahaan Modern</a></b>
      </blockquote>
    </div>

    <h2 id="manfaat">Apa Manfaat Custom Logo bagi Branding Perusahaan?</h2>
    <p>Custom logo pada hampers kantor memberikan manfaat signifikan terhadap upaya branding perusahaan. Setiap kali hampers diterima dan digunakan, logo perusahaan turut terekspos kepada penerima maupun lingkungan sekitarnya, sehingga membantu memperkuat brand recall secara berkelanjutan.</p>
    <p>Selain itu, hampers dengan custom logo turut mencerminkan tingkat profesionalisme dan perhatian terhadap detail, yang pada akhirnya memberikan kesan positif terhadap reputasi perusahaan di mata klien maupun mitra bisnis.</p>
    <p>Hampers kantor custom logo menjadi salah satu cara efektif bagi perusahaan di Malang untuk memperkuat identitas brand melalui corporate gifting. Mulai dari pemilihan posisi logo, teknik pencetakan, hingga proses produksi, setiap tahap perlu diperhatikan agar hasil akhir mencerminkan citra perusahaan secara maksimal. corporategifts.biz.id siap membantu mewujudkan hampers kantor custom logo yang profesional dan berkesan untuk perusahaan Anda di Malang.</p>

    <h2 id="faq">FAQ</h2>
    <h3>Apa itu hampers kantor custom logo?</h3>
    <p>Hampers kantor custom logo adalah hampers korporat yang disertai pencetakan logo perusahaan pada kemasan maupun produk di dalamnya.</p>

    <h3>Di bagian mana saja logo perusahaan bisa dicetak?</h3>
    <p>Logo dapat dicetak pada kemasan luar, label produk, kartu ucapan, maupun produk fungsional di dalam hampers.</p>

    <h3>Apa manfaat utama custom logo pada hampers kantor?</h3>
    <p>Custom logo membantu memperkuat brand recall dan mencerminkan profesionalisme perusahaan kepada penerima hampers.</p>
"""

# Replace the article content in the HTML
template = re.sub(
    r'(<article class="post-card">.*?</header>).*?(<div class="cta-slab">)',
    r'\g<1>\n  <div class="post-content blog">\n' + new_content + r'\n  </div>\n\g<2>',
    template,
    flags=re.DOTALL
)

# Update post-hero
template = re.sub(r'<h1 class="post-title">.*?</h1>', f'<h1 class="post-title">{title}</h1>', template)
excerpt = "Hampers kantor custom logo adalah hampers korporat yang dilengkapi dengan pencetakan logo perusahaan pada kemasan maupun produk di dalamnya. Layanan ini membantu perusahaan memperkuat identitas brand setiap kali hampers diterima oleh klien, mitra bisnis, atau karyawan."
template = re.sub(r'<p class="post-excerpt">.*?</p>', f'<p class="post-excerpt">{excerpt}</p>', template, flags=re.DOTALL)
template = re.sub(r'<time datetime=".*?">.*?</time>', f'<time datetime="{date_str_iso}">{date_str_display}</time>', template)

# Fix read time randomly to 7 mins
template = re.sub(r'<span class="dot">•</span>.*?menit baca', '<span class="dot">•</span> 7 menit baca', template)
# Fix breadcrumb
template = re.sub(r'<li class="current">.*?</li>', f'<li class="current">{title}</li>', template)


with open(f"{url_slug}.html", "w", encoding="utf-8") as f:
    f.write(template)

print(f"Created {url_slug}.html")
