"""
添加Open Graph標籤優化社交媒體預覽
並添加版本號參數強制刷新快取
"""
import time

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 當前時間戳作為版本號
version = int(time.time())

# Open Graph標籤
og_tags = f'''    <!-- Open Graph / 社交媒體預覽 -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://doorlock-79e27.web.app/?v={version}">
    <meta property="og:title" content="智能聯網電子鎖 | 頂級安全守護">
    <meta property="og:description" content="智能聯網電子鎖，結合人臉辨識、遠端開門、指紋等多種功能。頂級安全守護，奢華黑金配色。">
    <meta property="og:image" content="https://doorlock-79e27.web.app/assets/lock-body.png">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="智能聯網電子鎖 | 頂級安全守護">
    <meta name="twitter:description" content="智能聯網電子鎖，結合人臉辨識、遠端開門、指紋等多種功能。">
    <meta name="twitter:image" content="https://doorlock-79e27.web.app/assets/lock-body.png">
'''

# 檢查是否已有og標籤
if 'og:title' not in html:
    # 在</head>前插入
    html = html.replace('</head>', og_tags + '</head>')
    print("Added Open Graph tags")
else:
    # 更新版本號
    import re
    html = re.sub(r'og:url" content="[^"]+', f'og:url" content="https://doorlock-79e27.web.app/?v={version}', html)
    print("Updated version in og:url")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Version: {version}")
