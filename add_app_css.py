"""
添加CSS樣式到style.css文件
為新的APP演示區塊添加樣式、動畫和響應式設計
"""

css_styles = '''

/* ===== APP演示區塊 - 重新設計 ===== */
.app-demo-section {
    padding: 100px 0;
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
    position: relative;
    overflow: hidden;
}

.app-phone-container {
    position: relative;
    max-width: 450px;
    margin: 0 auto;
}

.app-screen-wrapper {
    position: relative;
    width: 100%;
    aspect-ratio: 9 / 19.5; /* 類似真實手機螢幕比例 */
    border-radius: 30px;
    overflow: hidden;
    box-shadow: 
        0 20px 60px rgba(0, 0, 0, 0.8),
        0 0 0 1px rgba(255, 215, 0, 0.2),
        0 0 40px rgba(255, 215, 0, 0.15);
    transition: transform 0.3s ease;
}

.app-screen-wrapper:hover {
    transform: scale(1.02);
}

/* 雙層圖片 */
.app-screen-img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: opacity 0.6s ease;
}

.app-default-img {
    opacity: 1;
    z-index: 1;
}

.app-unlocked-img {
    opacity: 0;
    z-index: 2;
}

.app-unlocked-img.active {
    opacity: 1;
}

/* 透明按鈕覆蓋層 */
.unlock-click-area {
    position: absolute;
    bottom: 22%; /* 調整位置以對齊圖片中的開門按鈕 */
    left: 50%;
    transform: translateX(-50%);
    width: 140px;
    height: 140px;
    border-radius: 50%;
    background: rgba(255, 215, 0, 0.1);
    border: 3px solid rgba(255, 215, 0, 0.3);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
    transition: all 0.3s ease;
}

.unlock-click-area:hover {
    background: rgba(255, 215, 0, 0.2);
    border-color: rgba(255, 215, 0, 0.6);
    transform: translateX(-50%) scale(1.05);
}

.unlock-click-area:active {
    transform: translateX(-50%) scale(0.95);
}

.unlock-hint-text {
    color: #FFD700;
    font-size: 14px;
    font-weight: 500;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
    opacity: 0.8;
    pointer-events: none;
}

/* 60秒倒數計時 */
.unlock-countdown-wrapper {
    position: absolute;
    bottom: 8%;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(0, 0, 0, 0.7);
    padding: 8px 16px;
    border-radius: 20px;
    border: 1px solid rgba(255, 215, 0, 0.3);
    z-index: 11;
}

.countdown-label {
    color: #999;
    font-size: 12px;
}

.unlock-countdown {
    color: #FFD700;
    font-size: 16px;
    font-weight: 700;
    min-width: 40px;
    text-align: center;
}

/* 開鎖成功特效 */
.unlock-success-effect {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    height: 100%;
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 20;
    pointer-events: none;
}

.unlock-success-effect.active {
    display: flex;
}

.success-pulse {
    position: absolute;
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(6, 199, 85, 0.4) 0%, transparent 70%);
    animation: successPulse 1s ease-out;
}

.success-checkmark {
    position: relative;
    z-index: 21;
    color: #06c755;
    font-size: 80px;
    animation: checkmark 0.5s ease-out;
    filter: drop-shadow(0 0 20px rgba(6, 199, 85, 0.8));
}

.success-text {
    position: absolute;
    bottom: 30%;
    left: 50%;
    transform: translateX(-50%);
    color: #fff;
    font-size: 20px;
    font-weight: 600;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.8);
    animation: fadeInUp 0.5s ease-out 0.3s both;
}

/* 動畫關鍵幀 */
@keyframes successPulse {
    0% {
        transform: scale(0.8);
        opacity: 1;
    }
    100% {
        transform: scale(2.5);
        opacity: 0;
    }
}

@keyframes checkmark {
    0% {
        transform: scale(0) rotate(-45deg);
        opacity: 0;
    }
    50% {
        transform: scale(1.2) rotate(0deg);
    }
    100% {
        transform: scale(1) rotate(0deg);
        opacity: 1;
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateX(-50%) translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateX(-50%) translateY(0);
    }
}

/* APP功能說明區 */
.app-demo-wrapper {
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: 80px;
    align-items: center;
    max-width: 1200px;
    margin: 60px auto 0;
}

.app-features {
    display: grid;
    grid-template-columns: 1fr;
    gap: 30px;
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
    font-size: 32px;
    color: #FFD700;
    flex-shrink: 0;
    margin-top: 4px;
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
    line-height: 1.6;
}

/* 響應式設計 */
@media (max-width: 992px) {
    .app-demo-wrapper {
        grid-template-columns: 1fr;
        gap: 50px;
    }
    
    .app-phone-container {
        max-width: 350px;
    }
}

@media (max-width: 768px) {
    .app-phone-container {
        max-width: 300px;
    }
    
    .unlock-click-area {
        width: 110px;
        height: 110px;
    }
    
    .unlock-hint-text {
        font-size: 12px;
    }
    
    .success-checkmark {
        font-size: 60px;
    }
    
    .success-text {
        font-size: 16px;
    }
}

@media (max-width: 480px) {
    .app-demo-section {
        padding: 60px 0;
    }
    
    .app-phone-container {
        max-width: 280px;
    }
    
    .app-features {
        gap: 20px;
    }
    
    .app-feature-item {
        padding: 20px;
    }
}
'''

# 讀取現有CSS（使用latin-1避免編碼錯誤）
with open('css/style.css', 'r', encoding='latin-1') as f:
    css_content = f.read()

# 檢查是否已有APP演示樣式，如果有就替換
if '.app-phone-container' in css_content:
    print("CSS already has app-phone-container styles, skipping...")
else:
    # 添加新樣式到文件末尾
    with open('css/style.css', 'a', encoding='utf-8') as f:
        f.write(css_styles)
    print("CSS styles added successfully")
