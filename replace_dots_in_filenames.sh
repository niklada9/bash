#!/bin/bash
# replaces dots to underlines in files, named as data
start_directory="./tmp_nik_all"

find "$start_directory" -depth -name "* *" -type f | while read -r file; do
    newfile=$(dirname "$file")/$(basename "$file" | sed -i 's/10.05.04/10_05_04/g')
    echo $newfile
    mv "$file" "$newfile"
done
