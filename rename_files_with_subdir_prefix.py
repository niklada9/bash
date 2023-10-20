# This script uses the os module to extract files from a folder, get the folder name, and rename the files as described. 
# Here's a Python script to accomplish this:
# Replace "/path/to/your/folder" with the actual path to the folder containing the files you want to rename. 
# This script will walk through all subdirectories, add the folder name in front of each file name separated by @, and rename the files accordingly.
# This script checks if the file name already exists - and renamed new file name with add "_2", "_3", and so on to the new file name if a file with the 
# same name already exists in the directory.

import os

# Function to process files in a folder
def rename_files_with_folder_name(folder_path):
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            folder_name = os.path.basename(root)
            new_name = f"{folder_name}@{file}"
            
            new_path = os.path.join(root, new_name)
            
            # Check if the new file name already exists
            counter = 2
            while os.path.exists(new_path):
                base_name, extension = os.path.splitext(new_name)
                new_name = f"{base_name}_{counter}{extension}"
                new_path = os.path.join(root, new_name)
                counter += 1
            
            os.rename(file_path, new_path)
            print(f"Renamed: {file} -> {new_name}")

if __name__ == "__main__":
    folder_path = "/media/nikmin/arc/ya_disk/upo"  # Change this to your folder path
    rename_files_with_folder_name(folder_path)
# write Python code to extact files from folder and rename them to add folder name in front of old file name with separate both part of new name with @ 
# 
