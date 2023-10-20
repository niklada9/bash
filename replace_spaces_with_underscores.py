# Replace "/media/nikmin/arc/ya_disk/2013_2001_Упорядоченное" with the actual path to the folder where you want to replace spaces with underscores in file and folder names.
# This script will recursively go through all subdirectories and replace spaces with underscores in both folder and file names.


import os
import shutil

def replace_spaces_with_underscores(folder_path):
    for root, dirs, files in os.walk(folder_path):
        # Rename folders
        for dir_name in dirs:
            original_dir_path = os.path.join(root, dir_name)
            new_dir_name = dir_name.replace(" ", "_")
            new_dir_path = os.path.join(root, new_dir_name)

            # Check for existing folder with the same name
            counter = 2
            while os.path.exists(new_dir_path):
                base_name, extension = os.path.splitext(new_dir_name)
                new_dir_name = f"{base_name}_{counter}{extension}"
                new_dir_path = os.path.join(root, new_dir_name)
                counter += 1

            if original_dir_path != new_dir_path:
                try:
                    os.rename(original_dir_path, new_dir_path)
                    print(f"Renamed folder: {original_dir_path} -> {new_dir_path}")
                except OSError:
                    # If renaming fails, merge the contents of both directories
                    for item in os.listdir(original_dir_path):
                        src = os.path.join(original_dir_path, item)
                        dst = os.path.join(new_dir_path, item)
                        if os.path.isdir(src):
                            shutil.move(src, dst)
                        else:
                            shutil.copy2(src, dst)
                    shutil.rmtree(original_dir_path)

        # Rename files
        for file_name in files:
            original_file_path = os.path.join(root, file_name)
            new_file_name = file_name.replace(" ", "_")
            new_file_path = os.path.join(root, new_file_name)

            # Check for an existing file with the same name
            counter = 2
            while os.path.exists(new_file_path):
                base_name, extension = os.path.splitext(new_file_name)
                new_file_name = f"{base_name}_{counter}{extension}"
                new_file_path = os.path.join(root, new_file_name)
                counter += 1

            if original_file_path != new_file_path:
                os.rename(original_file_path, new_file_path)
                print(f"Renamed file: {original_file_path} -> {new_file_path}")

if __name__ == "__main__":
    folder_path = "/media/nikmin/arc/ya_disk/upo"  # Change this to your folder path
    replace_spaces_with_underscores(folder_path)


 # OSError: [Errno 39] Directory not empty: '/media/nikmin/arc/ya_disk/upo/2007_05_07 Piter_JJ' -> '/media/nikmin/arc/ya_disk/upo/2007_05_07_Piter_JJ'
