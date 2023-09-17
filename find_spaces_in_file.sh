#!/bin/bash

# Specify the input file to search for spaces
input_file="mail_ru.txt"

# Specify the output file to store lines with spaces
output_file="lines_with_spaces.txt"

rclone lsd mail_ru:/fo_copied/2013_2001_Упорядоченное > mail_ru.txt 

# Find lines with spaces in the input file and write them to the output file
grep " " "$input_file" > "$output_file"
