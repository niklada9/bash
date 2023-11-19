#!/bin/bash

if [ -n "$1" ]; then
    target_directory="$1"
    echo "$target_directory"
else
    echo "replace_spaces.sh путь к целевой директории не указан."
    exit 1
fi

rclone dedupe --by-hash --dedupe-mode oldest --log-file=/media/nikmin/arc/dedupe.txt "$target_directory"
echo "дедуплицировано в директории ${target_directory}:" >> /media/nikmin/arc/log.txt
wc -l /media/nikmin/arc/dedupe.txt >> /media/nikmin/arc/log.txt
# shellcheck disable=SC2188
> "/media/nikmin/arc/dedupe.txt"

