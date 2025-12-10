"""
調整彈窗尺寸 - 減少擁擠感
"""
import re

# 新的彈窗和按鈕樣式
css_fix = '''
/* 開鎖對話框 - 調小尺寸減少擁擠 */
.unlock-dialog {
    position: absolute;
    bottom: 80px;
    left: 20px;
    right: 20px;
    background: #fff;
    border-radius: 14px;
    padding: 18px 16px 16px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
}

.dialog-title {
    text-align: center;
    font-size: 15px;
    font-weight: 600;
    color: #000;
    margin-bottom: 4px;
}

.dialog-subtitle {
    text-align: center;
    font-size: 13px;
    color: #666;
    margin-bottom: 16px;
}

.dialog-buttons {
    display: flex;
    gap: 10px;
}

/* 按鈕 - 調小尺寸 */
.btn-close {
    flex: 0.7;
    padding: 10px 14px;
    background: #ff3b30;
    border: none;
    border-radius: 18px;
    color: #fff;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
}

.btn-unlock {
    flex: 1;
    padding: 10px 14px;
    background: #007aff;
    border: none;
    border-radius: 18px;
    color: #fff;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
}

.btn-unlock:hover {
    background: #0056cc;
    transform: scale(1.02);
}

/* 功能圖標列 - 調小間距 */
.app-icons-row {
    display: flex;
    justify-content: space-around;
    padding: 14px 8px;
    background: #fff;
}

.icon-circle {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.icon-circle i {
    color: #fff;
    font-size: 18px;
}

.app-icon-item span {
    font-size: 11px;
    color: #333;
}

/* 遠程開鎖請求卡片 - 調小 */
.unlock-request-card {
    margin: 10px;
    padding: 20px 16px;
    background: linear-gradient(135deg, #4a8fd9 0%, #2d5a8a 50%, #1e4063 100%);
    border-radius: 16px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.request-icon {
    width: 40px;
    height: 40px;
    background: rgba(255, 255, 255, 0.15);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.request-icon i {
    font-size: 18px;
    color: rgba(255, 255, 255, 0.9);
}

.request-text {
    color: #fff;
    font-size: 14px;
    font-weight: 400;
}
'''

# 讀取CSS
with open('css/style.css', 'r', encoding='latin-1') as f:
    css = f.read()

# 移除舊的相關樣式
css = re.sub(r'\.unlock-dialog\s*\{[^}]+\}', '', css)
css = re.sub(r'\.dialog-title\s*\{[^}]+\}', '', css)
css = re.sub(r'\.dialog-subtitle\s*\{[^}]+\}', '', css)
css = re.sub(r'\.dialog-buttons\s*\{[^}]+\}', '', css)
css = re.sub(r'\.btn-close\s*\{[^}]+\}', '', css)
css = re.sub(r'\.btn-unlock\s*\{[^}]+\}', '', css)
css = re.sub(r'\.btn-unlock:hover\s*\{[^}]+\}', '', css)
css = re.sub(r'\.app-icons-row\s*\{[^}]+\}', '', css)
css = re.sub(r'\.icon-circle\s*\{[^}]+\}', '', css)
css = re.sub(r'\.icon-circle i\s*\{[^}]+\}', '', css)
css = re.sub(r'\.app-icon-item span\s*\{[^}]+\}', '', css)
css = re.sub(r'\.unlock-request-card\s*\{[^}]+\}', '', css)
css = re.sub(r'\.request-icon\s*\{[^}]+\}', '', css)
css = re.sub(r'\.request-icon i\s*\{[^}]+\}', '', css)
css = re.sub(r'\.request-text\s*\{[^}]+\}', '', css)

# 寫入
with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css + css_fix)

print("CSS updated: Dialog and buttons made smaller")
