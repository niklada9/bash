#!/bin/bash

# Specify the directory you want to search
start_directory="/media/nikmin/arc/fotoarchive/2013_2001_Упорядоченное"

# Specify the output file to store the names
output_file="space_names.txt"

# Find folder and file names with space characters and write them to the output file
find "$start_directory" -name '* *' -mindepth 1 -maxdepth 1 -print > "$output_file"

