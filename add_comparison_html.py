"""
添加競品比較表格到 index.html
"""
import re

# 讀取HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 比較表格內容
comparison_section = '''
    <!-- 競品比較表格 -->
    <section id="comparison" class="comparison-section">
        <div class="container">
            <h2 class="section-title animate-on-scroll">為什麼選擇 <span class="gold-glow">智能聯網電子鎖</span>？</h2>
            <p class="section-subtitle animate-on-scroll">與市售知名品牌熱銷款超級比一比</p>

            <div class="comparison-table-wrapper animate-on-scroll">
                <table class="comparison-table">
                    <thead>
                        <tr>
                            <th class="feature-col">功能項目</th>
                            <th class="competitor-col">知名賣場熱銷款</th>
                            <th class="our-product-col">
                                <div class="best-choice-badge">最佳選擇</div>
                                智能聯網電子鎖
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="feature-name"><i class="fas fa-tags"></i> 價格區間</td>
                            <td class="competitor-val">$20,000 起</td>
                            <td class="our-product-val highlight-text">超高 CP 值</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-unlock-alt"></i> 開鎖方式</td>
                            <td class="competitor-val">4-5 種</td>
                            <td class="our-product-val">10 種全能解鎖</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-video"></i> 視訊對講</td>
                            <td class="competitor-val text-muted">無 / 需加購</td>
                            <td class="our-product-val">標配 遠端視訊</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-camera"></i> 貓眼鏡頭</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="our-product-val">F1.8 超廣角鏡頭</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-tv"></i> 室內螢幕</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="our-product-val">4吋 高清大螢幕</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-mobile-alt"></i> APP 功能</td>
                            <td class="competitor-val">基礎功能</td>
                            <td class="our-product-val">遠端開門 + 監控</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-tools"></i> 售後服務</td>
                            <td class="competitor-val">一般安裝</td>
                            <td class="our-product-val">專業安裝 + 24H客服</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>
'''

# 在核心技術區塊後插入 (在 specs-section 之前)
if '<section id="specs"' in html:
    html = html.replace('<section id="specs"', comparison_section + '\n    <section id="specs"')
else:
    # Fallback: append to body if specs section not found (unlikely)
    html = html.replace('</body>', comparison_section + '</body>')

# 寫回
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added comparison section to index.html")
