# Replace "/media/nikmin/arc/ya_disk/2013_2001_Упорядоченное" with the actual path to the folder where you want to replace spaces with underscores in file and folder names.
# This script will recursively go through all subdirectories and replace spaces with underscores in both folder and file names.


import os

def replace_spaces_with_underscores(folder_path):
    for root, dirs, files in os.walk(folder_path):
        # Rename folders
        for dir_name in dirs:
            original_dir_path = os.path.join(root, dir_name)
            new_dir_name = dir_name.replace(" ", "_")
            new_dir_path = os.path.join(root, new_dir_name)

            if original_dir_path != new_dir_path:
                os.rename(original_dir_path, new_dir_path)
                print(f"Renamed folder: {original_dir_path} -> {new_dir_path}")

        # Rename files
        for file_name in files:
            original_file_path = os.path.join(root, file_name)
            new_file_name = file_name.replace(" ", "_")
            new_file_path = os.path.join(root, new_file_name)

            if original_file_path != new_file_path:
                os.rename(original_file_path, new_file_path)
                print(f"Renamed file: {original_file_path} -> {new_file_path}")

if __name__ == "__main__":
    folder_path = "/media/nikmin/arc/ya_disk/upo"  # Change this to your folder path
    replace_spaces_with_underscores(folder_path)

    # OSError: [Errno 39] Directory not empty: '/media/nikmin/arc/ya_disk/upo/2007_05_07 Piter_JJ' -> '/media/nikmin/arc/ya_disk/upo/2007_05_07_Piter_JJ'
