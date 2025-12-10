"""
完全用HTML/CSS重現APP介面，不使用圖片覆蓋
創建與APP截圖一模一樣的UI
"""
import re

new_app_section = '''    <!-- APP 演示 -->
    <section id="app-demo" class="app-demo-section">
        <div class="container">
            <h2 class="section-title animate-on-scroll">APP <span class="gold-glow">遠端視訊對講</span></h2>
            <p class="section-subtitle animate-on-scroll">人在外面也能隨時掌握家門狀況</p>

            <div class="app-demo-wrapper animate-on-scroll">
                <!-- 手機模擬器 - 完全用CSS重現APP介面 -->
                <div class="phone-simulator">
                    <!-- 手機框架 -->
                    <div class="phone-frame">
                        <!-- APP畫面內容 -->
                        <div class="app-screen" id="appScreen">
                            
                            <!-- 初始狀態：遠程開鎖請求 -->
                            <div class="app-state app-state-request" id="appStateRequest">
                                <!-- 頂部導航 -->
                                <div class="app-header">
                                    <span class="back-arrow">‹</span>
                                    <span class="header-title">展示架2</span>
                                    <span></span>
                                </div>
                                
                                <!-- 遠程開鎖請求卡片 -->
                                <div class="unlock-request-card">
                                    <div class="request-icon">
                                        <i class="fas fa-broadcast-tower"></i>
                                    </div>
                                    <span class="request-text">遠程開鎖請求</span>
                                </div>
                                
                                <!-- 功能圖標列 -->
                                <div class="app-icons-row">
                                    <div class="app-icon-item">
                                        <div class="icon-circle blue"><i class="fas fa-share-alt"></i></div>
                                        <span>分享設備</span>
                                    </div>
                                    <div class="app-icon-item">
                                        <div class="icon-circle blue"><i class="fas fa-key"></i></div>
                                        <span>鑰匙管理</span>
                                    </div>
                                    <div class="app-icon-item">
                                        <div class="icon-circle orange"><i class="fas fa-th"></i></div>
                                        <span>離線密碼</span>
                                    </div>
                                    <div class="app-icon-item">
                                        <div class="icon-circle green"><i class="fas fa-ellipsis-h"></i></div>
                                        <span>更多</span>
                                    </div>
                                </div>
                                
                                <!-- 開鎖對話框 -->
                                <div class="unlock-dialog">
                                    <div class="dialog-title">遠程開鎖請求</div>
                                    <div class="dialog-subtitle">展示架2</div>
                                    <div class="dialog-buttons">
                                        <button class="btn-close">關閉</button>
                                        <button class="btn-unlock" id="btnUnlock">
                                            馬上開鎖(<span id="countdownNum">60</span>秒)
                                        </button>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- 解鎖成功狀態 -->
                            <div class="app-state app-state-unlocked" id="appStateUnlocked">
                                <!-- 頂部通知 -->
                                <div class="unlock-notification">
                                    <div class="notif-header">
                                        <div class="notif-icon"><i class="fas fa-door-open"></i></div>
                                        <span class="notif-title">展示架2</span>
                                        <span class="notif-dismiss">忽略</span>
                                    </div>
                                    <div class="notif-content">
                                        <div class="notif-status">門鎖已打開</div>
                                        <div class="notif-user">手機用戶:</div>
                                    </div>
                                </div>
                                
                                <!-- 藍色區塊 -->
                                <div class="unlock-blue-bar"></div>
                                
                                <!-- 功能圖標列 -->
                                <div class="app-icons-row">
                                    <div class="app-icon-item">
                                        <div class="icon-circle blue"><i class="fas fa-share-alt"></i></div>
                                        <span>分享設備</span>
                                    </div>
                                    <div class="app-icon-item">
                                        <div class="icon-circle blue"><i class="fas fa-key"></i></div>
                                        <span>鑰匙管理</span>
                                    </div>
                                    <div class="app-icon-item">
                                        <div class="icon-circle orange"><i class="fas fa-th"></i></div>
                                        <span>離線密碼</span>
                                    </div>
                                    <div class="app-icon-item">
                                        <div class="icon-circle green"><i class="fas fa-ellipsis-h"></i></div>
                                        <span>更多</span>
                                    </div>
                                </div>
                                
                                <!-- 記錄列表 -->
                                <div class="unlock-records">
                                    <div class="records-date">今天</div>
                                    <div class="record-item">
                                        <div class="record-dot"></div>
                                        <div class="record-info">
                                            <div class="record-title">門鎖已打開</div>
                                            <div class="record-sub">手機用戶:</div>
                                        </div>
                                        <div class="record-icon"><i class="fas fa-mobile-alt"></i></div>
                                    </div>
                                    <div class="record-item">
                                        <div class="record-dot"></div>
                                        <div class="record-info">
                                            <div class="record-title">遠程開鎖請求</div>
                                        </div>
                                        <div class="record-thumb"></div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- 開鎖成功特效 -->
                            <div class="unlock-effect" id="unlockEffect">
                                <div class="effect-ring"></div>
                                <div class="effect-icon"><i class="fas fa-unlock-alt"></i></div>
                                <div class="effect-text">門鎖已打開</div>
                            </div>
                            
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

# 替換APP section
html = re.sub(r'<!-- APP 演示 -->.*?</section>', new_app_section, html, flags=re.DOTALL, count=1)

# 寫回
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML updated: Pure CSS APP interface created")
