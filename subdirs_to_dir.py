
# Here's a script that extracts files from a source folder, renames them by adding the names
# of the folders and subfolders to the file name using the "@" separator, and moves them to a target folder:
# You can achieve task using Python with the os and shutil modules.
# get_available_name function generates a unique name in the target folder by appending "_1", "_2",
# and so on if a file with the same name already exists.


import os
import shutil

def process_files(source_folder, target_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_path, source_folder)
            new_name = "@".join(relative_path.split(os.path.sep)[:-1]) + "@" + file
            target_path = os.path.join(target_folder, new_name)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)

            try:
                shutil.move(source_path, target_path)
                print(f"Moved '{source_path}' to '{target_path}'")
            except shutil.Error as e:
                print(f"Failed to move '{source_path}': {e}")

if __name__ == "__main__":
    source_folder = "/media/nikmin/arc/test"
    target_folder = "/media/nikmin/arc/test_output"

    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
    elif not os.path.exists(target_folder):
        print(f"Target folder '{target_folder}' does not exist.")
    else:
        process_files(source_folder, target_folder)

# relative_path - это относительный путь к исходному файлу относительно исходной папки.
# Он разбивается на список директорий с помощью метода split, используя разделитель os.path.sep,
# который представляет собой разделитель пути для текущей операционной системы.
#  [:-1] - это срез списка, который исключает последний элемент списка, который является именем исходного файла.
#  "@".join() - это метод, который объединяет список директорий в строку, используя символ "@" в качестве разделителя.
#  + "@" + file - это конкатенация полученной строки с символом "@" и именем исходного файла.
#  Таким образом, новое имя файла представляет собой список директорий в относительном пути, объединенных символом "@",
#  за которым следует символ "@", а затем имя исходного файла.