import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_pricing_html = """                <!-- Section 10: Pricing -->
        <section class="pricing-section reveal light-section" id="pricing">
            <div class="container">
                <div class="section-header">
                    <span class="section-num">08</span>
                    <h2 class="section-title">受講費用</h2>
                    <p class="section-title-en">PRICE</p>
                </div>
                
                <div class="pricing-intro" style="background: rgba(142,23,27,0.05); padding: 2rem; border-left: 3px solid var(--c-accent); margin-bottom: 3rem; text-align: center;">
                    <p style="margin-bottom: 0; line-height: 1.8;">今回は零式-関節調整法の<strong>第1期開催を記念し、特別価格</strong>でご案内いたします。<br>
                    第2期以降は、講座内容およびサポート体制の拡充に伴い、受講料を改定する予定です。<br>
                    <strong>現在の価格で受講できるのは、第1期のみ</strong>となります。</p>
                </div>

                <h3 class="pricing-category-title">【推奨】BASIC＋ADVANCE 全4日間セット</h3>
                <div class="pricing-table">
                    <div class="price-card">
                        <div class="price-header">通常価格</div>
                        <div class="price-amount">330,000<span class="currency">円</span><span class="tax">（税込）</span></div>
                    </div>
                    <div class="price-card">
                        <div class="price-header">早割価格</div>
                        <div class="price-amount">275,000<span class="currency">円</span><span class="tax">（税込）</span></div>
                    </div>
                    <div class="price-card featured-price">
                        <div class="featured-badge">RECOMMEND</div>
                        <div class="price-header">ZERO MEMBERS価格</div>
                        <div class="price-amount highlight-amount">242,000<span class="currency">円</span><span class="tax">（税込）</span></div>
                        <p class="price-note">※最もお得にご受講いただけます。</p>
                    </div>
                    <div class="price-card outline-price">
                        <div class="price-header">再受講価格</div>
                        <div class="price-amount">99,000<span class="currency">円</span><span class="tax">（税込）</span></div>
                    </div>
                </div>

                <h3 class="pricing-category-title mt-8">ADVANCE単体（2日間）</h3>
                <p class="pricing-note">※ADVANCE単体での受講は、過去にBASICを受講済の方に限ります。</p>
                <div class="pricing-table">
                    <div class="price-card">
                        <div class="price-header">通常価格</div>
                        <div class="price-amount">198,000<span class="currency">円</span><span class="tax">（税込）</span></div>
                    </div>
                    <div class="price-card">
                        <div class="price-header">早割価格</div>
                        <div class="price-amount">165,000<span class="currency">円</span><span class="tax">（税込）</span></div>
                    </div>
                    <div class="price-card featured-price">
                        <div class="price-header">ZERO MEMBERS価格</div>
                        <div class="price-amount highlight-amount">143,000<span class="currency">円</span><span class="tax">（税込）</span></div>
                    </div>
                    <div class="price-card outline-price">
                        <div class="price-header">再受講価格</div>
                        <div class="price-amount">66,000<span class="currency">円</span><span class="tax">（税込）</span></div>
                    </div>
                </div>

                <h3 class="pricing-category-title mt-8">BASIC単体（2日間）</h3>
                <div class="pricing-table">
                    <div class="price-card">
                        <div class="price-header">通常価格</div>
                        <div class="price-amount">165,000<span class="currency">円</span><span class="tax">（税込）</span></div>
                    </div>
                    <div class="price-card">
                        <div class="price-header">早期申込価格</div>
                        <div class="price-amount">143,000<span class="currency">円</span><span class="tax">（税込）</span></div>
                    </div>
                    <div class="price-card featured-price">
                        <div class="price-header">ZERO MEMBERS価格</div>
                        <div class="price-amount highlight-amount">121,000<span class="currency">円</span><span class="tax">（税込）</span></div>
                    </div>
                    <div class="price-card outline-price">
                        <div class="price-header">再受講価格</div>
                        <div class="price-amount">44,000<span class="currency">円</span><span class="tax">（税込）</span></div>
                    </div>
                </div>"""

pattern = re.compile(r'                <!-- Section 10: Pricing -->.*?<div class="price-amount">33,000<span class="currency">円</span><span class="tax">（税込）</span></div>\s*</div>\s*</div>', re.DOTALL)
html = pattern.sub(new_pricing_html, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
