"""
更新JavaScript - 處理純CSS APP介面的互動
"""
import re

js_code = '''
// ----- APP模擬器互動 -----
function initUnlockDemo() {
    const btnUnlock = document.getElementById('btnUnlock');
    const countdownNum = document.getElementById('countdownNum');
    const stateRequest = document.getElementById('appStateRequest');
    const stateUnlocked = document.getElementById('appStateUnlocked');
    const unlockEffect = document.getElementById('unlockEffect');
    
    if (!btnUnlock) {
        console.warn('APP demo elements not found');
        return;
    }
    
    let countdown = 60;
    
    // 更新倒數
    setInterval(function() {
        countdown--;
        if (countdown < 0) countdown = 60;
        if (countdownNum) countdownNum.textContent = countdown;
    }, 1000);
    
    // 點擊開鎖按鈕
    btnUnlock.addEventListener('click', function() {
        // 顯示特效
        if (unlockEffect) {
            unlockEffect.classList.add('active');
        }
        
        // 1.5秒後切換到解鎖狀態
        setTimeout(function() {
            if (unlockEffect) unlockEffect.classList.remove('active');
            if (stateUnlocked) stateUnlocked.classList.add('active');
        }, 1500);
        
        // 5秒後恢復初始狀態
        setTimeout(function() {
            if (stateUnlocked) stateUnlocked.classList.remove('active');
        }, 6000);
    });
}
'''

# 讀取main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 替換initUnlockDemo函數
pattern = r'// -+ (解鎖按鈕演示|APP模擬器).*?^function initUnlockDemo\(\).*?^\}'
js = re.sub(pattern, js_code.strip(), js, flags=re.DOTALL | re.MULTILINE)

# 寫回
with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("JavaScript updated: APP simulator interaction ready")
