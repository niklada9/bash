import sys
import os
import shutil

def copy_and_rename_files(source_directory, target_directory):
    if not os.path.exists(target_directory):
        os.mkdir(target_directory)

    for file in os.listdir(source_directory):
        source_path = os.path.join(source_directory, file)

        if os.path.isfile(source_path):
            # Проверка конфликта имен и модификация имени файла
            target_file = os.path.join(target_directory, file)
            counter = 1
            while os.path.exists(target_file):
                base_name, extension = os.path.splitext(file)
                modified_filename = f"{base_name}_{counter}{extension}"
                target_file = os.path.join(target_directory, modified_filename)
                counter += 1

            # Копирование файла в целевую папку
            shutil.copy(source_path, target_file)
            print(f"Скопирован файл: {file} -> {target_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 move_fotos_to_collector.py /path/to/dir")
        sys.exit(1)
    source_directory = sys.argv[1]
    #source_directory = "/путь/к/исходной/папке"
    target_directory = "/media/nikmin/arc/test_foto_collector"

    # Вызываем функцию с параметрами
    copy_and_rename_files(source_directory, target_directory)

print("Копирование завершено.")
