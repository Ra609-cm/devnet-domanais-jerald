"""
Module 2 — Activity: File Sorting with os and shutil
Student: Domanais, jerald M.
Date: 09/27/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I built a Python script that automatically sorts files into different folders. The script looks at the file extension and moves each file into the correct folder.

For example, image files such as .jpg and .png are moved into an Images folder, while PDF files are moved into a PDFs folder. This makes organizing files faster and easier instead of moving each file manually.


============================================
KEY VOCABULARY
============================================
-os module: A Python module that allows a program to interact with the operating system, such as working with files and folders.
-shutil module: A Python module that provides tools for copying and moving files and folders.
-file path: The location of a file or folder on a computer.
-directory: Another name for a folder where files and other folders are stored.
-file extension: The part of a filename that shows what type of file it is, such as .jpg, .pdf, or .txt.


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

# Target directory to clean up
SOURCE_DIR = "./messy_folder"

# Extension-to-folder mapping rules
EXTENSION_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".odt"],
    "Spreadsheets_and_Data": [".csv", ".xlsx", ".xls", ".json", ".xml"],
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".svg", ".bmp"],
    "Code_and_Scripts": [".py", ".js", ".html", ".css", ".cpp", ".sql"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
}


def organize_directory(target_path):
    # Ensure source directory exists
    if not os.path.exists(target_path):
        print(f"Error: Directory '{target_path}' does not exist.")
        return

    # List all items in the target directory
    items = os.listdir(target_path)
    moved_count = 0

    for item in items:
        item_full_path = os.path.join(target_path, item)

        # Skip subdirectories to avoid nested loops or moving folders
        if os.path.isdir(item_full_path):
            continue

        # Extract extension (lowercased for case-insensitivity)
        _, ext = os.path.splitext(item)
        ext = ext.lower()

        # Determine target category folder
        dest_folder_name = "Others"
        for folder_name, extensions in EXTENSION_CATEGORIES.items():
            if ext in extensions:
                dest_folder_name = folder_name
                break

        # Create destination folder if it doesn't already exist
        dest_dir_path = os.path.join(target_path, dest_folder_name)
        os.makedirs(dest_dir_path, exist_ok=True)

        # Move the file
        destination_path = os.path.join(dest_dir_path, item)
        shutil.move(item_full_path, destination_path)
        print(f"Moved: {item} -> {dest_folder_name}/")
        moved_count += 1

    print(f"\nOrganization complete. Total files sorted: {moved_count}")


if __name__ == "__main__":
    # Example setup: create dummy directory and run
    os.makedirs(SOURCE_DIR, exist_ok=True)
    organize_directory(SOURCE_DIR)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
1. Forgetting to construct the full file path:
   `os.listdir()` only returns the base file names (like "report.pdf"), not 
   the full path. Passing just the file name to `os.path.isfile()` or `shutil.move()` 
   causes a `FileNotFoundError` because Python looks in the current working 
   directory instead of the target folder. 
   -> Fix: Always wrap items with `os.path.join(SOURCE_DIR, item)`.

2. Moving folders into folders:
   Initially, if the script created a "Documents" folder on the first run, 
   the next pass might treat "Documents" as an item and try to sort it.
   -> Fix: Added `if os.path.isdir(item_full_path): continue` at the start of the loop.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
