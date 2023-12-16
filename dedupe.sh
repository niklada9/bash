#!/bin/bash

# дедупликация файлов общей папки, куда собраны файлы из подпапок с переименованием
if [ -n "$1" ] && [ -n "$2" ]; then
    target_directory="$1"
    dir="$2"
    # echo "$target_directory"
else
    echo "replace_spaces.sh путь к целевой директории не указан."
    exit 1
fi

echo "начинаем дедупликацию папки: ${target_directory}"
rclone dedupe --by-hash --dedupe-mode oldest --log-file=$dir"dedupe.txt" "$target_directory"
echo "дедуплицировано в директории ${target_directory}:" >> $dir"log.txt"
wc -l $dir"dedupe.txt" >> $dir"log.txt"
# shellcheck disable=SC2188
> $dir"dedupe.txt"


