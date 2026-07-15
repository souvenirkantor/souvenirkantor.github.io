import re
from datetime import datetime

# Read a base template article
with open("jasa-hampers-kantor-malang.html", "r", encoding="utf-8") as f:
    template = f.read()

# Details for the new article
title = "Harga Hampers Kantor Malang: Faktor Penentu dan Kisaran Biaya"
description = "Harga hampers kantor di Malang ditentukan oleh kombinasi jenis isi, jumlah pesanan, dan tingkat kustomisasi kemasan. Temukan kisaran biaya dan cara optimasi budget."
keywords = "Harga Hampers Kantor Malang, Biaya Hampers Corporate, Hampers Premium Malang, Souvenir Kantor Custom"
url_slug = "harga-hampers-kantor-malang-faktor-penentu-kisaran-biaya"
hero_img = "assets/img/blog/Corporate-gifts-in-modern-office-setting.webp"
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
        "Harga Hampers Kantor Malang",
        "Biaya Hampers Corporate",
        "Hampers Premium Malang",
        "Souvenir Kantor Custom"
      ],
      "inLanguage": "id-ID",
      "url": "https://corporategifts.biz.id/{url_slug}"
    }},
    {{
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "Apa faktor utama yang menentukan harga hampers kantor?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Harga hampers kantor ditentukan oleh jenis isi, material kemasan, tingkat kustomisasi logo, dan kuantitas pesanan."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Apakah harga lebih murah jika memesan dalam jumlah besar?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Umumnya ya, karena skala produksi yang lebih besar memungkinkan efisiensi harga per unit."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Apakah custom logo menambah biaya hampers kantor?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Ya, proses custom logo menambah tahap produksi sehingga umumnya memengaruhi total biaya hampers."
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
        <li>Harga hampers kantor dipengaruhi oleh isi, kuantitas, dan kustomisasi.</li>
        <li>Hampers standar dan premium memiliki rentang harga berbeda.</li>
        <li>Pemesanan dalam jumlah besar berpotensi menurunkan harga per unit.</li>
        <li>Custom logo dan kemasan eksklusif menambah komponen biaya produksi.</li>
        <li>corporategifts.biz.id menyediakan pilihan hampers sesuai budget perusahaan.</li>
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

    <h2 id="faktor-harga">Faktor Apa Saja yang Memengaruhi Harga Hampers Kantor?</h2>
    <p>Beberapa faktor utama menentukan besaran biaya hampers kantor, mulai dari jenis produk di dalamnya hingga proses kustomisasi yang dipilih perusahaan.</p>
    
    <h3>Jenis dan Jumlah Isi Hampers</h3>
    <p>Semakin banyak dan semakin berkualitas item yang ditambahkan ke dalam hampers, semakin tinggi biaya produksinya. Kombinasi makanan premium dengan produk fungsional seperti tumbler atau notebook biasanya berada pada rentang harga lebih tinggi dibanding hampers dengan isi sederhana.</p>

    <h3>Material dan Desain Kemasan</h3>
    <p>Kemasan berperan besar dalam menentukan kesan pertama penerima hampers. Material seperti kotak kayu, box premium dengan penyelesaian khusus, atau kemasan kustom yang dicetak dengan logo biasanya akan meningkatkan biaya dibandingkan dengan kemasan standar.</p>
    
    <figure class="post-cover">
      <img src="assets/img/blog/Modern-office-with-elegant-packaging-boxes.webp" alt="Kotak kemasan elegan di meja kantor modern" />
    </figure>

    <h3>Tingkat Kustomisasi Logo dan Branding</h3>
    <p>Proses custom logo, baik dicetak pada kemasan maupun diaplikasikan langsung pada produk, menambah tahap produksi tambahan yang memengaruhi total biaya.</p>
    
    <h3>Kuantitas Pesanan</h3>
    <p>Prinsip skala produksi berlaku pada hampers kantor. Pemesanan dalam jumlah besar umumnya memungkinkan negosiasi harga per unit yang lebih kompetitif dibanding pemesanan dalam jumlah kecil.</p>

    <div class="callout success">
      <blockquote>
        <b>Baca juga:&nbsp;<a href="jasa-hampers-kantor-malang.html" target="_blank">Jasa Hampers Kantor Malang: Solusi Hampers Korporat Custom Logo</a></b>
      </blockquote>
    </div>

    <h2 id="kisaran-harga">Berapa Kisaran Harga Hampers Kantor Standar hingga Premium?</h2>
    <p>Berdasarkan gambaran umum industri corporate gifting, hampers kategori standar biasanya berisi kombinasi produk fungsional dengan camilan ringan pada rentang harga menengah. Hampers kategori premium umumnya menampilkan produk pilihan seperti makanan berkualitas tinggi, aksesori kerja, hingga kemasan eksklusif dengan finishing khusus, sehingga berada pada rentang harga yang lebih tinggi dibanding kategori standar. Menurut riset ASI mengenai tren promotional products, kualitas dan personalisasi produk menjadi pertimbangan utama perusahaan dalam menentukan anggaran corporate gifting.</p>

    <h2 id="optimasi-budget">Bagaimana Cara Mengoptimalkan Budget Hampers Kantor?</h2>
    <p>Menentukan tujuan pemberian hampers sejak awal membantu perusahaan memilih kombinasi isi yang sesuai tanpa melebihi anggaran. Memesan lebih awal juga memberi ruang negosiasi dan waktu produksi yang lebih fleksibel, sehingga perusahaan dapat memperoleh harga yang lebih efisien tanpa mengorbankan kualitas.</p>
    <p>Menyesuaikan jumlah item dalam hampers dengan prioritas penerima turut membantu mengontrol biaya. Misalnya, hampers untuk klien utama dapat dibuat lebih premium, sementara hampers untuk penerima dalam jumlah besar dapat menggunakan kombinasi standar namun tetap berkualitas.</p>
    
    <h2 id="perbedaan-momen">Apakah Harga Hampers Kantor Berbeda untuk Momen Tertentu?</h2>
    <p>Momen seperti Lebaran dan akhir tahun umumnya meningkatkan permintaan hampers kantor secara signifikan. Pada periode ini, perencanaan anggaran lebih awal menjadi penting agar perusahaan tetap mendapatkan harga kompetitif meski permintaan pasar sedang tinggi.</p>
    <p>Harga hampers kantor Malang sangat dipengaruhi oleh isi, kemasan, kustomisasi, dan kuantitas pesanan. Memahami faktor-faktor ini membantu perusahaan merencanakan anggaran corporate gifting secara lebih tepat. corporategifts.biz.id menyediakan berbagai pilihan hampers kantor sesuai budget, mulai dari kategori standar hingga premium. Dapatkan penawaran harga hampers kantor terbaik untuk perusahaan Anda melalui corporategifts.biz.id.</p>

    <h2 id="faq">FAQ</h2>
    <h3>Apa faktor utama yang menentukan harga hampers kantor?</h3>
    <p>Harga hampers kantor ditentukan oleh jenis isi, material kemasan, tingkat kustomisasi logo, dan kuantitas pesanan.</p>

    <h3>Apakah harga lebih murah jika memesan dalam jumlah besar?</h3>
    <p>Umumnya ya, karena skala produksi yang lebih besar memungkinkan efisiensi harga per unit.</p>

    <h3>Apakah custom logo menambah biaya hampers kantor?</h3>
    <p>Ya, proses custom logo menambah tahap produksi sehingga umumnya memengaruhi total biaya hampers.</p>
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
excerpt = "Harga hampers kantor di Malang ditentukan oleh kombinasi jenis isi, jumlah pesanan, dan tingkat kustomisasi kemasan. Hampers kelas standar berada pada rentang harga menengah, sementara hampers premium dengan produk eksklusif dan custom logo umumnya lebih tinggi. Semakin banyak jumlah unit yang dipesan, harga per unit berpotensi lebih efisien."
template = re.sub(r'<p class="post-excerpt">.*?</p>', f'<p class="post-excerpt">{excerpt}</p>', template, flags=re.DOTALL)
template = re.sub(r'<time datetime=".*?">.*?</time>', f'<time datetime="{date_str_iso}">{date_str_display}</time>', template)
template = re.sub(r'<figure class="post-cover">\s*<img src=".*?"', f'<figure class="post-cover">\n      <img src="{hero_img}"', template)

# Fix read time randomly to 7 mins
template = re.sub(r'<span class="dot">•</span>.*?menit baca', '<span class="dot">•</span> 7 menit baca', template)
# Fix breadcrumb
template = re.sub(r'<li class="current">.*?</li>', f'<li class="current">{title}</li>', template)


with open(f"{url_slug}.html", "w", encoding="utf-8") as f:
    f.write(template)

print(f"Created {url_slug}.html")
