"""
在頂級光學鏡頭卡片中添加鏡頭分解圖
"""
import re

# 讀取HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 舊的lens-card
old_lens = '''<!-- 右上：頂級光學鏡頭 -->
                <div class="tech-card lens-card animate-on-scroll" data-delay="100">
                    <div class="tech-icon"><i class="fas fa-camera-retro"></i></div>
                    <h3>頂級光學鏡頭</h3>
                    <p>F1.8 大光圈，超廣角視野，還原真實色彩，夜間拍攝更清晰</p>
                </div>'''

# 新的lens-card（包含圖片）
new_lens = '''<!-- 右上：頂級光學鏡頭 -->
                <div class="tech-card lens-card animate-on-scroll" data-delay="100">
                    <div class="lens-image-container">
                        <img src="assets/lens_exploded.png" alt="頂級光學鏡頭分解圖" class="lens-exploded-img">
                    </div>
                    <div class="lens-text-overlay">
                        <div class="tech-icon"><i class="fas fa-camera-retro"></i></div>
                        <h3>頂級光學鏡頭</h3>
                        <p>F1.8 大光圈，超廣角視野，還原真實色彩，夜間拍攝更清晰</p>
                    </div>
                </div>'''

html = html.replace(old_lens, new_lens)

# 寫回
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added lens image to lens-card")
