import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract header boilerplate (everything up to <main>)
header_match = re.search(r'(.*?<main class="site-main">)', html, re.DOTALL)
header_boilerplate = header_match.group(1) if header_match else ""

# Extract footer boilerplate (everything from <footer> to end)
footer_match = re.search(r'(<footer class="site-footer">.*)', html, re.DOTALL)
footer_boilerplate = footer_match.group(1) if footer_match else ""

# Extract pricing section
pricing_match = re.search(r'(<!-- Section 10: Pricing -->\s*<section class="pricing-section.*?</section>)', html, re.DOTALL)
if not pricing_match:
    print("Could not find pricing section")
    exit(1)

pricing_section = pricing_match.group(1)

# Modify pricing_section slightly to add a back button or CTA
pricing_page_content = f"""
{header_boilerplate}
    <!-- Subpage Header -->
    <header class="subpage-header text-center" style="padding: 6rem 0 2rem;">
        <div class="container">
            <h1 style="font-family: var(--font-serif); font-size: 2rem; color: var(--c-white-1);">受講費用・コース詳細</h1>
            <p style="color: var(--c-accent); font-size: 0.9rem; letter-spacing: 0.1em; margin-top: 0.5rem;">PRICING & DETAILS</p>
        </div>
    </header>

{pricing_section}

    <!-- CTA Section for Pricing Page -->
    <section class="final-cta-section reveal" style="padding-top: 2rem; padding-bottom: 6rem;">
        <div class="container text-center">
            <h2 class="final-cta-title">受講のお申し込み</h2>
            <div class="cta-group-vertical mt-8">
                <a href="#" class="apply-btn apply-btn--large dynamic-application-set">【推奨】全4日間セットに申し込む</a>
                <div class="cta-group-sub">
                    <a href="#" class="apply-btn dynamic-application-basic">BASIC単体に申し込む</a>
                    <a href="#" class="apply-btn dynamic-application-advance">ADVANCE単体に申し込む<br><span style="font-size: 0.75rem; letter-spacing: 0.05em;">（※過去にBASICを受講済の方）</span></a>
                </div>
            </div>
            
            <div style="margin-top: 4rem;">
                <a href="index.html" style="color: var(--c-gray-1); text-decoration: underline; font-size: 0.9rem;">トップページへ戻る</a>
            </div>
        </div>
    </section>
{footer_boilerplate}
"""

# Now write pricing.html
with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(pricing_page_content)

# Now replace the pricing section in index.html with a slim version
slim_pricing = """        <!-- Section 10: Pricing Link -->
        <section class="pricing-section reveal light-section" id="pricing">
            <div class="container text-center">
                <div class="section-header">
                    <span class="section-num">08</span>
                    <h2 class="section-title">受講費用</h2>
                    <p class="section-title-en">PRICE</p>
                </div>
                
                <div style="max-width: 600px; margin: 0 auto 3rem;">
                    <p style="margin-bottom: 1rem;">各コースの受講料、および再受講価格、受講料に含まれる教材や実技指導の内容については、詳細ページにてご確認ください。</p>
                    <p style="color: var(--c-accent); font-size: 0.9rem;">※現在、第1期開催記念の特別価格でご案内中です。</p>
                </div>
                
                <a href="pricing.html" class="apply-btn apply-btn--large" style="display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;">受講費用・コース詳細を見る <span style="font-size: 1.2rem;">→</span></a>
            </div>
        </section>"""

new_html = html.replace(pricing_section, slim_pricing)

# Also update the final CTA on index.html to point to pricing.html, or leave it as forms?
# The user said: "The bottom CTA still has application buttons. If pricing is separate, usually you view pricing then apply."
# The final CTA in index.html is Section 14. We should probably keep it pointing to the application forms, but maybe add a note "受講費用をご確認の上、お申し込みください".
# Actually, let's change the final CTA buttons in index.html to just go to pricing.html, or keep them as dynamic forms?
# I'll keep them as dynamic forms but maybe it's better to just direct them to pricing?
# Let's change the "【推奨】全4日間セットに申し込む" in index.html to link to the form, since `script.js` injects the URL. That's fine.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Split complete")
