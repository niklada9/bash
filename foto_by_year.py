import os
import shutil
from PIL import Image

def extract_date_taken(filename):
    try:
        image = Image.open(filename)
        exif_data = image._getexif()
        if exif_data is not None and 36867 in exif_data:
            date_taken = exif_data[36867]
            return date_taken
    except (AttributeError, KeyError, IndexError, IOError):
        pass
    return None

def move_photo_to_year_folder(filename):
    date_taken = extract_date_taken(filename)
    if date_taken is not None:
        year = date_taken[:4]
        destination_folder = os.path.join(os.getcwd(), year)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        shutil.move(filename, destination_folder)

# Пример использования скрипта:
folder_path = "путь_к_папке_с_фотографиями"
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        file_path = os.path.join(folder_path, filename)
        move_photo_to_year_folder(file_path)
