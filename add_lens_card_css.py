"""
添加CSS樣式讓鏡頭圖片正確顯示並凸顯重點
"""

css_styles = '''

/* ===== 鏡頭卡片圖片樣式 ===== */
.lens-card {
    position: relative;
    overflow: hidden;
    background: #000 !important;
    padding: 0 !important;
}

.lens-image-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
}

.lens-exploded-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
}

.lens-text-overlay {
    position: relative;
    z-index: 2;
    padding: 25px;
    background: linear-gradient(180deg, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.4) 50%, rgba(0,0,0,0.8) 100%);
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}

.lens-text-overlay .tech-icon {
    color: #FFD700;
    font-size: 2rem;
    margin-bottom: 10px;
}

.lens-text-overlay h3 {
    color: #FFD700;
    font-size: 1.4rem;
    margin-bottom: 8px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.8);
}

.lens-text-overlay p {
    color: rgba(255,255,255,0.9);
    font-size: 0.9rem;
    text-shadow: 0 1px 5px rgba(0,0,0,0.8);
}

/* 鏡頭發光效果 */
.lens-card::after {
    content: '';
    position: absolute;
    top: 50%;
    right: 20%;
    width: 80px;
    height: 80px;
    background: radial-gradient(circle, rgba(255,215,0,0.3) 0%, transparent 70%);
    border-radius: 50%;
    z-index: 3;
    animation: lensGlow 2s ease-in-out infinite;
    pointer-events: none;
}

@keyframes lensGlow {
    0%, 100% { opacity: 0.5; transform: translate(-50%, -50%) scale(1); }
    50% { opacity: 1; transform: translate(-50%, -50%) scale(1.2); }
}
'''

# 添加樣式
with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_styles)

print("CSS added: Lens card image styles")
