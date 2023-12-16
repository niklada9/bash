#!/bin/bash

# Головной скрипт, запускающий последовательно скрипты и программы, собирающие файлы из целевых папок и подпапок 
# с переименованием, исключающем конфликт имен файлов, и оставляющих путь к исходному файлу в именовании файла
root_dir="/home/nikmin/Yandex.Disk/w/batu/"
exec_dir="/home/nikmin/git/bash/"
target_dir="/media/nikmin/USB_1TB/"
collector=$target_dir"j_collector/"
echo $collector
mkdir $target_dir"w_output"
output_dir=$target_dir"w_output"
echo $output_dir

# Удаляем пробелы в названиях файлов и директорий
$exec_dir"replace_spaces.sh" "$root_dir"

# Переносим файлы из подпапок в единую папку, с добавлением к имени файла названия папок и подпапок через @
#output_diy=$(python3 $exec_dirsubdirs_to_dir.py "$root_dir")
python3 $exec_dir"subdirs_to_dir.py" "$root_dir" "$output_dir"

# Делаем дедупликацию файлов в единой папке
$exec_dir"dedupe.sh" "$output_dir" "target_dir"

# Переносим файлы из единой папки в конечную папку collector
python3 $exec_dir"move_fotos_to_collector.py" "$output_dir" "$collector"

# Делаем дедупликацию папки collector
$exec_dir"dedupe.sh" "$collector" "target_dir"

# Удаляем промежуточные папки и файлы
# rm -r "$output_dir"