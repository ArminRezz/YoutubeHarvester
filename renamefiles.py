# This is a quick helper file that allows you to rename all files in a folder to numbered ones for easier tracking and troubleshooting with datasets
import os

def rename_files_in_folder(folder_path, count_start=1, suffix='', increment=1):
    """Rename files in the specified folder by adding a count and a suffix."""
    try:
        for index, filename in enumerate(os.listdir(folder_path), start=count_start):
            old_file_path = os.path.join(folder_path, filename)
            if os.path.isfile(old_file_path):
                # Create new filename
                new_filename = f"{suffix}_{index}{os.path.splitext(filename)[1]}" # CAN CHANGE OUTPUT PATTERN ON THIS LINE (index_suf or suf_index)
                new_file_path = os.path.join(folder_path, new_filename)
                
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} to {new_file_path}")
                count_start += increment  # Increase count by the specified increment
    except Exception as e:
        print(f"Error renaming files: {e}")

# Example usage
folder_to_rename = 'mp4s'  # Folder containing the files to rename
rename_files_in_folder(folder_to_rename, count_start=1, suffix='pushups', increment=1) # you can change count, name of file, and increment here
