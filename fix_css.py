"""
修正CSS：
1. 讓圖片完整顯示（使用object-fit: contain）
2. 按鈕精確覆蓋圖片中的藍色「馬上開鎖」按鈕
"""

# 新的CSS樣式（修正版）
css_fix = '''

/* ===== APP演示板塊 - 修正版 ===== */
.app-screen-wrapper {
    position: relative;
    width: 320px;
    max-width: 100%;
    background: #000;
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 
        0 25px 80px rgba(0, 0, 0, 0.6),
        0 0 0 1px rgba(255, 215, 0, 0.15);
}

/* APP截圖 - 完整顯示整張圖片 */
.app-screen-img {
    width: 100%;
    height: auto;
    display: block;
    object-fit: contain;
}

.app-unlocked-img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: contain;
    background: #000;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.5s ease;
}

.app-unlocked-img.active {
    opacity: 1;
}

/* 透明按鈕 - 精確覆蓋圖片中的藍色「馬上開鎖」按鈕 */
/* 根據用戶標記的位置，按鈕在對話框右側 */
.app-unlock-btn {
    position: absolute;
    /* 精確對齊圖片中藍色按鈕的位置 */
    bottom: 43.5%;
    right: 7%;
    width: 42%;
    height: 6.5%;
    background: transparent;
    border: none;
    border-radius: 25px;
    cursor: pointer;
    z-index: 10;
    transition: all 0.2s ease;
}

.app-unlock-btn:hover {
    background: rgba(0, 122, 255, 0.2);
    box-shadow: 0 0 15px rgba(0, 122, 255, 0.3);
}

.app-unlock-btn:active {
    transform: scale(0.98);
}

.app-unlock-btn .btn-text,
.app-unlock-btn .btn-countdown {
    display: none;
}
'''

# 讀取CSS
with open('css/style.css', 'r', encoding='latin-1') as f:
    css = f.read()

# 移除舊的相關樣式
import re
# 移除.app-screen-wrapper的舊定義
css = re.sub(r'\.app-screen-wrapper\s*\{[^}]+\}', '', css)
# 移除.app-screen-img的舊定義  
css = re.sub(r'\.app-screen-img\s*\{[^}]+\}', '', css)
# 移除.app-unlock-btn的舊定義
css = re.sub(r'\.app-unlock-btn\s*\{[^}]+\}', '', css)
css = re.sub(r'\.app-unlock-btn:hover\s*\{[^}]+\}', '', css)
css = re.sub(r'\.app-unlock-btn:active\s*\{[^}]+\}', '', css)
css = re.sub(r'\.app-unlock-btn \.btn-text[^}]+\}', '', css)
# 移除.app-unlocked-img的舊定義
css = re.sub(r'\.app-unlocked-img\s*\{[^}]+\}', '', css)
css = re.sub(r'\.app-unlocked-img\.active\s*\{[^}]+\}', '', css)

# 添加新樣式
with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css + css_fix)

print("CSS fixed: Image shows completely, button covers the exact position")
