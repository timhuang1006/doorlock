"""
修正title和description
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 修正title
html = html.replace(
    '<title>智能聯網電子鎖 旗艦智能鎖 | 頂級安全守護</title>',
    '<title>智能聯網電子鎖 | 頂級安全守護</title>'
)

# 修正description
html = html.replace(
    '智能聯網電子鎖 智能門鎖，',
    '智能聯網電子鎖，'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed title and description")
