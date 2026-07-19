import re

# 1. Update HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_html = """        <!-- Section 5: Differentiation (replaces old About) -->
        <section class="differentiation-section reveal" id="about">
            <div class="container">
                
                <!-- 1. 問題提起 -->
                <div class="diff-intro text-center">
                    <h2 class="diff-intro-title mask-reveal"><span>その関節調整、本当に目の前の日本人の身体に合っていますか？</span></h2>
                    <div class="diff-intro-text fade-up-text">
                        <p>現在広く学ばれている関節調整法には、海外で体系化されたものが多いのが事実です。<br>それらには長い歴史があり、非常に優れた理論と技術を持っています。</p>
                        <p>しかし、学んだ「型」をそのまま全員に当てはめればよいわけではありません。<br>実際の施術現場では、体格、関節の可動性、筋緊張、生活習慣、運動経験、そして痛みへの感受性などを見極める必要があります。</p>
                        <p>大切なのは技術を覚えることではなく、<strong>目の前の身体に合わせて使い分けること</strong>です。</p>
                    </div>
                </div>

                <!-- 2. 従来の関節調整とは -->
                <div class="diff-traditional mt-12 fade-up-text">
                    <h3 class="diff-sub-title">海外で体系化されてきた、従来の関節調整</h3>
                    <div class="diff-card">
                        <ul class="diff-list">
                            <li>関節の動きや位置関係を評価する</li>
                            <li>動きが低下している方向や部位を見つける</li>
                            <li>手技によって関節へ適切な刺激を加える</li>
                            <li>本来の動きや身体全体の連動を引き出す</li>
                            <li>スラストを含め、複数の調整方法が存在する</li>
                            <li>正確な評価、適応判断、方向、接触、力加減が重要になる</li>
                        </ul>
                        <p class="mt-4">従来の技術も決して「単に音を鳴らすことが目的」ではありません。<br>強く捻る、勢いをつける、決められた型を無理に当てはめるものではなく、非常に精緻な体系を持っています。</p>
                    </div>
                </div>

                <!-- 3. 零式は何が違うのか -->
                <div class="diff-zero mt-12 fade-up-text">
                    <h3 class="diff-sub-title">零式が調整するのは、関節だけではない。</h3>
                    <div class="diff-card highlight-card">
                        <p class="diff-lead text-center"><strong>型に身体を当てはめるのではない。<br>目の前の身体に、技術を合わせていく。</strong></p>
                        <ul class="diff-list mt-6">
                            <li>足部から頭部、顎までを一つの連動として捉える</li>
                            <li>症状が出ている場所だけで原因を決めつけない</li>
                            <li>関節の硬さだけでなく、左右差や動作、姿勢、全身のつながりを確認する</li>
                            <li>同じ部位の不調でも、全員に同じ調整を行わない</li>
                            <li>必要な部位を見極め、刺激の方向・強さ・順序を変える</li>
                            <li>調整後に身体がどう変化したかを再評価する</li>
                            <li>手技の型だけではなく、評価から施術を組み立てる思考を学ぶ</li>
                        </ul>
                        <p class="mt-4 text-center text-accent">「鳴らす技術」ではなく「見極めて変化を導く技術」です。</p>
                    </div>
                </div>

                <!-- 4. 日本人に特化するとはどういうことか -->
                <div class="diff-japanese mt-12 fade-up-text">
                    <h3 class="diff-sub-title">海外の技術を、日本人の身体と臨床現場へ。</h3>
                    <div class="diff-card">
                        <p class="mb-4">日本人を一括りにするわけではありません。しかし、日本の生活環境には特有の背景があります。</p>
                        <ul class="diff-tags">
                            <li>長時間のデスクワーク</li>
                            <li>スマートフォンの長時間使用</li>
                            <li>床に座る生活習慣（正座やあぐら）</li>
                            <li>長時間の座位・通勤や立ち仕事</li>
                            <li>運動習慣の不足</li>
                            <li>日本人施術者と受講者の体格差</li>
                            <li>強い刺激に対する不安</li>
                            <li>日本の整体・トレーニング現場で求められる安全性と繊細さ</li>
                        </ul>
                        <p class="mt-6 diff-bold-text text-center">日本の生活環境で形成された身体の使い方を読み取り、<br>さらに一人ひとりの体格・可動性・緊張・既往歴に合わせて調整する。</p>
                    </div>
                </div>

                <!-- 5. 比較表 -->
                <div class="diff-comparison mt-12 fade-up-text">
                    <div class="comparison-table-wrapper">
                        <table class="comparison-table diff-table">
                            <thead>
                                <tr>
                                    <th class="table-label-col">比較項目</th>
                                    <th>型を中心にした関節調整</th>
                                    <th class="zero-col">零式－関節調整法</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="table-label-col">身体の見方</td>
                                    <td data-label="型を中心にした関節調整">症状がある関節を中心に見る</td>
                                    <td data-label="零式" class="zero-col">足部から頭部・顎まで全身の連動を見る</td>
                                </tr>
                                <tr>
                                    <td class="table-label-col">技術の選択</td>
                                    <td data-label="型を中心にした関節調整">学んだ型を基準にする</td>
                                    <td data-label="零式" class="zero-col">評価結果を基準に選択する</td>
                                </tr>
                                <tr>
                                    <td class="table-label-col">施術方法</td>
                                    <td data-label="型を中心にした関節調整">同じ部位に同じ方法を使いやすい</td>
                                    <td data-label="零式" class="zero-col">体格や可動性に合わせて変える</td>
                                </tr>
                                <tr>
                                    <td class="table-label-col">刺激量</td>
                                    <td data-label="型を中心にした関節調整">技術の形が優先されやすい</td>
                                    <td data-label="零式" class="zero-col">必要最小限の刺激を見極める</td>
                                </tr>
                                <tr>
                                    <td class="table-label-col">目的</td>
                                    <td data-label="型を中心にした関節調整">関節を調整する</td>
                                    <td data-label="零式" class="zero-col">身体全体の変化を引き出す</td>
                                </tr>
                                <tr>
                                    <td class="table-label-col">スラスト</td>
                                    <td data-label="型を中心にした関節調整">手技を成功させる意識が中心になりやすい</td>
                                    <td data-label="零式" class="zero-col">適応・方向・接触・力加減を重視する</td>
                                </tr>
                                <tr>
                                    <td class="table-label-col">評価</td>
                                    <td data-label="型を中心にした関節調整">施術前の確認が中心</td>
                                    <td data-label="零式" class="zero-col">施術前後の変化まで再評価する</td>
                                </tr>
                                <tr>
                                    <td class="table-label-col">学ぶ内容</td>
                                    <td data-label="型を中心にした関節調整">手技の再現</td>
                                    <td data-label="零式" class="zero-col">評価・判断・選択・実技を統合する</td>
                                </tr>
                                <tr>
                                    <td class="table-label-col">日本での応用</td>
                                    <td data-label="型を中心にした関節調整">海外の体系を学ぶ</td>
                                    <td data-label="零式" class="zero-col">日本の生活背景と臨床現場に合わせて再構築する</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 6. セクションの締め -->
                <div class="diff-outro mt-16 text-center fade-up-text">
                    <p class="diff-outro-text">
                        海外で生まれた技術を、そのまま繰り返すためではない。<br>
                        日本の現場で、日本人の身体を前にしたとき、本当に使える技術へ変えていく。<br><br>
                        体格も、可動性も、生活背景も、一人ひとり違う。<br>
                        だから零式は、決められた型だけで身体を見ない。<br><br>
                        評価し、見極め、選択し、最小限の刺激で変化を導く。<br>
                        それが、零式－関節調整法です。
                    </p>
                    
                    <div class="mt-8 diff-cta">
                        <p class="mb-4"><strong>手技を増やすのではなく、身体を見極める力を手に入れる。</strong></p>
                        <a href="#curriculum" class="apply-btn apply-btn--large">零式－関節調整法の詳細を見る</a>
                    </div>
                </div>
                
            </div>
        </section>"""

pattern = re.compile(r'<!-- Section 5: About -->.*?</section>', re.DOTALL)
html = pattern.sub(new_html, html, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
