import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS definition to add if not exists
css_included = """
.included-items {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
    padding: 2rem;
    max-width: 800px;
    margin: 2rem auto 0;
}
.included-title {
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
    text-align: center;
    color: var(--c-white-1);
    border-bottom: 1px solid rgba(255,255,255,0.1);
    padding-bottom: 1rem;
}
.included-list {
    list-style: none;
    padding: 0;
    text-align: left;
}
.included-list li {
    font-size: 0.95rem;
    margin-bottom: 0.8rem;
    padding-left: 1.5rem;
    position: relative;
    color: var(--c-gray-1);
}
.included-list li::before {
    content: '✓';
    position: absolute;
    left: 0;
    top: 0;
    color: var(--c-accent);
    font-weight: bold;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_included)


# SET List
set_list = """                <div class="included-items">
                    <h4 class="included-title">受講料に含まれるもの</h4>
                    <ul class="included-list">
                        <li>BASICコース全2日間・ADVANCEコース全2日間の講義および実技指導</li>
                        <li>各コースのオリジナルテキスト・講義資料</li>
                        <li>受講者限定の復習動画（BASIC）</li>
                        <li>全身の評価・臨床推論・症例別調整プログラム構築指導（ADVANCE）</li>
                        <li>実技チェック</li>
                        <li>零式－関節調整法 BASIC課程修了証・修了証番号の発行</li>
                        <li>零式－関節調整法 ADVANCE課程修了証の発行</li>
                        <li>零式公式サイトの修了者名簿への掲載</li>
                        <li>修了者限定のロゴ・表記使用権（※使用規定は別途設定）</li>
                        <li>再受講制度の対象</li>
                    </ul>
                </div>"""

# ADVANCE List
adv_list = """                <div class="included-items">
                    <h4 class="included-title">受講料に含まれるもの</h4>
                    <ul class="included-list">
                        <li>全2日間の講義・実技指導</li>
                        <li>ADVANCE専用オリジナルテキスト・講義資料</li>
                        <li>全身の評価・臨床推論・症例別調整プログラム構築指導</li>
                        <li>実技チェック</li>
                        <li>零式－関節調整法 ADVANCE課程修了証の発行</li>
                        <li>零式公式サイトの修了者名簿への掲載</li>
                        <li>修了者限定のロゴ・表記使用権（※使用規定は別途設定）</li>
                        <li>再受講制度の対象</li>
                    </ul>
                </div>"""

# BASIC List
basic_list = """                <div class="included-items">
                    <h4 class="included-title">受講料に含まれるもの</h4>
                    <ul class="included-list">
                        <li>全2日間（合計12時間）の講義・実技指導</li>
                        <li>BASIC専用オリジナルテキスト</li>
                        <li>受講者限定の復習動画</li>
                        <li>実技チェック</li>
                        <li>零式－関節調整法 BASIC課程修了証・修了証番号の発行</li>
                        <li>零式公式サイトの修了者名簿への掲載</li>
                        <li>再受講制度の対象</li>
                    </ul>
                </div>"""

# Update SET Title to include note
html = re.sub(
    r'<h3 class="pricing-category-title">【推奨】BASIC＋ADVANCE 全4日間セット</h3>',
    r'<h3 class="pricing-category-title">【推奨】BASIC＋ADVANCE 全4日間セット</h3>\n                <p class="pricing-note">※「一般再受講」「MEMBERS再受講」は、過去にBASIC・ADVANCEの両方を修了した方が、全4日間を再受講する場合の価格です。</p>',
    html
)

# Insert SET List
html = re.sub(
    r'(<div class="price-header">MEMBERS再受講</div>\s*<div class="price-amount">165,000<span class="currency">円</span><span class="tax">（税込）</span></div>\s*</div>\s*</div>)',
    r'\1\n' + set_list,
    html
)

# Insert ADVANCE List
html = re.sub(
    r'(<div class="price-header">MEMBERS再受講</div>\s*<div class="price-amount">99,000<span class="currency">円</span><span class="tax">（税込）</span></div>\s*</div>\s*</div>)',
    r'\1\n' + adv_list,
    html
)

# Insert BASIC List
html = re.sub(
    r'(<div class="price-header">MEMBERS再受講</div>\s*<div class="price-amount">82,500<span class="currency">円</span><span class="tax">（税込）</span></div>\s*</div>\s*</div>)',
    r'\1\n' + basic_list,
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

