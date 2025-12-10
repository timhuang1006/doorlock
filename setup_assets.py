import os
import shutil
import glob

# Source and destination directories
source_dir = r"C:\Users\Administrator\Desktop\E7"
dest_dir = r"C:\Users\Administrator\Desktop\門鎖網站\assets"

# Ensure destination exists
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Patterns to match
patterns = ["**/*.jpg", "**/*.png"]

copied_count = 0

print(f"Scanning {source_dir} for images...")

for pattern in patterns:
    # Recursive search
    search_path = os.path.join(source_dir, pattern)
    files = glob.glob(search_path, recursive=True)
    
    for file_path in files:
        try:
            # Get filename
            filename = os.path.basename(file_path)
            dest_path = os.path.join(dest_dir, filename)
            
            # Copy file
            shutil.copy2(file_path, dest_path)
            print(f"Copied: {filename}")
            copied_count += 1
        except Exception as e:
            print(f"Error copying {file_path}: {e}")

print(f"\nTotal images copied: {copied_count}")
