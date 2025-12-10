"""
添加CSS樣式凸顯鏡頭圖片
"""

css_styles = '''

/* ===== 光學鏡頭展示樣式 ===== */
.lens-showcase {
    position: relative;
    background: #000;
    border-radius: 16px;
    padding: 20px;
    overflow: hidden;
}

.lens-img {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 12px;
    animation: lensPulse 3s ease-in-out infinite;
}

/* 鏡頭圖片發光效果 */
@keyframes lensPulse {
    0%, 100% {
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
    }
    50% {
        box-shadow: 0 0 40px rgba(255, 215, 0, 0.6);
    }
}

/* 鏡頭區域金色邊框強調 */
.lens-showcase::before {
    content: '';
    position: absolute;
    top: 10px;
    left: 10px;
    right: 10px;
    bottom: 10px;
    border: 2px solid rgba(255, 215, 0, 0.4);
    border-radius: 14px;
    pointer-events: none;
    animation: borderGlow 2s ease-in-out infinite;
}

@keyframes borderGlow {
    0%, 100% {
        border-color: rgba(255, 215, 0, 0.4);
    }
    50% {
        border-color: rgba(255, 215, 0, 0.8);
    }
}

/* 光學鏡頭Tab的特殊樣式 */
#optical-lens .security-feature-title {
    color: #FFD700;
}

#optical-lens .sec-feature-icon {
    background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
}
'''

# 添加樣式
with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_styles)

print("CSS added: Lens highlight styles")
