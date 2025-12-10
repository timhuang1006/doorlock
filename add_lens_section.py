"""
添加光學鏡頭Tab到安全核心區塊
"""
import re

# 讀取HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. 在tabs裡添加新的「頂級光學鏡頭」tab
old_tabs = '''<div class="security-tab" onclick="switchTab(this, 'monitoring')">24H主動監控&防偽</div>'''
new_tabs = '''<div class="security-tab" onclick="switchTab(this, 'monitoring')">24H主動監控&防偽</div>
                <div class="security-tab" onclick="switchTab(this, 'optical-lens')">頂級光學鏡頭</div>'''
html = html.replace(old_tabs, new_tabs)

# 2. 添加光學鏡頭的內容區塊（在security-content-wrapper結尾前）
lens_content = '''
                <!-- 5. 頂級光學鏡頭 -->
                <div id="optical-lens" class="security-content security-content-block animate-on-scroll">
                    <!-- 左側：鏡頭分解圖 -->
                    <div class="security-left">
                        <div class="security-main-showcase lens-showcase">
                            <img src="assets/lens_exploded.png" alt="頂級光學鏡頭" class="security-main-img lens-img">
                            <p class="img-caption">AI 智能貓眼 × 鷹眼鏡頭</p>
                        </div>
                    </div>

                    <!-- 右側：功能說明 -->
                    <div class="security-right">
                        <h3 class="security-feature-title">頂級光學鏡頭</h3>
                        <p class="security-feature-subtitle">F1.8 大光圈，超廣角視野，還原真實色彩，夜間拍攝更清晰</p>

                        <div class="security-feature-list">
                            <div class="sec-feature-item">
                                <div class="sec-feature-icon"><i class="fas fa-camera"></i></div>
                                <div class="sec-feature-text">
                                    <h4>F1.8 大光圈</h4>
                                    <p>更大進光量，低光環境下也能清晰成像</p>
                                </div>
                            </div>
                            <div class="sec-feature-item">
                                <div class="sec-feature-icon"><i class="fas fa-expand-arrows-alt"></i></div>
                                <div class="sec-feature-text">
                                    <h4>超廣角視野</h4>
                                    <p>170° 超廣角鏡頭，門口動態一覽無遺</p>
                                </div>
                            </div>
                            <div class="sec-feature-item">
                                <div class="sec-feature-icon"><i class="fas fa-palette"></i></div>
                                <div class="sec-feature-text">
                                    <h4>真實色彩還原</h4>
                                    <p>高品質光學玻璃，影像不失真</p>
                                </div>
                            </div>
                            <div class="sec-feature-item">
                                <div class="sec-feature-icon"><i class="fas fa-moon"></i></div>
                                <div class="sec-feature-text">
                                    <h4>夜間更清晰</h4>
                                    <p>配合紅外補光，夜晚拍攝同樣銳利</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div><!-- /security-content-wrapper -->'''

# 找到wrapper結尾並替換
html = re.sub(r'(\s*)</div>\s*<!--\s*/security-content-wrapper\s*-->', lens_content, html, count=1)

# 如果上面的替換沒成功，嘗試另一種方式
if 'optical-lens' not in html:
    # 在monitoring區塊後添加
    html = html.replace('</div><!-- /security-content-wrapper -->', lens_content)

# 寫回
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added optical lens tab and content")
