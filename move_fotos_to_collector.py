import logging
import sys
import os
import shutil


def copy_and_rename_files(source_dir, target_dir):
    # вводим перменную подсчета количества перемещенных в коллектор файлов
    collector_foto_counter = 0
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    for file in os.listdir(source_dir):
        source_path = os.path.join(source_dir, file)

        if os.path.isfile(source_path):
            # Проверка конфликта имен и модификация имени файла
            target_file = os.path.join(target_dir, file)
            counter = 1
            while os.path.exists(target_file):
                base_name, extension = os.path.splitext(file)
                modified_filename = f"{base_name}_{counter}{extension}"
                target_file = os.path.join(target_dir, modified_filename)
                counter += 1

            # Копирование файла в целевую папку
            shutil.copy(source_path, target_file)
            print(f"Скопирован файл: {file} -> {target_file}")
            collector_foto_counter += 1
    logging.info(f"Собрано фото в коллектор: {collector_foto_counter}")


if __name__ == "__main__":
    # настраиваем логгинг
    logging.basicConfig(filename='/media/nikmin/arc/log.txt', level=logging.INFO)
    if len(sys.argv) != 3:
        print("Usage: python3 move_fotos_to_collector.py /path/to/dir")
        sys.exit(1)
    source_directory = sys.argv[1]
    target_directory = sys.argv[2]

    # Вызываем функцию с параметрами
    copy_and_rename_files(source_directory, target_directory)

print("Копирование завершено.")
