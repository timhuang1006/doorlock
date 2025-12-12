"""
移動並更新競品比較表格
1. 移除舊的比較表格
2. 在 Gallery 區塊前插入新的比較表格 (包含 S/P/M/A 牌)
"""
import re

# 讀取HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. 移除舊的比較表格
# 嘗試匹配整個section
pattern = r'<section id="comparison".*?</section>'
html = re.sub(pattern, '', html, flags=re.DOTALL)

# 2. 新的比較表格內容
new_comparison = '''
    <!-- 競品比較表格 -->
    <section id="comparison" class="comparison-section">
        <div class="container">
            <h2 class="section-title animate-on-scroll">為什麼選擇 <span class="gold-glow">智能聯網電子鎖</span>？</h2>
            <p class="section-subtitle animate-on-scroll">與市售知名品牌超級比一比</p>

            <div class="comparison-table-wrapper animate-on-scroll">
                <table class="comparison-table">
                    <thead>
                        <tr>
                            <th class="feature-col">功能項目</th>
                            <th class="competitor-col">S牌</th>
                            <th class="competitor-col">P牌</th>
                            <th class="competitor-col">M牌</th>
                            <th class="competitor-col">A牌</th>
                            <th class="our-product-col">
                                <div class="best-choice-badge">最佳選擇</div>
                                智能聯網電子鎖
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="feature-name"><i class="fas fa-tags"></i> 價格區間</td>
                            <td class="competitor-val">$25,000+</td>
                            <td class="competitor-val">$28,000+</td>
                            <td class="competitor-val">$15,000+</td>
                            <td class="competitor-val">$20,000+</td>
                            <td class="our-product-val highlight-text">超高 CP 值</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-unlock-alt"></i> 開鎖方式</td>
                            <td class="competitor-val">5 種</td>
                            <td class="competitor-val">5 種</td>
                            <td class="competitor-val">6 種</td>
                            <td class="competitor-val">6 種</td>
                            <td class="our-product-val">10 種全能解鎖</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-video"></i> 視訊對講</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="competitor-val text-muted">選配</td>
                            <td class="competitor-val text-muted">選配</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="our-product-val">標配 遠端視訊</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-camera"></i> 貓眼鏡頭</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="our-product-val">F1.8 超廣角鏡頭</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-tv"></i> 室內螢幕</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="our-product-val">4吋 高清大螢幕</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-mobile-alt"></i> APP 功能</td>
                            <td class="competitor-val">基礎</td>
                            <td class="competitor-val">基礎</td>
                            <td class="competitor-val">基礎</td>
                            <td class="competitor-val">基礎</td>
                            <td class="our-product-val">遠端開門 + 監控</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-tools"></i> 售後服務</td>
                            <td class="competitor-val">送回原廠維修</td>
                            <td class="competitor-val">送回原廠維修</td>
                            <td class="competitor-val">送回原廠維修</td>
                            <td class="competitor-val">送回原廠維修</td>
                            <td class="our-product-val">只換不修 + 24H客服</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>
'''

# 3. 在 Gallery 區塊前插入
# 找到 <section id="gallery"
if '<section id="gallery"' in html:
    html = html.replace('<section id="gallery"', new_comparison + '\n    <section id="gallery"')
else:
    print("Warning: Gallery section not found, appending to body")
    html = html.replace('</body>', new_comparison + '</body>')

# 寫回
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Moved and updated comparison table")
