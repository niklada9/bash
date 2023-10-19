import os
import shutil
from PIL import Image
import exifread

# Функция для извлечения даты съемки из метаданных EXIF
def get_capture_date(file_path):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)
        if 'EXIF DateTimeOriginal' in tags:
            return str(tags['EXIF DateTimeOriginal'])
    return None

# Папка, из которой будут извлекаться фотографии
source_folder = 'путь_к_исходной_папке'
# Папка, в которую будут отправляться фотографии
destination_folder = 'путь_к_папке_года'

for root, _, files in os.walk(source_folder):
    for filename in files:
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            file_path = os.path.join(root, filename)
            capture_date = get_capture_date(file_path)
            if capture_date:
                year = capture_date[:4]
                year_folder = os.path.join(destination_folder, year)
                if not os.path.exists(year_folder):
                    os.makedirs(year_folder)
                destination_path = os.path.join(year_folder, filename)
                shutil.copy(file_path, destination_path)
                print(f"Файл {filename} перемещен в папку {year}")

print("Готово.")
