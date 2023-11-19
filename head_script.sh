#!/bin/bash

root_dir="/media/nikmin/arc/ya_disk/w/fo"
collector="/media/nikmin/USB_1TB/foto_collector"
mkdir "/media/nikmin/USB_1TB/w_output"
output_directory="/media/nikmin/USB_1TB/w_output"
# Удаляем пробелы в названиях файлов и директорий
./replace_spaces.sh "$root_dir"

# Переносим файлы из подпапок в единую папку, с добавлением к имени файла названия папок и подпапок через @
#output_directory=$(python3 /home/nikmin/PycharmProjects/bash1/subdirs_to_dir.py "$root_dir")
python3 /home/nikmin/PycharmProjects/bash1/subdirs_to_dir.py "$root_dir"

# Делаем дедупликацию файлов в единой папке
/home/nikmin/PycharmProjects/bash1/dedupe.sh "$output_directory"

# Переносим файлы из единой папки в конечную папку collector
python3 /home/nikmin/PycharmProjects/bash1/move_fotos_to_collector.py "$output_directory" "$collector"

# Делаем дедупликацию папки collector
/home/nikmin/PycharmProjects/bash1/dedupe.sh "$collector"

# Удаляем промежуточные папки и файлы
rm -r "$output_directory"
