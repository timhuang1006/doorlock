import os

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the start and end markers for the section to replace
start_marker = '<div class="app-demo-wrapper animate-on-scroll">'
end_marker = '<div class="app-features">'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find the target section in index.html")
    exit(1)

# The new content to insert
new_content = '''<div class="app-demo-wrapper animate-on-scroll">
                <div class="phone-mockup">
                    <div class="phone-screen">
                        <!-- 互動式開鎖容器 -->
                        <div id="app-interaction-container" class="app-interaction-container">
                            <img id="app-screen-img" src="assets/app_unlock_request.jpg" alt="APP 遠端開鎖請求" class="app-screenshot">
                            
                            <!-- 模擬開鎖按鈕 (覆蓋在圖片上的藍色按鈕區域) -->
                            <button id="interactive-unlock-btn" class="interactive-unlock-btn" onclick="unlockDoor()">
                                <!-- 透明按鈕，覆蓋在圖片按鈕上 -->
                            </button>

                            <!-- 開鎖成功特效 (預設隱藏) -->
                            <div id="unlock-success-overlay" class="unlock-success-overlay" style="display: none;">
                                <div class="success-icon-circle">
                                    <i class="fas fa-check"></i>
                                </div>
                                <p class="success-text">已成功解鎖</p>
                            </div>
                        </div>
                    </div>
                </div>

                '''

# Construct the full file content
final_content = content[:start_idx] + new_content + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Successfully updated APP demo section")
