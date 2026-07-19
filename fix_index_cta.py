with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Fixed CTA (Mobile)
html = html.replace(
    '<a href="#cta" class="apply-btn apply-btn--fixed">受講申込みはこちら</a>',
    '<a href="pricing.html" class="apply-btn apply-btn--fixed">受講費用・申込み</a>'
)

# Update Final CTA section
final_cta = """        <!-- Section 14: Final CTA -->
        <section class="final-cta-section reveal" id="cta">
            <div class="container text-center">
                <h2 class="final-cta-title">技術を増やすだけで終わるのか。<br>身体を読み、選び、使える臨床家へ進むのか。</h2>
                <p class="final-cta-subtitle">零から始める4日間</p>
                <div class="cta-group-vertical mt-8">
                    <a href="pricing.html" class="apply-btn apply-btn--large">受講費用・詳細を見る</a>
                </div>
            </div>
        </section>"""

import re
html = re.sub(r'        <!-- Section 14: Final CTA -->.*?</section>', final_cta, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
