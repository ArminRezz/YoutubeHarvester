import os
import shutil
from pathlib import Path

# Define the path to your Downloads folder
downloads_folder = Path.home() / "Downloads"

# Define the target folders and their corresponding file extensions
folders = {
    "Audio": [".mp3", ".wav", ".flac"],
    "Video": [".mp4", ".avi", ".mov", ".mkv", ".dmg"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Papers": [".pdf", ".docx", ".doc", ".txt", ".tex", ".md", ".pptx"],
    "Archives": [".zip"],
    "Applications": [".app", ".pkg"],
    "Scripts": [".ml", ".java", ".c", ".cpp", ".py", ".rs", ".js", ".html", ".css", ".ts", ".Rmd"],
    "Data": [".json", ".csv", ".xlsx"]
}

# Create target directories if they don't exist
for folder in folders.keys():
    target_folder = downloads_folder / folder
    target_folder.mkdir(exist_ok=True)

# Function to move files to their respective folders
def sort_files():
    for item in downloads_folder.iterdir():
        if item.is_file():
            file_extension = item.suffix.lower()
            moved = False
            for folder, extensions in folders.items():
                if file_extension in extensions:
                    target_folder = downloads_folder / folder
                    try:
                        shutil.move(str(item), str(target_folder / item.name))
                        print(f"Moved: {item.name} to {folder}")
                        moved = True
                        break
                    except Exception as e:
                        print(f"Error moving {item.name}: {e}")
            if not moved:
                print(f"No matching folder for: {item.name}")

if __name__ == "__main__":
    sort_files()
