"""
修復APP圖片路徑問題 - 將中文檔名改為英文檔名
"""
import re

# 讀取HTML文件
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 替換圖片路徑從中文檔名到英文檔名
html_content = html_content.replace('assets/app遠端開門.jpg', 'assets/app_unlock_request.jpg')
html_content = html_content.replace('assets/app解鎖.jpg', 'assets/app_unlocked.jpg')

# 寫回文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Image paths updated successfully")
print("Changed: app遠端開門.jpg -> app_unlock_request.jpg")
print("Changed: app解鎖.jpg -> app_unlocked.jpg")
