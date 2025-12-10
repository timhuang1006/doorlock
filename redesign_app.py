"""
完全重新設計APP板塊
使用實際app截圖，創建與圖片一模一樣的互動式按鈕
"""
import re

# 定義新的APP板塊HTML（與圖片完全匹配的設計）
new_app_section = '''    <!-- APP 演示 -->
    <section id="app-demo" class="app-demo-section">
        <div class="container">
            <h2 class="section-title animate-on-scroll">APP <span class="gold-glow">遠端視訊對講</span></h2>
            <p class="section-subtitle animate-on-scroll">人在外面也能隨時掌握家門狀況</p>

            <div class="app-demo-wrapper animate-on-scroll">
                <!-- 手機APP截圖互動區 -->
                <div class="app-phone-container">
                    <div class="app-screen-wrapper" id="appScreenWrapper">
                        <!-- 預設圖片：遠程開鎖請求 -->
                        <img src="assets/app_unlock_request.jpg" alt="APP 遠端開門" class="app-screen-img" id="appDefaultImg">
                        
                        <!-- 解鎖後圖片：門鎖已打開 -->
                        <img src="assets/app_unlocked.jpg" alt="APP 已解鎖" class="app-screen-img app-unlocked-img" id="appUnlockedImg">
                        
                        <!-- 透明按鈕覆蓋層 - 對齊藍色「馬上開鎖」按鈕位置 -->
                        <button class="app-unlock-btn" id="appUnlockBtn">
                            <span class="btn-text">馬上開鎖</span>
                            <span class="btn-countdown" id="btnCountdown">(60秒)</span>
                        </button>
                        
                        <!-- 開鎖成功特效 -->
                        <div class="unlock-success-overlay" id="unlockSuccessOverlay">
                            <div class="success-ring"></div>
                            <div class="success-icon">
                                <i class="fas fa-unlock-alt"></i>
                            </div>
                            <div class="success-message">門鎖已打開</div>
                        </div>
                    </div>
                </div>

                <!-- 功能說明 -->
                <div class="app-features">
                    <div class="app-feature-item">
                        <i class="fas fa-video"></i>
                        <h4>即時視訊通話</h4>
                        <p>高清雙向語音視訊對講</p>
                    </div>
                    <div class="app-feature-item">
                        <i class="fas fa-unlock"></i>
                        <h4>遠端一鍵開鎖</h4>
                        <p>確認訪客後遠端解鎖</p>
                    </div>
                    <div class="app-feature-item">
                        <i class="fas fa-history"></i>
                        <h4>開門記錄查詢</h4>
                        <p>完整記錄每次進出</p>
                    </div>
                    <div class="app-feature-item">
                        <i class="fas fa-bell"></i>
                        <h4>異常即時通知</h4>
                        <p>門前異常立即手機推播</p>
                    </div>
                </div>
            </div>
        </div>
    </section>'''

# 讀取HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 用正則表達式替換整個APP演示section
pattern = r'<!-- APP 演示 -->.*?</section>'
html = re.sub(pattern, new_app_section, html, flags=re.DOTALL, count=1)

# 寫回文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML updated: APP section redesigned with interactive button")
