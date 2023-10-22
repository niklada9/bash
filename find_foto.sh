#!/bin/bash

# Путь к папке, в которой нужно искать фотографии
folder_path="/media/nikmin/arc/ya_disk/upo"

# Рекурсивный поиск файлов с расширениями .jpg, .jpeg и .png
find "$folder_path" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \)

