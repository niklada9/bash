#!/bin/bash

# начальный каталог, из которого будем искать файлы
src_dir="/media/nikmin/arc/test"

# каталог, в который будем перемещать файлы
dst_dir="/media/nikmin/arc/test_output/"
# разделитель между путем и именем файла
delimeter='@'

# создаем конечный каталог, если он еще не существует
#mkdir -p "$dst_dir"

# перебираем все файлы в подкаталогах начального каталога
find "$src_dir" -type f | while read -r file; do
 # извлекаем путь подкаталога относительно начального каталога
  sub_dir=$(dirname "${file#$src_dir}")
 #заменяем слэши на собачки
  sub_dir_name_t=${sub_dir//\//@}
 #убираем собачку в начале строки
  sub_dir_name=${sub_dir_name_t/@/}
 # формируем новое имя файла
  new_name="${sub_dir_name}${delimeter}${file##*/}"
 # перемещаем и переименовываем файл
  mv "$file" "$dst_dir/$new_name"
done
