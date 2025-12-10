"""
精確匹配原始APP截圖的CSS樣式
根據用戶上傳的照片調整：
- 灰色背景
- 更圓潤的對話框和按鈕
- 正確的顏色和間距
"""

# 精確匹配原始照片的CSS
css_fix = '''

/* ===== APP模擬器 - 精確匹配原始照片 ===== */
.phone-simulator {
    display: flex;
    justify-content: center;
}

.phone-frame {
    width: 300px;
    background: linear-gradient(180deg, #1a1a1a 0%, #0a0a0a 100%);
    border-radius: 40px;
    padding: 10px;
    box-shadow: 
        0 30px 60px rgba(0, 0, 0, 0.5),
        inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

.app-screen {
    background: #e8e8e8;
    border-radius: 32px;
    overflow: hidden;
    position: relative;
    height: 600px;
}

/* APP狀態切換 */
.app-state {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #e8e8e8;
    transition: opacity 0.5s ease;
}

.app-state-request { opacity: 1; z-index: 1; }
.app-state-unlocked { opacity: 0; z-index: 0; }
.app-state-unlocked.active { opacity: 1; z-index: 2; }

/* 頂部導航 - 符合原始照片 */
.app-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 16px;
    background: #f5f5f5;
}

.back-arrow {
    font-size: 22px;
    color: #333;
    font-weight: 300;
}

.header-title {
    font-size: 17px;
    font-weight: 500;
    color: #000;
}

/* 遠程開鎖請求卡片 - 符合原始照片深藍色漸層 */
.unlock-request-card {
    margin: 12px;
    padding: 28px 20px;
    background: linear-gradient(135deg, #4a8fd9 0%, #2d5a8a 50%, #1e4063 100%);
    border-radius: 20px;
    display: flex;
    align-items: center;
    gap: 14px;
}

.request-icon {
    width: 45px;
    height: 45px;
    background: rgba(255, 255, 255, 0.15);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.request-icon i {
    font-size: 22px;
    color: rgba(255, 255, 255, 0.9);
}

.request-text {
    color: #fff;
    font-size: 16px;
    font-weight: 400;
}

/* 功能圖標列 - 符合原始照片 */
.app-icons-row {
    display: flex;
    justify-content: space-around;
    padding: 18px 10px;
    background: #fff;
    margin: 0;
}

.app-icon-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
}

.icon-circle {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.icon-circle.blue { background: #3b8dd6; }
.icon-circle.orange { background: #f5a623; }
.icon-circle.green { background: #34c759; }

.icon-circle i {
    color: #fff;
    font-size: 22px;
}

.app-icon-item span {
    font-size: 12px;
    color: #333;
}

/* 開鎖對話框 - 符合原始照片白色圓角彈窗 */
.unlock-dialog {
    position: absolute;
    bottom: 100px;
    left: 12px;
    right: 12px;
    background: #fff;
    border-radius: 16px;
    padding: 28px 20px 22px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.dialog-title {
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    color: #000;
    margin-bottom: 6px;
}

.dialog-subtitle {
    text-align: center;
    font-size: 15px;
    color: #666;
    margin-bottom: 28px;
}

.dialog-buttons {
    display: flex;
    gap: 10px;
}

/* 按鈕 - 符合原始照片圓潤樣式 */
.btn-close {
    flex: 0.8;
    padding: 15px 20px;
    background: #ff3b30;
    border: none;
    border-radius: 22px;
    color: #fff;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
}

.btn-unlock {
    flex: 1.2;
    padding: 15px 20px;
    background: #007aff;
    border: none;
    border-radius: 22px;
    color: #fff;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
}

.btn-unlock:hover {
    background: #0056cc;
    transform: scale(1.02);
}

.btn-unlock:active {
    transform: scale(0.98);
}

/* 解鎖成功狀態 - 符合原始照片 */
.app-state-unlocked {
    background: #f0f0f0;
}

.unlock-notification {
    margin: 12px;
    background: #fff;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
}

.notif-header {
    display: flex;
    align-items: center;
    padding: 12px 14px;
    gap: 10px;
}

.notif-icon {
    width: 30px;
    height: 30px;
    background: #3b8dd6;
    border-radius: 7px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.notif-icon i {
    color: #fff;
    font-size: 14px;
}

.notif-title {
    flex: 1;
    font-size: 14px;
    color: #000;
    font-weight: 400;
}

.notif-dismiss {
    color: #007aff;
    font-size: 14px;
}

.notif-content {
    padding: 8px 14px 14px;
}

.notif-status {
    font-size: 17px;
    font-weight: 600;
    color: #000;
    margin-bottom: 4px;
}

.notif-user {
    font-size: 14px;
    color: #888;
}

.unlock-blue-bar {
    height: 55px;
    margin: 0 12px;
    background: linear-gradient(135deg, #4a8fd9 0%, #2d5a8a 100%);
    border-radius: 14px;
}

/* 記錄列表 - 符合原始照片 */
.unlock-records {
    padding: 16px 12px;
    background: #fff;
    margin-top: 12px;
}

.records-date {
    font-size: 13px;
    color: #888;
    margin-bottom: 12px;
    padding-left: 4px;
}

.record-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px 4px;
    border-bottom: 1px solid #f0f0f0;
}

.record-dot {
    width: 8px;
    height: 8px;
    background: #007aff;
    border-radius: 50%;
    flex-shrink: 0;
}

.record-info { flex: 1; }

.record-title {
    font-size: 15px;
    color: #000;
    margin-bottom: 2px;
}

.record-sub {
    font-size: 13px;
    color: #888;
}

.record-icon {
    color: #333;
    font-size: 20px;
}

.record-thumb {
    width: 48px;
    height: 48px;
    background: #e5e5e5;
    border-radius: 8px;
}

/* 開鎖成功特效 */
.unlock-effect {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.75);
    display: none;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 100;
    border-radius: 32px;
}

.unlock-effect.active {
    display: flex;
    animation: fadeIn 0.3s ease;
}

.effect-ring {
    position: absolute;
    width: 110px;
    height: 110px;
    border: 3px solid rgba(52, 199, 89, 0.5);
    border-radius: 50%;
    animation: ringPulse 1s ease-out infinite;
}

.effect-icon {
    width: 85px;
    height: 85px;
    background: linear-gradient(135deg, #34c759, #28a745);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: iconPop 0.5s ease;
    box-shadow: 0 8px 25px rgba(52, 199, 89, 0.5);
}

.effect-icon i {
    font-size: 40px;
    color: #fff;
}

.effect-text {
    margin-top: 18px;
    font-size: 20px;
    font-weight: 600;
    color: #fff;
    animation: slideUp 0.5s ease 0.2s both;
}

/* 響應式 */
@media (max-width: 992px) {
    .app-demo-wrapper {
        grid-template-columns: 1fr;
        gap: 50px;
    }
}

@media (max-width: 400px) {
    .phone-frame { width: 280px; }
    .app-screen { height: 550px; }
}
'''

# 讀取現有CSS，移除舊的APP樣式
with open('css/style.css', 'r', encoding='latin-1') as f:
    css = f.read()

import re
# 移除之前添加的APP樣式
css = re.sub(r'/\* =+ APP模擬器樣式.*?(?=/\*|$)', '', css, flags=re.DOTALL)
css = re.sub(r'/\* =+ APP模擬器 - 精確匹配.*?(?=/\*|$)', '', css, flags=re.DOTALL)

# 寫入清理後的CSS並添加新樣式
with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css + css_fix)

print("CSS updated: Precisely matching original photo")
