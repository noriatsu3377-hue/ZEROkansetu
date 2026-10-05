import re

def update_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Meta / OGP / Viewport
    content = content.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    )
    content = content.replace(
        '<meta name="description" content="評価から技術選択、症例対応まで。つま先から顎、頭部まで全身の関節調整を体系的に学ぶ、零式－関節調整法BASIC＋ADVANCE全4日間講座。">',
        '<meta name="description" content="海外で体系化された関節調整を、日本人の体格・骨の強さ・生活動作に合わせて再構築。評価から技術選択、症例対応まで全身の関節調整を学ぶ全4日間講座。">'
    )
    content = content.replace(
        '<meta property="og:description" content="評価から技術選択、症例対応まで。全身の関節調整を体系的に学ぶ全4日間講座。">',
        '<meta property="og:description" content="海外で体系化された関節調整を、日本人の体格・骨の強さ・生活動作に合わせて再構築。評価から技術選択、症例対応まで全身の関節調整を学ぶ全4日間講座。">'
    )
    content = content.replace(
        '<meta property="og:url" content="">',
        '<meta property="og:url" content="<!-- 【要入力：サイトのURL】 -->">'
    )
    content = content.replace(
        '<meta property="og:image" content="">',
        '<meta property="og:image" content="<!-- 【要入力：OGP画像URL】images/founder.jpg -->">'
    )

    # First view Hero
    content = content.replace(
        '<p class="hero-subtitle">つま先から顎、頭部まで<br>全身の関節を読み解き<br>評価、技術、臨床判断を4日間でつなぐ</p>',
        '<p class="hero-subtitle">つま先から顎、頭部まで<br>全身の関節を読み解き<br>評価、技術、臨床判断を4日間でつなぐ<br>体格・骨の強さ・生活動作に合わせて、必要最小限の刺激で変化を導く</p>'
    )
    
    content = content.replace(
        '<p class="hero-catchcopy">\n                        ただ鳴らす技術ではない<br>',
        '<p class="hero-catchcopy">\n                        <span style="display:block; font-size:1.2em; font-weight:bold; margin-bottom:0.5em;">海外の技術を、日本人の身体へ。</span><br>\n                        ただ鳴らす技術ではない<br>'
    )
    
    # 2. Section number for "FOR JAPANESE BODIES"
    # Locate the section
    old_section_header = """<div class="diff-intro text-center">
                    <h2 class="diff-intro-title mask-reveal"><span>その関節調整、本当に目の前の日本人の身体に合っていますか？</span></h2>"""
    new_section_header = """<div class="section-header">
                    <span class="section-num">03</span>
                    <h2 class="section-title">その関節調整、本当に目の前の日本人の身体に合っていますか？</h2>
                    <p class="section-title-en">FOR JAPANESE BODIES</p>
                </div>
                <div class="diff-intro text-center">"""
    
    # Replacing the h2 in diff-intro with a standard section header
    # Let's use regex for precision
    content = re.sub(
        r'<div class="diff-intro text-center">\s*<h2 class="diff-intro-title mask-reveal"><span>その関節調整、本当に目の前の日本人の身体に合っていますか？</span></h2>',
        new_section_header,
        content
    )

    # 3. "海外の技術を、日本人の身体と臨床現場へ。" modifications
    content = content.replace(
        '<li>日本人施術者と受講者の体格差</li>',
        '<li>施術者と受け手の体格差</li>'
    )
    
    new_diff_block = """
                <!-- 新規追加：日本人の身体に合わせて -->
                <div class="diff-japanese-adapt mt-12 fade-up-text">
                    <h3 class="diff-sub-title">日本人の身体に合わせて、零式が変える5つのこと</h3>
                    <div class="diff-card">
                        <ul class="diff-list">
                            <li>
                                <strong>1. 刺激量｜骨の強さを考える</strong><br>
                                閉経後の女性、高齢者、痩せ型の方など、骨が弱くなっている可能性を事前に確認し、スラストを使うか、低負荷の調整や運動に切り替えるかを判断します。
                            </li>
                            <li class="mt-4">
                                <strong>2. ポジションとテコ｜体格に合わせる</strong><br>
                                海外の手技は大柄な施術者・受け手を前提に作られたものも少なくありません。施術者と受け手の体格差に合わせて、立ち位置、テーブルの高さ、テコの長さ、体重の乗せ方を変えます。
                            </li>
                            <li class="mt-4">
                                <strong>3. 評価動作｜日本の生活動作で見る</strong><br>
                                スクワットや歩行に加え、正座、あぐら、しゃがみ、床からの立ち上がりなど、日本の生活で実際に使う動作で評価・再評価します。
                            </li>
                            <li class="mt-4">
                                <strong>4. 部位の特徴｜日本の臨床で多いケースを知る</strong><br>
                                寛骨臼形成不全、内側型の変形性膝関節症、デスクワークやスマートフォン使用による胸椎・頸部の負担など、日本の臨床現場で出会う機会が多い状態を踏まえて評価します。
                            </li>
                            <li class="mt-4">
                                <strong>5. 説明と同意｜刺激への不安に配慮する</strong><br>
                                強い刺激への不安や、痛みを言い出しにくい方にも配慮し、何をするか・なぜ行うか・音が鳴る可能性を事前に説明し、同意を得てから行います。
                            </li>
                        </ul>
                    </div>
                </div>
                """
                
    content = content.replace(
        '<!-- 5. 比較表 -->',
        new_diff_block + '\n                <!-- 5. 比較表 -->'
    )

    # 4. BASIC Curriculum Buttons
    content = content.replace(
        '<a href="#" class="apply-btn dynamic-application-basic">BASIC単体で申し込む</a>',
        '<a href="<!-- 【要入力：申込URL】 -->#" class="apply-btn dynamic-application-basic">BASIC単体で申し込む</a>'
    )
    content = content.replace(
        '<a href="#" class="apply-btn dynamic-application-set">BASIC＋ADVANCE セットで申し込む</a>',
        '<a href="<!-- 【要入力：申込URL】 -->#" class="apply-btn dynamic-application-set">BASIC＋ADVANCE セットで申し込む</a>'
    )
    content = content.replace(
        '<a href="#" class="apply-btn dynamic-application-advance">ADVANCE単体で申し込む<br>',
        '<a href="<!-- 【要入力：申込URL】 -->#" class="apply-btn dynamic-application-advance">ADVANCE単体で申し込む<br>'
    )

    # 5. ADVANCE Curriculum changes
    content = content.replace(
        '<p class="curriculum-intro">\n                    関節を動かす技術から',
        '<p class="curriculum-intro">\n                    ADVANCEでは、BASICで身につけた技術を、日本人の体格・骨の強さ・可動性・生活動作・刺激への感受性に合わせて組み替えます。集団の傾向を知った上で、目の前の一人を評価して技術を選びます。<br><br>\n                    関節を動かす技術から'
    )
    
    # 5-2. Timeline additions
    content = content.replace(
        '<li>局所だけでなく全身から捉える / 調整前後で必ず変化を確認する理由</li>\n                            </ul>',
        '<li>局所だけでなく全身から捉える / 調整前後で必ず変化を確認する理由</li>\n                                <li>日本人の体格・生活背景から身体を読む視点 / 集団の傾向と個人差の扱い方</li>\n                            </ul>'
    )
    content = content.replace(
        '<li>痛みの原因関節を絞り込む / 一つの結果で決めつけない評価法</li>\n                            </ul>',
        '<li>痛みの原因関節を絞り込む / 一つの結果で決めつけない評価法</li>\n                                <li>日本の生活動作を使った評価（しゃがみ・正座・あぐら・床からの立ち上がり）</li>\n                            </ul>'
    )
    content = content.replace(
        '<li>施術中・後に異変が出た場合の対応</li>\n                            </ul>',
        '<li>施術中・後に異変が出た場合の対応</li>\n                                <li>骨脆弱性のスクリーニング（閉経後女性・高齢者・痩せ型・ステロイド使用歴）</li>\n                                <li>強い刺激に不安がある方への説明と同意 / 痛みを言い出しにくい方への確認方法</li>\n                            </ul>'
    )
    content = content.replace(
        '<li>膝関節の回旋評価 / 伸展制限と屈曲制限の鑑別 / 膝痛に対し足・股関節から介入する判断</li>\n                            </ul>',
        '<li>膝関節の回旋評価 / 伸展制限と屈曲制限の鑑別 / 膝痛に対し足・股関節から介入する判断</li>\n                                <li>裸足・床生活と足趾機能 / 浮き指・外反母趾への考え方</li>\n                                <li>内側型の変形性膝関節症を考慮した評価と調整 / しゃがみ・正座での膝屈曲評価</li>\n                            </ul>'
    )
    content = content.replace(
        '<li>腰痛に対して股関節から介入するケース / 股関節痛に対して足部・骨盤から介入するケース</li>\n                            </ul>',
        '<li>腰痛に対して股関節から介入するケース / 股関節痛に対して足部・骨盤から介入するケース</li>\n                                <li>寛骨臼形成不全を考慮した股関節の評価と牽引時の注意</li>\n                                <li>正座・あぐら・横座りの習慣と股関節回旋の左右差</li>\n                            </ul>'
    )
    content = content.replace(
        '<li>どこから調整を始めるか / 複数箇所を調整しすぎない考え方</li>\n                            </ul>',
        '<li>どこから調整を始めるか / 複数箇所を調整しすぎない考え方</li>\n                                <li>床からの立ち上がり動作を使った下肢〜体幹の再評価</li>\n                            </ul>'
    )
    content = content.replace(
        '<li>力ではなく方向と固定で調整する / 音を目的にしない調整法</li>\n                            </ul>',
        '<li>力ではなく方向と固定で調整する / 音を目的にしない調整法</li>\n                                <li>体格差に合わせたポジション変更（小柄な施術者が大柄な方を扱う場合／その逆）/ テーブルの高さとテコの長さの調整</li>\n                            </ul>'
    )
    content = content.replace(
        '<li>頸部痛・肩痛に対する胸郭からの介入 / 座位・背・腹臥位の術式選択</li>\n                            </ul>',
        '<li>頸部痛・肩痛に対する胸郭からの介入 / 座位・背・腹臥位の術式選択</li>\n                                <li>長時間座位・デスクワークによる胸椎伸展制限への介入</li>\n                                <li>骨脆弱性が疑われる方の胸腰部にスラストを使わない調整法</li>\n                            </ul>'
    )
    content = content.replace(
        '<li>握力低下と手関節可動性 / 肘痛・手首痛への肩甲帯からの介入</li>\n                            </ul>',
        '<li>握力低下と手関節可動性 / 肘痛・手首痛への肩甲帯からの介入</li>\n                                <li>パソコン・スマートフォン操作による手指・前腕・肘への負担の評価</li>\n                            </ul>'
    )
    content = content.replace(
        '<li>頸椎への直接的なスラストを避ける判断 / 胸郭から頸部を変化させる方法</li>\n                            </ul>',
        '<li>頸椎への直接的なスラストを避ける判断 / 胸郭から頸部を変化させる方法</li>\n                                <li>スマートフォン使用・頭部前方位と上位頸椎への負担の評価</li>\n                            </ul>'
    )
    content = content.replace(
        '<li>食いしばり・開口制限への考え方 / 顎→頸椎→胸郭の連動</li>\n                            </ul>',
        '<li>食いしばり・開口制限への考え方 / 顎→頸椎→胸郭の連動</li>\n                                <li>食いしばり・歯ぎしりと日中の姿勢・作業習慣の関係</li>\n                            </ul>'
    )
    content = content.replace(
        '（例）足関節背屈制限を伴う膝痛、胸椎制限を伴う肩痛、全身に複数の制限があるケース等<br>',
        '（例）足関節背屈制限を伴う膝痛、胸椎制限を伴う肩痛、全身に複数の制限があるケース等<br>\n                            （日本の臨床で多い例）デスクワークによる肩・頸部痛、床からの立ち上がりが困難な膝痛、骨粗鬆症リスクがある方の腰背部痛でスラストを使わず改善を図るケース<br>'
    )
    
    # ADVANCE Table row addition
    content = content.replace(
        '<tr><td>手技中心</td><td>評価・推論・再評価中心</td></tr>',
        '<tr><td>手技中心</td><td>評価・推論・再評価中心</td></tr>\n                            <tr><td>基本の型を正確に覚える</td><td>日本人の体格・骨の強さ・生活動作に合わせて組み替える</td></tr>'
    )

    # 6. Transformation
    content = content.replace(
        '<span class="step-label">STEP 1</span>\n                        <h4>知る</h4>',
        '<span class="step-label">STEP 1</span>\n                        <h4>知る</h4>\n                        <p style="font-size: 0.85rem; margin-top:0.5rem;">関節の構造・動き・禁忌を、技術を使う根拠として理解する</p>'
    )
    content = content.replace(
        '<span class="step-label">STEP 2</span>\n                        <h4>触れる</h4>',
        '<span class="step-label">STEP 2</span>\n                        <h4>触れる</h4>\n                        <p style="font-size: 0.85rem; margin-top:0.5rem;">骨指標と関節の遊びを、正確に触って感じ取る</p>'
    )
    content = content.replace(
        '<span class="step-label">STEP 3</span>\n                        <h4>安全に行う</h4>',
        '<span class="step-label">STEP 3</span>\n                        <h4>安全に行う</h4>\n                        <p style="font-size: 0.85rem; margin-top:0.5rem;">スクリーニングと同意を経て、必要最小限の刺激で調整する</p>'
    )
    content = content.replace(
        '<span class="step-label">STEP 4</span>\n                        <h4>評価する</h4>',
        '<span class="step-label">STEP 4</span>\n                        <h4>評価する</h4>\n                        <p style="font-size: 0.85rem; margin-top:0.5rem;">日本の生活動作も使い、調整前の基準をつくる</p>'
    )
    content = content.replace(
        '<span class="step-label">STEP 5</span>\n                        <h4>選択する</h4>',
        '<span class="step-label">STEP 5</span>\n                        <h4>選択する</h4>\n                        <p style="font-size: 0.85rem; margin-top:0.5rem;">体格・骨の強さ・症状に合わせて、触る関節と技術を選ぶ</p>'
    )
    content = content.replace(
        '<span class="step-label">STEP 6</span>\n                        <h4>組み合わせる</h4>',
        '<span class="step-label">STEP 6</span>\n                        <h4>組み合わせる</h4>\n                        <p style="font-size: 0.85rem; margin-top:0.5rem;">全身の連動から、調整の順序と運動を組み立てる</p>'
    )
    content = content.replace(
        '<span class="step-label">STEP 7</span>\n                        <h4>再評価する</h4>',
        '<span class="step-label">STEP 7</span>\n                        <h4>再評価する</h4>\n                        <p style="font-size: 0.85rem; margin-top:0.5rem;">同じ条件で変化を確認し、次の一手を決める</p>'
    )

    # 7. Target Audience Section (New)
    target_section = """
        <!-- Section 7: Target Audience (New) -->
        <section class="target-section reveal light-section" id="target">
            <div class="container">
                <div class="section-header">
                    <span class="section-num">07</span>
                    <h2 class="section-title">こんな方におすすめ／おすすめしない方</h2>
                    <p class="section-title-en">TARGET AUDIENCE</p>
                </div>
                
                <div class="diff-card highlight-card mt-8">
                    <h3 class="diff-sub-title text-accent">おすすめの方</h3>
                    <ul class="diff-list mt-4">
                        <li>海外の関節調整を学んだが、日本人のクライアントにそのまま使いにくいと感じている方</li>
                        <li>小柄な体格で、大柄な方への手技に苦労している方</li>
                        <li>高齢者や女性のクライアントが多く、安全な刺激量を知りたい方</li>
                        <li>施術とトレーニングをつなげて、変化を定着させたい方</li>
                        <li>評価から再評価まで、自分の施術を説明できるようになりたい方</li>
                    </ul>
                </div>
                
                <div class="diff-card mt-8">
                    <h3 class="diff-sub-title">おすすめしない方</h3>
                    <ul class="diff-list mt-4">
                        <li>関節を鳴らす技術だけを短時間で覚えたい方</li>
                        <li>評価や安全管理を省いて、手技の数だけを増やしたい方</li>
                    </ul>
                </div>
            </div>
        </section>
"""
    content = content.replace(
        '<!-- Section 9: Instructor -->',
        target_section + '\n        <!-- Section 8: Instructor -->'
    )
    
    # 8. Instructor Section & Renumbering
    # Renumbering
    content = content.replace('<span class="section-num">07</span>\n                    <h2 class="section-title">講師紹介</h2>', '<span class="section-num">08</span>\n                    <h2 class="section-title">講師紹介</h2>')
    content = content.replace('<span class="section-num">08</span>\n                    <h2 class="section-title">受講費用</h2>', '<span class="section-num">09</span>\n                    <h2 class="section-title">受講費用</h2>')
    content = content.replace('<span class="section-num">09</span>\n                    <h2 class="section-title">開催概要</h2>', '<span class="section-num">10</span>\n                    <h2 class="section-title">開催概要</h2>')
    content = content.replace('<span class="section-num">10</span>\n                    <h2 class="section-title">安全な受講のために</h2>', '<span class="section-num">11</span>\n                    <h2 class="section-title">安全な受講のために</h2>')
    content = content.replace('<span class="section-num">11</span>\n                    <h2 class="section-title">よくある質問</h2>', '<span class="section-num">12</span>\n                    <h2 class="section-title">よくある質問</h2>')
    
    # Instructor Text Changes
    content = content.replace('<li>オステオパシー修了書</li>', '<li>オステオパシー修了証</li>')
    content = content.replace(
        'パーソナルトレーニング、企業研修、国内外での講師活動を展開する。\n                        </p>',
        'パーソナルトレーニング、企業研修、国内外での講師活動を展開する。<br>\n                            12年以上、日本人の身体に向き合う中で、海外で学んだ技術をそのまま使うのではなく、体格や生活背景に合わせて組み替える必要性を感じ、零式－関節調整法を体系化しました。\n                        </p>\n                        <p class="instructor-stats mt-4" style="font-weight:600; color:var(--c-accent);"><!-- 【要入力：これまでの施術・指導実績（人数など）】 -->【要入力：これまでの施術・指導実績（人数など）】</p>'
    )

    # 9. Information Placeholders
    content = content.replace(
        '<p class="dynamic-venue">東京</p>',
        '<p class="dynamic-venue"><!-- 【要入力：会場詳細】 -->東京（詳細は申込者へご案内いたします）</p>'
    )
    content = content.replace(
        '<p class="dynamic-capacity">12名の少人数制</p>',
        '<p class="dynamic-capacity"><!-- 【要確認：定員（8名 or 12名）】 -->12名の少人数制</p>'
    )
    
    # 10. Safety
    content = content.replace(
        '<li>本講座には関節のスラスト技術（音を伴う手技）が含まれます。</li>',
        '<li>本講座には関節のスラスト技術（音を伴う手技）が含まれます。</li>\n                        <li>頸椎への急激な回旋・伸展を伴うスラストは、厚生労働省の注意喚起に基づき講座範囲外としています。</li>'
    )
    
    # 11. FAQ Placeholders & New QAs
    content = content.replace(
        '<div class="faq-answer"><p>運営へお問い合わせください。</p></div>',
        '<div class="faq-answer"><p><!-- 【要入力：回答文を入力してください】 -->運営へお問い合わせください。</p></div>'
    )
    
    new_faqs = """
                    <div class="faq-item">
                        <button class="faq-question">「日本人に合わせた関節調整」とは、具体的に何が違うのですか？</button>
                        <div class="faq-answer"><p>技術そのものを否定するのではなく、刺激量、ポジション、テコの長さ、評価に使う動作を、日本人の体格・骨の強さ・生活動作に合わせて変えます。ただし日本人を一括りにはせず、必ず目の前の一人を評価して判断します。</p></div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-question">力が弱くても（小柄でも）できますか？</button>
                        <div class="faq-answer"><p>はい。零式は力ではなく、方向と固定で調整することを重視しています。ADVANCEでは体格差に合わせたポジションの変え方も扱います。</p></div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-question">スラストに抵抗がある方でも受講できますか？</button>
                        <div class="faq-answer"><p>はい。スラストを使わない判断と、モビライゼーションや運動への切り替えも講座で学びます。実技で受け手になる際に不安がある場合は、事前に講師へお伝えください。</p></div>
                    </div>
    """
    
    content = content.replace(
        '<!-- FAQ Items -->',
        '<!-- FAQ Items -->\n' + new_faqs
    )
    
    # 12. Final CTA
    content = content.replace(
        '<h2 class="final-cta-title">技術を増やすだけで終わるのか。<br>身体を読み、選び、使える臨床家へ進むのか。</h2>',
        '<h2 class="final-cta-title">技術を増やすだけで終わるのか。<br>身体を読み、選び、使える臨床家へ進むのか。</h2>\n                <p class="final-cta-catch mt-4" style="font-size:1.2rem; font-weight:600;">海外の技術を、日本人の身体で使える技術へ。</p>'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_html('/Users/user/Desktop/零式-関節調整法LP/index.html')
