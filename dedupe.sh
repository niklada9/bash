#!/bin/bash

if [ -n "$1" ]; then
    target_directory="$1"
    echo $target_directory
else
    echo "replace_spaces.sh путь к целевой директории не указан."
    exit 1
fi

rclone dedupe --by-hash --dedupe-mode oldest $target_directory