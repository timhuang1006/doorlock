"""
將所有 BECK E7 替換成 智能聯網電子鎖
"""

# 讀取HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 計算替換數量
count = html.count('BECK E7')
print(f"Found {count} occurrences of 'BECK E7'")

# 替換
html = html.replace('BECK E7', '智能聯網電子鎖')

# 寫回
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Replaced {count} occurrences")
