#!/bin/bash

root_directory="/путь/к/корневому/каталогу"

# Переход в корневой каталог
cd "$root_directory"

# Цикл по всем подкаталогам
for subdirectory in */; do
    subdirectory_name="${subdirectory%/}"

    # Шаг 1: Вызов Python программы 1 с параметром "название каталога"
    python_program_1 "$subdirectory_name"

    # Шаг 2: Создание подкаталога с названием "название каталога + _output"
    output_directory="${subdirectory_name}_output"
    mkdir "$output_directory"

    # Шаг 3: Вызов Python программы 2 с параметрами "название каталога", "название каталога_output"
    python_program_2 "$subdirectory_name" "$output_directory"

    # Шаг 4: Перемещение файлов с проверкой уникальности имени
    destination_directory="/путь/к/upa"
    for file in "$output_directory"/*; do
        filename="${file##*/}"
        destination_path="$destination_directory/$filename"
        index=1
        while [ -e "$destination_path" ]; do
            filename="${filename%.*}_$index.${filename##*.}"
            destination_path="$destination_directory/$filename"
            ((index++))
        done
        mv "$file" "$destination_path"
    done

    # Шаг 5: Вызов Bash-скрипта для каталога upa
    # Предполагается, что есть скрипт с именем "upa_script.sh"
    bash "$destination_directory/upa_script.sh"

    # Шаг 6: Удаление подкаталогов "название каталога" и "название каталога_output"
    rm -r "$subdirectory"
    rm -r "$output_directory"
done
