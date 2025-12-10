"""
添加CSS樣式 - 讓按鈕精確覆蓋圖片中的藍色「馬上開鎖」按鈕位置
"""

css_styles = '''

/* ===== APP演示板塊 - 重新設計（與圖片一致） ===== */
.app-demo-section {
    padding: 100px 0;
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
}

.app-demo-wrapper {
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: 80px;
    align-items: center;
    max-width: 1200px;
    margin: 60px auto 0;
}

/* 手機容器 */
.app-phone-container {
    display: flex;
    justify-content: center;
}

.app-screen-wrapper {
    position: relative;
    width: 320px;
    max-width: 100%;
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 
        0 25px 80px rgba(0, 0, 0, 0.6),
        0 0 0 1px rgba(255, 215, 0, 0.15);
}

/* APP截圖圖片 */
.app-screen-img {
    width: 100%;
    height: auto;
    display: block;
    transition: opacity 0.5s ease;
}

.app-unlocked-img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0;
    pointer-events: none;
}

.app-unlocked-img.active {
    opacity: 1;
}

/* 透明按鈕 - 精確覆蓋圖片中的藍色「馬上開鎖」按鈕 */
.app-unlock-btn {
    position: absolute;
    /* 根據圖片中按鈕位置調整 - 對話框右下角 */
    bottom: 36%;
    right: 8%;
    width: 140px;
    height: 45px;
    background: rgba(0, 122, 255, 0.15);
    border: 2px solid rgba(0, 122, 255, 0.4);
    border-radius: 8px;
    color: transparent;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.3s ease;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 2px;
}

.app-unlock-btn:hover {
    background: rgba(0, 122, 255, 0.35);
    border-color: rgba(0, 122, 255, 0.8);
    box-shadow: 0 0 20px rgba(0, 122, 255, 0.4);
}

.app-unlock-btn:active {
    transform: scale(0.97);
}

.app-unlock-btn .btn-text,
.app-unlock-btn .btn-countdown {
    color: transparent;
}

/* 開鎖成功特效覆蓋層 */
.unlock-success-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    display: none;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 20;
    backdrop-filter: blur(4px);
}

.unlock-success-overlay.active {
    display: flex;
    animation: fadeIn 0.3s ease;
}

/* 成功光環 */
.success-ring {
    position: absolute;
    width: 150px;
    height: 150px;
    border-radius: 50%;
    border: 3px solid rgba(6, 199, 85, 0.5);
    animation: ringPulse 1s ease-out infinite;
}

/* 成功圖標 */
.success-icon {
    width: 100px;
    height: 100px;
    background: linear-gradient(135deg, #06c755, #04a847);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: iconPop 0.5s ease;
    box-shadow: 0 10px 40px rgba(6, 199, 85, 0.5);
}

.success-icon i {
    font-size: 50px;
    color: #fff;
}

/* 成功訊息 */
.success-message {
    margin-top: 25px;
    font-size: 24px;
    font-weight: 600;
    color: #fff;
    animation: slideUp 0.5s ease 0.2s both;
}

/* 動畫關鍵幀 */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes ringPulse {
    0% { transform: scale(0.8); opacity: 1; }
    100% { transform: scale(1.5); opacity: 0; }
}

@keyframes iconPop {
    0% { transform: scale(0); }
    70% { transform: scale(1.15); }
    100% { transform: scale(1); }
}

@keyframes slideUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* 功能說明區 */
.app-features {
    display: grid;
    gap: 25px;
}

.app-feature-item {
    display: flex;
    align-items: flex-start;
    gap: 20px;
    padding: 25px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 215, 0, 0.1);
    border-radius: 12px;
    transition: all 0.3s ease;
}

.app-feature-item:hover {
    background: rgba(255, 215, 0, 0.05);
    border-color: rgba(255, 215, 0, 0.3);
    transform: translateX(10px);
}

.app-feature-item i {
    font-size: 28px;
    color: #FFD700;
    flex-shrink: 0;
    margin-top: 2px;
}

.app-feature-item h4 {
    font-size: 18px;
    color: #fff;
    margin: 0 0 8px 0;
}

.app-feature-item p {
    font-size: 14px;
    color: #999;
    margin: 0;
    line-height: 1.5;
}

/* 響應式設計 */
@media (max-width: 992px) {
    .app-demo-wrapper {
        grid-template-columns: 1fr;
        gap: 50px;
    }
}

@media (max-width: 576px) {
    .app-screen-wrapper {
        width: 280px;
    }
    
    .app-unlock-btn {
        width: 120px;
        height: 38px;
    }
    
    .success-icon {
        width: 80px;
        height: 80px;
    }
    
    .success-icon i {
        font-size: 40px;
    }
    
    .success-message {
        font-size: 20px;
    }
}
'''

# 讀取CSS
with open('css/style.css', 'r', encoding='latin-1') as f:
    css = f.read()

# 移除舊的APP演示樣式（如果存在）
import re
css = re.sub(r'/\* =+ APP演示.*?(?=/\*|\Z)', '', css, flags=re.DOTALL)

# 添加新樣式
with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_styles)

print("CSS styles added: Button positioned to match image")
