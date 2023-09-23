#!/bin/bash

target_dir="/путь/к/конечному/каталогу"

find /путь/к/начальному/каталогу -type f | while read file; do
    # Получаем имя подкаталога
    dir_name=$(dirname "$file")
    dir_name=$(basename "$dir_name")

    # Получаем имя файла
    file_name=$(basename "$file")

    # Формируем новое имя файла
    new_file_name="${dir_name}_${file_name}"

    # Перемещаем и переименовываем файл
    mv "$file" "$target_dir/$new_file_name"
done
