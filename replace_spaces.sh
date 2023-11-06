#!/bin/bash
#This is an example of a Bash script that replaces spaces with underscores in file, folder, and path names:

# Specify the directory you want to start renaming from
# Проверка наличия параметра (пути к целевой директории)
if [ -n "$1" ]; then
    target_directory="$1"
    echo $target_directory
else
    echo "replace_spaces.sh путь к целевой директории не указан."
    exit 1
fi

#start_directory="/media/nikmin/arc/_2013_Summary"
start_directory=$target_directory
# Recursively navigate through the directory and rename folders
find "$start_directory" -depth -name "* *" -type d | while read -r dir; do
    newdir=$(dirname "$dir")/$(basename "$dir" | tr ' ' '_')
    mv "$dir" "$newdir"
    #echo "$dir"
    #echo "$newdir"
done
find "$start_directory" -depth -name "* *" -type f | while read -r file; do
    newfile=$(dirname "$file")/$(basename "$file" | tr ' ' '_')
    mv "$file" "$newfile"
    #echo "$file"
    #echo "$newfile"
done
