import re
import os

clean_widget = """<div class="widget">
                            <h3 class="widget-title">Artikel Terkait</h3>
                            <div class="mini-list">
                                <a class="mini-post"
                                    href="biaya-dan-budgeting-corporate-gift-indonesia.html">
                                    <img src="assets/img/blog/Corporate-gifting-budget-workspace-setup.webp"
                                        alt="Biaya dan Budgeting Corporate Gift Indonesia">
                                    <div>
                                        <div class="mini-title">Biaya dan Budgeting Corporate Gift Indonesia</div>
                                        <div class="mini-meta">15 Jul • 8 min</div>
                                    </div>
                                </a>
                                <a class="mini-post"
                                    href="ide-corporate-gift-indonesia-untuk-karyawan-dan-klien.html">
                                    <img src="assets/img/blog/Business-gift-exchange-in-a-modern-office.webp"
                                        alt="Ide Corporate Gift Indonesia untuk Karyawan dan Klien">
                                    <div>
                                        <div class="mini-title">Ide Corporate Gift Indonesia untuk Karyawan dan Klien</div>
                                        <div class="mini-meta">14 Jul • 8 min</div>
                                    </div>
                                </a>
                                <a class="mini-post"
                                    href="cara-memilih-corporate-gift-indonesia-untuk-klien.html">
                                    <img src="assets/img/blog/Corporate-gift-set-on-desk.webp"
                                        alt="Cara Memilih Corporate Gift Indonesia untuk Klien">
                                    <div>
                                        <div class="mini-title">Cara Memilih Corporate Gift Indonesia untuk Klien</div>
                                        <div class="mini-meta">13 Jul • 8 min</div>
                                    </div>
                                </a>
                            </div>
                        </div>"""

articles = [
    'biaya-dan-budgeting-corporate-gift-indonesia.html',
    'ide-corporate-gift-indonesia-untuk-karyawan-dan-klien.html',
    'cara-memilih-corporate-gift-indonesia-untuk-klien.html',
    'corporate-gift-indonesia-panduan-lengkap.html',
    'kesalahan-umum-memilih-corporate-gifts-dan-cara-menghindarinya.html',
    'ide-corporate-gifts-untuk-karyawan-manfaat-dan-rekomendasi.html',
    'cara-memilih-corporate-gifts-untuk-klien-perusahaan.html',
    'panduan-lengkap-memilih-corporate-gifts-berkesan.html',
    'rekomendasi-souvenir-bem-fungsional-peserta-event-kampus.html',
    'ragam-souvenir-bem-untuk-branding-organisasi.html'
]

for article in articles:
    if os.path.exists(article):
        with open(article, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to match the widget containing Artikel Terkait and everything up to </aside>
        match = re.search(r'<div class="widget">\s*<h3 class="widget-title">Artikel Terkait</h3>.*?</aside>', content, re.DOTALL)
        if match:
            # Replace the entire widget with the clean one, keeping the </aside>
            new_content = content[:match.start()] + clean_widget + "\n                    </aside>" + content[match.end():]
            with open(article, 'w', encoding='utf-8') as f:
                f.write(new_content)
