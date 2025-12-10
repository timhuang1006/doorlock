"""
修改 index.html 中的 APP 演示區塊
將現有的 phone-mockup 改為使用實際app截圖和互動元素
"""
import re

# 讀取HTML文件
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 定義新的APP演示區塊內容
new_app_demo = '''    <!-- APP 演示 -->
    <section id="app-demo" class="app-demo-section">
        <div class="container">
            <h2 class="section-title animate-on-scroll">APP <span class="gold-glow">遠端視訊對講</span></h2>
            <p class="section-subtitle animate-on-scroll">人在外面也能隨時掌握家門狀況</p>

            <div class="app-demo-wrapper animate-on-scroll">
                <!-- 實際APP截圖互動區 -->
                <div class="app-phone-container">
                    <div class="app-screen-wrapper">
                        <!-- 預設圖片（可開鎖狀態） -->
                        <img src="assets/app遠端開門.jpg" alt="APP 遠端開門" class="app-default-img app-screen-img">
                        
                        <!-- 解鎖後圖片 -->
                        <img src="assets/app解鎖.jpg" alt="APP 已解鎖" class="app-unlocked-img app-screen-img">
                        
                        <!-- 透明按鈕覆蓋層 -->
                        <div class="unlock-click-area" id="unlockClickArea">
                            <span class="unlock-hint-text">👆 點擊開門</span>
                        </div>
                        
                        <!-- 60秒倒數計時 -->
                        <div class="unlock-countdown-wrapper">
                            <span class="countdown-label">自動重置</span>
                            <span class="unlock-countdown" id="unlockCountdown">60s</span>
                        </div>
                        
                        <!-- 開鎖成功特效 -->
                        <div class="unlock-success-effect" id="unlockSuccessEffect">
                            <div class="success-pulse"></div>
                            <div class="success-checkmark">
                                <i class="fas fa-check- circle"></i>
                            </div>
                            <div class="success-text">門鎖已開啟</div>
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

# 使用正則表達式替換整個 app-demo section
pattern = r'<!-- APP 演示 -->.*?</section>'
html_content = re.sub(pattern, new_app_demo, html_content, flags=re.DOTALL)

# 寫回文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML updated: APP demo section now uses real app screenshots")
