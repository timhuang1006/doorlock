import re
import urllib.parse

def fix_encoding(match):
    prefix = match.group(1) # src=" or url('
    path = match.group(2)   # assets/filename.png
    suffix = match.group(3) # " or ')
    
    # Split path into parts to encode only the filename/segments, not the slashes?
    # Actually, urllib.parse.quote(path) encodes slashes by default unless safe='/' is used.
    # But we want to keep 'assets/' as is.
    
    if 'assets/' in path:
        base, filename = path.split('assets/', 1)
        # base should be empty string usually if match includes assets/
        # But my regex below will capture the whole path.
        
        encoded_filename = urllib.parse.quote(filename)
        new_path = f"assets/{encoded_filename}"
        return f"{prefix}{new_path}{suffix}"
    return match.group(0)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Regex for src="assets/..."
# Captures: 1: src=", 2: path, 3: "
pattern_src = re.compile(r'(src=["\'])((?:assets/)[^"\']+)((?:["\']))')
content = pattern_src.sub(fix_encoding, content)

# Regex for url('assets/...')
# Captures: 1: url(', 2: path, 3: ')
pattern_url = re.compile(r'(url\([\'"]?)((?:assets/)[^\'"\)]+)((?:[\'"]?\)))')
content = pattern_url.sub(fix_encoding, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Encoded paths in index.html")
