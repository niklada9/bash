#!/bin/bash

# начальный каталог, из которого будем искать файлы
src_dir="./source_directory"

# каталог, в который будем перемещать файлы
dst_dir="./destination_directory"

# создаем конечный каталог, если он еще не существует
mkdir -p "$dst_dir"

# перебираем все файлы в подкаталогах начального каталога
find "$src_dir" -type f | while read -r file; do
  # извлекаем путь подкаталога относительно начального каталога
  sub_dir=$(dirname "${file#$src_dir}")
  
  # формируем новое имя файла
  new_name="${sub_dir//\//_}${file##*/}"
  
  # перемещаем и переименовываем файл
  mv "$file" "$dst_dir/$new_name"
done
