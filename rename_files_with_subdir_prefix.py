# This script uses the os module to extract files from a folder, get the folder name, and rename the files as described. 
# Here's a Python script to accomplish this:
# Replace "/path/to/your/folder" with the actual path to the folder containing the files you want to rename. 
# This script will walk through all subdirectories, add the folder name in front of each file name separated by @, and rename the files accordingly.
# This script checks if the file name already exists - and renamed new file name with add "_2", "_3", and so on to the new file name if a file with the 
# same name already exists in the directory.
# test test

import os
import shutil

def rename_and_move_files(source_folder, target_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)

            # Получить относительный путь файла от исходной папки
            relative_path = os.path.relpath(file_path, source_folder)

            # Построить новое имя файла, объединяя имя файла и иерархию папок
            new_name = relative_path.replace(os.path.sep, '@')

            # Проверить, существует ли файл с таким именем в целевой папке
            target_path = os.path.join(target_folder, new_name)
            base, ext = os.path.splitext(target_path)
            counter = 1

            while os.path.exists(target_path):
                target_path = f"{base}_{counter}{ext}"
                counter += 1

            # Скопировать и переименовать файл в целевую папку
            shutil.copy(file_path, target_path)

if __name__ == "__main__":
    source_folder = "/media/nikmin/arc/Photos"
    target_folder = "/media/nikmin/arc/Photos_output"

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    rename_and_move_files(source_folder, target_folder)

# write Python code to extact files from folder and rename them to add folder name in front of old file name with separate both part of new name with @ 
# 
