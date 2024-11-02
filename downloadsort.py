import os
import shutil
from pathlib import Path

# Define the path to your Downloads folder
# for windows users, local folders in wsl are accessed through mnt/c/..
# for mac users, no worries :)
downloads_folder = Path("/mnt/c/Users/arnoj/Downloads") 

# Define the target folders and their corresponding file extensions
folders = {
    "Audio": [".mp3", ".wav", ".flac"],
    "Video": [".mp4", ".avi", ".mov", ".mkv", ".dmg"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Papers": [".pdf", ".docx", ".doc", ".txt", ".tex", ".md", ".pptx"],
    "Archives": [".zip"],
    "Applications": [".app", ".pkg"],
    "Scripts": [".ml", ".java", ".c", ".cpp", ".py", ".rs", ".js", ".html", ".css", ".ts", ".Rmd"],
    "Data": [".json", ".csv", ".xlsx"],
    "Other": []  # Added "Other" folder for unmatched files
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
                        print(f"Error moving {item.name} to {folder}: {e}")
            if not moved:
                # Move unmatched files to the "Other" folder
                target_folder = downloads_folder / "Other"
                try:
                    shutil.move(str(item), str(target_folder / item.name))
                    print(f"Moved: {item.name} to Other")
                except Exception as e:
                    print(f"Error moving {item.name} to Other: {e}")

if __name__ == "__main__":
    sort_files()
