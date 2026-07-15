import re
from datetime import datetime

# Read a base template article
with open("jasa-hampers-kantor-malang.html", "r", encoding="utf-8") as f:
    template = f.read()

# Details for the new article
title = "Isi Hampers Kantor untuk Klien dan Mitra Bisnis"
description = "Isi hampers kantor untuk klien umumnya terdiri dari kombinasi produk makanan premium, aksesori kerja fungsional, dan elemen branding perusahaan."
keywords = "Isi Hampers Kantor, Hampers Klien Bisnis, Corporate Gift Premium, Hampers Mitra Bisnis"
url_slug = "isi-hampers-kantor-untuk-klien-dan-mitra-bisnis"
hero_img = "assets/img/blog/Corporate-gift-box-in-modern-officeg.webp"
date_str_iso = datetime.now().strftime("%Y-%m-%d")
date_str_display = f"{datetime.now().day} {datetime.now().strftime('%B')} {datetime.now().year}" # e.g. 15 July 2026

# Replace metadata
template = re.sub(
    r'<title>.*?</title>',
    f'<title>{title}</title>',
    template,
    flags=re.DOTALL
)

template = re.sub(
    r'<meta name="description"\s*content=".*?">',
    f'<meta name="description" content="{description}">',
    template,
    flags=re.DOTALL
)

template = re.sub(
    r'<meta name="keywords"\s*content=".*?">',
    f'<meta name="keywords" content="{keywords}">',
    template,
    flags=re.DOTALL
)

template = re.sub(
    r'<link rel="canonical" href=".*?" />',
    f'<link rel="canonical" href="https://corporategifts.biz.id/{url_slug}" />',
    template
)

template = re.sub(
    r'<meta property="og:url"\s*content=".*?" />',
    f'<meta property="og:url" content="https://corporategifts.biz.id/{url_slug}" />',
    template
)

template = re.sub(
    r'<meta property="og:title"\s*content=".*?" />',
    f'<meta property="og:title" content="{title}" />',
    template
)

template = re.sub(
    r'<meta property="og:description"\s*content=".*?" />',
    f'<meta property="og:description" content="{description}" />',
    template
)

template = re.sub(
    r'<meta property="og:image"\s*content=".*?" />',
    f'<meta property="og:image" content="https://corporategifts.biz.id/{hero_img}" />',
    template
)

template = re.sub(
    r'<meta property="og:image:secure_url"\s*content=".*?" />',
    f'<meta property="og:image:secure_url" content="https://corporategifts.biz.id/{hero_img}" />',
    template
)

template = re.sub(
    r'<meta property="og:image:alt"\s*content=".*?" />',
    f'<meta property="og:image:alt" content="{title}" />',
    template
)

template = re.sub(
    r'<meta name="twitter:title"\s*content=".*?" />',
    f'<meta name="twitter:title" content="{title}" />',
    template
)

template = re.sub(
    r'<meta name="twitter:description"\s*content=".*?" />',
    f'<meta name="twitter:description" content="{description}" />',
    template
)

template = re.sub(
    r'<meta name="twitter:image"\s*content=".*?" />',
    f'<meta name="twitter:image" content="https://corporategifts.biz.id/{hero_img}" />',
    template
)

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
        "Isi Hampers Kantor",
        "Hampers Klien Bisnis",
        "Corporate Gift Premium",
        "Hampers Mitra Bisnis"
      ],
      "inLanguage": "id-ID",
      "url": "https://corporategifts.biz.id/{url_slug}"
    }},
    {{
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "Apa isi hampers kantor yang paling umum untuk klien?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Kombinasi makanan premium dan produk kerja fungsional merupakan pilihan yang paling umum digunakan untuk hampers klien."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Apakah isi hampers bisa disesuaikan dengan preferensi klien tertentu?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Ya, isi hampers dapat disesuaikan berdasarkan preferensi umum klien seperti produk sehat atau produk fungsional."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Mengapa kemasan penting dalam hampers untuk mitra bisnis?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Kemasan mencerminkan profesionalisme perusahaan pengirim dan turut memengaruhi kesan pertama penerima terhadap hampers yang diberikan."
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
        <li>Isi hampers klien biasanya mengombinasikan makanan premium dan produk fungsional.</li>
        <li>Elemen branding seperti logo dan kartu ucapan memperkuat kesan personal.</li>
        <li>Kombinasi isi disesuaikan dengan profil dan preferensi klien.</li>
        <li>Kemasan yang rapi turut memengaruhi persepsi terhadap perusahaan pengirim.</li>
        <li>corporategifts.biz.id membantu mengurasi isi hampers sesuai kebutuhan mitra bisnis Anda.</li>
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

    <h2 id="kategori-isi">Apa Saja Kategori Isi Hampers Kantor untuk Klien?</h2>
    <p>Isi hampers kantor untuk klien dapat dikelompokkan ke dalam beberapa kategori utama yang biasa dikombinasikan sesuai kebutuhan perusahaan.</p>
    
    <h3>Hampers Kategori Makanan dan Minuman Premium</h3>
    <p>Kategori ini mencakup camilan sehat, cokelat premium, kopi atau teh kemasan eksklusif, hingga produk kuliner lokal berkualitas. Kategori makanan menjadi pilihan populer karena bersifat universal dan mudah dinikmati oleh berbagai kalangan penerima.</p>

    <h3>Hampers Kategori Produk Kerja dan Aksesori</h3>
    <p>Produk seperti tumbler, notebook, pen set, hingga organizer meja kerja sering dipilih karena memberikan nilai fungsional jangka panjang. Produk kategori ini juga memberi peluang lebih besar untuk penempatan logo perusahaan secara elegan.</p>
    
    <figure class="post-cover">
      <img src="assets/img/blog/Corporate-elegance-and-city-views.webp" alt="Pemandangan kota dan keanggunan hadiah perusahaan" />
    </figure>

    <h3>Kombinasi Hampers Makanan dan Produk Kerja</h3>
    <p>Banyak perusahaan memilih kombinasi kedua kategori di atas untuk menghadirkan hampers yang lebih lengkap. Kombinasi ini memberikan kesan hampers yang lebih istimewa dibanding hanya satu kategori saja.</p>
    
    <div class="callout success">
      <blockquote>
        <b>Baca juga:&nbsp;<a href="ide-corporate-gift-indonesia-untuk-karyawan-dan-klien.html" target="_blank">Ide Corporate Gift Indonesia untuk Karyawan dan Klien</a></b>
      </blockquote>
    </div>

    <h2 id="memilih-kombinasi">Bagaimana Memilih Kombinasi Isi Hampers yang Berkesan untuk Mitra Bisnis?</h2>
    <p>Pemilihan isi hampers sebaiknya mempertimbangkan profil penerima, mulai dari posisi jabatan hingga jenis hubungan bisnis yang sedang dijalin. Hampers untuk mitra bisnis strategis umumnya menggunakan kombinasi produk yang lebih eksklusif dibanding hampers untuk penerima dalam jumlah besar.</p>
    <p>Selain itu, mempertimbangkan momen pemberian turut membantu menentukan tema isi hampers, misalnya nuansa hangat untuk momen Lebaran, atau tema formal untuk apresiasi kerja sama bisnis di akhir tahun.</p>

    <h3>Menyesuaikan Isi Hampers dengan Preferensi Klien</h3>
    <p>Beberapa perusahaan memilih untuk menyesuaikan isi hampers berdasarkan preferensi umum klien, misalnya preferensi terhadap produk sehat atau preferensi terhadap produk fungsional. Penyesuaian ini membantu memastikan hampers benar-benar relevan dan bermanfaat bagi penerima.</p>
    
    <h2 id="peran-kemasan">Apa Peran Kemasan dalam Hampers Kantor untuk Klien?</h2>
    <p>Kemasan menjadi elemen yang tidak kalah penting dibanding isi hampers itu sendiri. Kemasan yang rapi dengan sentuhan elemen branding perusahaan mencerminkan tingkat profesionalisme pengirim. Kartu ucapan yang bersifat personal dapat memberikan kesan hangat tambahan pada hampers yang diterima oleh klien atau mitra bisnis.</p>
    <p>Kemasan yang dirancang dengan baik juga meningkatkan pengalaman unboxing, yang pada akhirnya memperkuat kesan positif terhadap perusahaan pengirim di mata penerima.</p>
    <p>Isi hampers kantor untuk klien dan mitra bisnis sebaiknya dipilih dengan mempertimbangkan kombinasi produk, elemen branding, serta preferensi penerima. Kombinasi yang tepat mampu memperkuat kesan profesional sekaligus mempererat hubungan bisnis jangka panjang. Jika perusahaan Anda membutuhkan bantuan mengurasi isi hampers yang sesuai kebutuhan, corporategifts.biz.id siap membantu mewujudkan hampers kantor yang berkesan bagi klien dan mitra bisnis Anda.</p>

    <h2 id="faq">FAQ</h2>
    <h3>Apa isi hampers kantor yang paling umum untuk klien?</h3>
    <p>Kombinasi makanan premium dan produk kerja fungsional merupakan pilihan yang paling umum digunakan untuk hampers klien.</p>

    <h3>Apakah isi hampers bisa disesuaikan dengan preferensi klien tertentu?</h3>
    <p>Ya, isi hampers dapat disesuaikan berdasarkan preferensi umum klien seperti produk sehat atau produk fungsional.</p>

    <h3>Mengapa kemasan penting dalam hampers untuk mitra bisnis?</h3>
    <p>Kemasan mencerminkan profesionalisme perusahaan pengirim dan turut memengaruhi kesan pertama penerima terhadap hampers yang diberikan.</p>
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
excerpt = "Isi hampers kantor untuk klien umumnya terdiri dari kombinasi produk makanan premium, aksesori kerja fungsional, dan elemen branding perusahaan seperti kartu ucapan bertanda tangan atau logo custom. Kombinasi ini dipilih untuk mencerminkan profesionalisme sekaligus memberikan kesan personal kepada penerima."
template = re.sub(r'<p class="post-excerpt">.*?</p>', f'<p class="post-excerpt">{excerpt}</p>', template, flags=re.DOTALL)
template = re.sub(r'<time datetime=".*?">.*?</time>', f'<time datetime="{date_str_iso}">{date_str_display}</time>', template)

# Fix read time randomly to 7 mins
template = re.sub(r'<span class="dot">•</span>.*?menit baca', '<span class="dot">•</span> 7 menit baca', template)
# Fix breadcrumb
template = re.sub(r'<li class="current">.*?</li>', f'<li class="current">{title}</li>', template)


with open(f"{url_slug}.html", "w", encoding="utf-8") as f:
    f.write(template)

print(f"Created {url_slug}.html")
