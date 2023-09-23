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
# The expression new_name="${sub_dir//\//_}${file##*/}" consists of two parts: the value of sub_dir and the value of file. Let's break down each part:
# ${sub_dir//\//_}: This part is using a parameter expansion syntax in Bash. It replaces all occurrences of the forward slash (/) in the value of sub_dir with an underscore (). The forward slash (/) and the underscore () are characters used in the replacement pattern.
# ${file##*/}: This part is also using a parameter expansion syntax in Bash. It extracts the file name from the value of file by removing all characters until the last occurrence of the forward slash (/). The double hash (##) is used to perform a greedy deletion, meaning it removes the longest match. The asterisk (*) is a wildcard that matches any number of characters.
# By combining these two parts, the expression assigns a new value to the new_name variable. It creates a file name by combining the modified value of sub_dir (with forward slashes replaced by underscores) and the extracted file name from file.
# For example, if sub_dir is "path/to" and file is "file.txt", the resulting value of new_name would be "path_to_file.txt".

