
# Вы можете использовать Python и модуль shutil для переноса файлов из исходной папки и ее подпапок в целевую папку, 
# а также добавлять "_3" (или более) к именам файлов в случае конфликта. 

import os
import shutil

def move_files_to_target(source_folder, target_folder):
    for root, dirs, files in os.walk(source_folder):
        for file_name in files:
            source_file_path = os.path.join(root, file_name)
            target_file_path = os.path.join(target_folder, file_name)

            # Check for an existing file with the same name in the target folder
            counter = 2
            while os.path.exists(target_file_path):
                base_name, extension = os.path.splitext(file_name)
                new_file_name = f"{base_name}_{counter}{extension}"
                target_file_path = os.path.join(target_folder, new_file_name)
                counter += 1

            shutil.move(source_file_path, target_file_path)
            print(f"Moved file: {source_file_path} -> {target_file_path}")

if __name__ == "__main__":
    source_folder = "/media/nikmin/arc/ya_disk/upo"  # Замените на исходную папку
    target_folder = "/media/nikmin/arc/ya_disk/upa"  # Замените на целевую папку

    move_files_to_target(source_folder, target_folder)
