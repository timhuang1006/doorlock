"""
更新JavaScript - 實現點擊開鎖和特效功能
"""
import re

js_code = '''
// ----- 解鎖按鈕演示（重新設計） -----
function initUnlockDemo() {
    const unlockBtn = document.getElementById('appUnlockBtn');
    const defaultImg = document.getElementById('appDefaultImg');
    const unlockedImg = document.getElementById('appUnlockedImg');
    const successOverlay = document.getElementById('unlockSuccessOverlay');
    const countdownSpan = document.getElementById('btnCountdown');
    
    if (!unlockBtn || !defaultImg || !unlockedImg) {
        console.warn('APP demo elements not found');
        return;
    }
    
    let countdown = 60;
    
    // 更新倒數顯示
    function updateCountdown() {
        if (countdownSpan) {
            countdownSpan.textContent = '(' + countdown + '秒)';
        }
        countdown--;
        if (countdown < 0) countdown = 60;
    }
    
    // 每秒更新倒數
    setInterval(updateCountdown, 1000);
    
    // 點擊開鎖按鈕
    unlockBtn.addEventListener('click', function() {
        // 隱藏按鈕
        unlockBtn.style.opacity = '0';
        unlockBtn.style.pointerEvents = 'none';
        
        // 顯示成功特效
        if (successOverlay) {
            successOverlay.classList.add('active');
        }
        
        // 1秒後切換到解鎖圖片
        setTimeout(function() {
            if (successOverlay) {
                successOverlay.classList.remove('active');
            }
            unlockedImg.classList.add('active');
        }, 1500);
        
        // 3秒後恢復初始狀態
        setTimeout(function() {
            unlockedImg.classList.remove('active');
            unlockBtn.style.opacity = '1';
            unlockBtn.style.pointerEvents = 'auto';
        }, 4500);
    });
}
'''

# 讀取main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 找到並替換initUnlockDemo函數
pattern = r'// -+ 解鎖按鈕演示.*?^function initUnlockDemo\(\).*?^\}'
js = re.sub(pattern, js_code.strip(), js, flags=re.DOTALL | re.MULTILINE)

# 寫回文件
with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("JavaScript updated: Unlock demo with effects")
