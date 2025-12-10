import os
import re
import urllib.parse

ASSETS_DIR = 'assets'
INDEX_FILE = 'index.html'

# Specific mappings for important files
MAPPING = {
    '主圖去背.png': 'main_lock.png',
    '主圖去背2.png': 'main_lock_2.png',
    'E7主圖2.png': 'main_lock_side.png',
    'E7繁中主圖.png': 'main_lock_zh.png',
    '25個介紹.jpg': 'intro_25.jpg'
}

def get_safe_name(filename):
    if filename in MAPPING:
        return MAPPING[filename]
    
    # Handle screenshots: 螢幕擷取畫面 2025-11-07 001342.png
    if '螢幕擷取畫面' in filename:
        # Extract timestamp
        match = re.search(r'(\d{4}-\d{2}-\d{2}) (\d{6})', filename.replace(':', ''))
        if not match:
             match = re.search(r'(\d{4}-\d{2}-\d{2}) (\d{6})', filename) # Try without replace if needed
        
        if match:
            return f"screenshot_{match.group(1)}_{match.group(2)}.png"
        
        # Fallback for other formats
        return filename.replace('螢幕擷取畫面', 'screenshot').replace(' ', '_')
    
    # Generic fallback: keep ASCII, replace non-ASCII with 'file'
    # But better to just keep it if we don't know what it is, or try to romanize?
    # For now, just return as is if no match, but we want to fix non-ascii.
    
    # If it contains non-ascii
    if not all(ord(c) < 128 for c in filename):
        # Simple hash or generic name?
        # Let's just replace known ones. If unknown, maybe leave it or warn.
        print(f"Warning: Unknown non-ascii file: {filename}")
        return filename # Skip renaming if we don't have a strategy
        
    return filename

def main():
    # 1. Build full mapping of old -> new
    file_mapping = {}
    
    if not os.path.exists(ASSETS_DIR):
        print(f"Error: {ASSETS_DIR} not found")
        return

    for filename in os.listdir(ASSETS_DIR):
        if not all(ord(c) < 128 for c in filename):
            new_name = get_safe_name(filename)
            if new_name != filename:
                old_path = os.path.join(ASSETS_DIR, filename)
                new_path = os.path.join(ASSETS_DIR, new_name)
                
                # Rename file
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {filename} -> {new_name}")
                    file_mapping[filename] = new_name
                except OSError as e:
                    print(f"Error renaming {filename}: {e}")

    # 2. Update index.html
    if not os.path.exists(INDEX_FILE):
        print(f"Error: {INDEX_FILE} not found")
        return

    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace both raw and encoded versions
    for old_name, new_name in file_mapping.items():
        # Raw replacement
        content = content.replace(old_name, new_name)
        
        # Encoded replacement
        encoded_old = urllib.parse.quote(old_name)
        content = content.replace(encoded_old, new_name)
        
        # Also try partial encoding? (e.g. spaces encoded but chinese not? or vice versa?)
        # Usually urllib.parse.quote encodes everything unsafe.
        
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Updated index.html with new filenames")

if __name__ == '__main__':
    main()
