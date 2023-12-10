#!/bin/bash

# Головной скрипт, запускающий последовательно скрипты и программы, собирающие файлы из целевых папок и подпапок 
# с переименованием, исключающем конфликт имен файлов, и оставляющих путь к исходному файлу в именовании файла
root_dir="/home/nikmin/Yandex.Disk/w/"
collector="/media/nikmin/USB_1TB/foto_collector/"
mkdir "/media/nikmin/USB_1TB/w_output"
output_directory="/media/nikmin/USB_1TB/w_output"
# Удаляем пробелы в названиях файлов и директорий
/home/nikmin/git/bash/replace_spaces.sh "$root_dir"

# Переносим файлы из подпапок в единую папку, с добавлением к имени файла названия папок и подпапок через @
#output_directory=$(python3 /home/nikmin/git/bash/subdirs_to_dir.py "$root_dir")
python3 /home/nikmin/git/bash/subdirs_to_dir.py "$root_dir" "$output_directory"

# Делаем дедупликацию файлов в единой папке
/home/nikmin/git/bash/dedupe.sh "$output_directory"

# Переносим файлы из единой папки в конечную папку collector
python3 /home/nikmin/git/bash/move_fotos_to_collector.py "$output_directory" "$collector"

# Делаем дедупликацию папки collector
/home/nikmin/git/bash/dedupe.sh "$collector"

# Удаляем промежуточные папки и файлы
rm -r "$output_directory"