#!/bin/bash

# Set the necessary variables
ACCESS_KEY="your_access_key"
SECRET_KEY="your_secret_key"
BUCKET="your_bucket_name"

# Specify the directory you want to start renaming from
start_directory="your_directory"

# Recursively navigate through the directory and rename files, folders, and paths
find "$start_directory" -depth -name "* *" -type d | while read -r dir; do
    newdir=$(dirname "$dir")/$(basename "$dir" | tr ' ' '_')
    curl -X MOVE -H "Authorization: Bearer $ACCESS_KEY:$SECRET_KEY" "https://storage.yandexcloud.net/$BUCKET$(realpath --relative-to="$start_directory" "$dir")" -H "Destination: /$BUCKET$(realpath --relative-to="$start_directory" "$newdir")"
done

find "$start_directory" -depth -name "* *" -type f | while read -r file; do
    newfile=$(dirname "$file")/$(basename "$file" | tr ' ' '_')
    curl -X MOVE -H "Authorization: Bearer $ACCESS_KEY:$SECRET_KEY" "https://storage.yandexcloud.net/$BUCKET$(realpath --relative-to="$start_directory" "$file")" -H "Destination: /$BUCKET$(realpath --relative-to="$start_directory" "$newfile")"
done

find "$start_directory" -depth -name "* *" -type l | while read -r link; do
    newlink=$(readlink "$file" | tr ' ' '_')
    curl -X MOVE -H "Authorization: Bearer $ACCESS_KEY:$SECRET_KEY" "https://storage.yandexcloud.net/$BUCKET$(realpath --relative-to="$start_directory" "$link")" -H "Destination: /$BUCKET$(realpath --relative-to="$start_directory" "$newlink")"
done
