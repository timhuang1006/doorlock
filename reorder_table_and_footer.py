"""
更新比較表格和頁尾
1. 將「智能聯網電子鎖」欄位移到第一欄
2. 移除「24H客服」
3. 移除頁尾的「BECK」
"""
import re

# 讀取HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. 更新比較表格
# 定義新的表格內容 (智能聯網電子鎖移到第一欄，移除24H客服)
new_table_content = '''
                <table class="comparison-table">
                    <thead>
                        <tr>
                            <th class="feature-col">功能項目</th>
                            <th class="our-product-col sticky-col">
                                <div class="best-choice-badge">最佳選擇</div>
                                智能聯網電子鎖
                            </th>
                            <th class="competitor-col">S牌</th>
                            <th class="competitor-col">P牌</th>
                            <th class="competitor-col">M牌</th>
                            <th class="competitor-col">A牌</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="feature-name"><i class="fas fa-tags"></i> 價格區間</td>
                            <td class="our-product-val highlight-text sticky-col">超高 CP 值</td>
                            <td class="competitor-val">$25,000+</td>
                            <td class="competitor-val">$28,000+</td>
                            <td class="competitor-val">$15,000+</td>
                            <td class="competitor-val">$20,000+</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-unlock-alt"></i> 開鎖方式</td>
                            <td class="our-product-val sticky-col">10 種全能解鎖</td>
                            <td class="competitor-val">5 種</td>
                            <td class="competitor-val">5 種</td>
                            <td class="competitor-val">6 種</td>
                            <td class="competitor-val">6 種</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-video"></i> 視訊對講</td>
                            <td class="our-product-val sticky-col">標配 遠端視訊</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="competitor-val text-muted">選配</td>
                            <td class="competitor-val text-muted">選配</td>
                            <td class="competitor-val text-muted">無</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-camera"></i> 貓眼鏡頭</td>
                            <td class="our-product-val sticky-col">F1.8 超廣角鏡頭</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="competitor-val text-muted">無</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-tv"></i> 室內螢幕</td>
                            <td class="our-product-val sticky-col">4吋 高清大螢幕</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="competitor-val text-muted">無</td>
                            <td class="competitor-val text-muted">無</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-mobile-alt"></i> APP 功能</td>
                            <td class="our-product-val sticky-col">遠端開門 + 監控</td>
                            <td class="competitor-val">基礎</td>
                            <td class="competitor-val">基礎</td>
                            <td class="competitor-val">基礎</td>
                            <td class="competitor-val">基礎</td>
                        </tr>
                        <tr>
                            <td class="feature-name"><i class="fas fa-tools"></i> 售後服務</td>
                            <td class="our-product-val sticky-col">只換不修</td>
                            <td class="competitor-val">送回原廠維修</td>
                            <td class="competitor-val">送回原廠維修</td>
                            <td class="competitor-val">送回原廠維修</td>
                            <td class="competitor-val">送回原廠維修</td>
                        </tr>
                    </tbody>
                </table>
'''

# 替換舊表格
pattern_table = r'<table class="comparison-table">.*?</table>'
html = re.sub(pattern_table, new_table_content, html, flags=re.DOTALL)

# 2. 更新頁尾 (移除 BECK)
# 尋找 Copyright 行
pattern_footer = r'Copyright © 2025 BECK\. All Rights Reserved\.'
html = re.sub(pattern_footer, 'Copyright © 2025. All Rights Reserved.', html)

# 寫回
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated comparison table layout and footer text")
