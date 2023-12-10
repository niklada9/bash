# Here's a script that extracts files from a source folder, renames them by adding the names
# of the folders and subfolders to the file name using the "@" separator, and moves them to a target folder:
# You can achieve task using Python with the os and shutil modules.
# get_available_name function generates a unique name in the target folder by appending "_1", "_2",
# and so on if a file with the same name already exists.

# сбор файлов из подпапок в промежуточную папку с устранением конфликта имен.

import logging
import sys
import os
import shutil


def copy_and_rename_files(source_dir, target_directory):
    # вводим переменную подсчета количества перемещенных файлов
    subdir_to_dir_foto_counter = 0
    if not os.path.exists(target_directory):
        os.mkdir(target_directory)

    for root, dirs, files in os.walk(source_dir, topdown=False):  # Установите topdown=False
        for file in files:
            source_path = os.path.join(root, file)

            # Создаем имя файла, добавляя имена подпапок, разделенные знаком @
            relative_path = os.path.relpath(root, source_dir)
            new_file_name = os.path.join(relative_path, file).replace(os.sep, '@')

            # Создаем путь к целевому файлу
            target_path = os.path.join(target_directory, new_file_name)

            # Проверяем конфликт имен и модифицируем имя, если необходимо
            counter = 1
            while os.path.exists(target_path):
                base_name, extension = os.path.splitext(new_file_name)
                new_file_name = f"{base_name}_{counter}{extension}"
                target_path = os.path.join(target_directory, new_file_name)
                counter += 1

            # Копируем файл в целевую папку с модифицированным именем
            shutil.copy(source_path, target_path)
            subdir_to_dir_foto_counter += 1
    logging.info(f"Собрано фото в общую папку: {subdir_to_dir_foto_counter}")


def main(source_dir, output_dir):
    # настраиваем логгинг
    logging.basicConfig(filename='/media/nikmin/arc/log.txt', level=logging.INFO)
    # Создаем имя_папки_output на уровень выше
    # parent_directory = os.path.dirname(source_directory)
    # output_directory = os.path.join(parent_directory, os.path.basename(source_directory) + "_output")
    # output_directory = "/media/nikmin/USB_1TB/w_output"
    # print(output_directory)
    # Вызываем функцию с параметрами
    copy_and_rename_files(source_dir, output_dir)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 subdirs_to_dir.py /path/to/source_dir /path/to/target_dir")
        sys.exit(1)
    source_directory = sys.argv[1]
    output_directory = sys.argv[2]
    main(source_directory, output_directory)
