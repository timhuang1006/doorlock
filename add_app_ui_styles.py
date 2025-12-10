"""
添加CSS樣式 - 完全重現APP介面視覺效果
"""

css_styles = '''

/* ===== APP模擬器樣式 ===== */
.phone-simulator {
    display: flex;
    justify-content: center;
}

.phone-frame {
    width: 320px;
    background: #000;
    border-radius: 36px;
    padding: 12px;
    box-shadow: 
        0 30px 60px rgba(0, 0, 0, 0.5),
        inset 0 0 0 2px rgba(255, 255, 255, 0.1);
}

.app-screen {
    background: #f5f5f5;
    border-radius: 28px;
    overflow: hidden;
    position: relative;
    min-height: 580px;
}

/* APP狀態切換 */
.app-state {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transition: opacity 0.5s ease;
}

.app-state-request {
    opacity: 1;
    z-index: 1;
}

.app-state-unlocked {
    opacity: 0;
    z-index: 0;
}

.app-state-unlocked.active {
    opacity: 1;
    z-index: 2;
}

/* 頂部導航 */
.app-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 20px;
    background: #fff;
}

.back-arrow {
    font-size: 24px;
    color: #333;
}

.header-title {
    font-size: 16px;
    font-weight: 500;
    color: #333;
}

/* 遠程開鎖請求卡片 */
.unlock-request-card {
    margin: 15px;
    padding: 25px;
    background: linear-gradient(135deg, #4a90d9 0%, #357abd 100%);
    border-radius: 16px;
    display: flex;
    align-items: center;
    gap: 15px;
}

.request-icon {
    width: 50px;
    height: 50px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.request-icon i {
    font-size: 24px;
    color: #fff;
}

.request-text {
    color: #fff;
    font-size: 16px;
    font-weight: 500;
}

/* 功能圖標列 */
.app-icons-row {
    display: flex;
    justify-content: space-around;
    padding: 20px 15px;
    background: #fff;
}

.app-icon-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
}

.icon-circle {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.icon-circle.blue {
    background: #4a90d9;
}

.icon-circle.orange {
    background: #f5a623;
}

.icon-circle.green {
    background: #4cd964;
}

.icon-circle i {
    color: #fff;
    font-size: 20px;
}

.app-icon-item span {
    font-size: 11px;
    color: #666;
}

/* 開鎖對話框 */
.unlock-dialog {
    position: absolute;
    bottom: 80px;
    left: 15px;
    right: 15px;
    background: #fff;
    border-radius: 16px;
    padding: 25px 20px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
}

.dialog-title {
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    color: #333;
    margin-bottom: 8px;
}

.dialog-subtitle {
    text-align: center;
    font-size: 14px;
    color: #666;
    margin-bottom: 25px;
}

.dialog-buttons {
    display: flex;
    gap: 12px;
}

.btn-close {
    flex: 1;
    padding: 14px;
    background: #ff3b30;
    border: none;
    border-radius: 10px;
    color: #fff;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: transform 0.2s;
}

.btn-unlock {
    flex: 1.3;
    padding: 14px;
    background: #007aff;
    border: none;
    border-radius: 10px;
    color: #fff;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
}

.btn-unlock:hover {
    background: #0056b3;
    transform: scale(1.02);
}

.btn-unlock:active {
    transform: scale(0.98);
}

/* 解鎖成功狀態 */
.unlock-notification {
    margin: 15px;
    background: #fff;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.notif-header {
    display: flex;
    align-items: center;
    padding: 12px 15px;
    gap: 10px;
}

.notif-icon {
    width: 32px;
    height: 32px;
    background: #4a90d9;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.notif-icon i {
    color: #fff;
    font-size: 16px;
}

.notif-title {
    flex: 1;
    font-size: 14px;
    color: #333;
}

.notif-dismiss {
    color: #007aff;
    font-size: 14px;
}

.notif-content {
    padding: 10px 15px 15px;
}

.notif-status {
    font-size: 16px;
    font-weight: 600;
    color: #333;
    margin-bottom: 4px;
}

.notif-user {
    font-size: 13px;
    color: #999;
}

.unlock-blue-bar {
    height: 60px;
    margin: 0 15px;
    background: linear-gradient(135deg, #4a90d9 0%, #357abd 100%);
    border-radius: 12px;
}

/* 記錄列表 */
.unlock-records {
    padding: 20px 15px;
}

.records-date {
    font-size: 13px;
    color: #999;
    margin-bottom: 15px;
}

.record-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid #eee;
}

.record-dot {
    width: 8px;
    height: 8px;
    background: #007aff;
    border-radius: 50%;
}

.record-info {
    flex: 1;
}

.record-title {
    font-size: 14px;
    color: #333;
}

.record-sub {
    font-size: 12px;
    color: #999;
}

.record-icon {
    color: #333;
    font-size: 18px;
}

.record-thumb {
    width: 50px;
    height: 50px;
    background: #e0e0e0;
    border-radius: 8px;
}

/* 開鎖成功特效 */
.unlock-effect {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    display: none;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 100;
}

.unlock-effect.active {
    display: flex;
    animation: fadeIn 0.3s ease;
}

.effect-ring {
    position: absolute;
    width: 120px;
    height: 120px;
    border: 3px solid rgba(76, 217, 100, 0.5);
    border-radius: 50%;
    animation: ringPulse 1s ease-out infinite;
}

.effect-icon {
    width: 90px;
    height: 90px;
    background: linear-gradient(135deg, #4cd964, #34c759);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: iconPop 0.5s ease;
    box-shadow: 0 10px 30px rgba(76, 217, 100, 0.5);
}

.effect-icon i {
    font-size: 45px;
    color: #fff;
}

.effect-text {
    margin-top: 20px;
    font-size: 22px;
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
    .phone-frame {
        width: 290px;
    }
    
    .app-screen {
        min-height: 520px;
    }
}
'''

# 添加新樣式
with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_styles)

print("CSS added: APP interface styles complete")
