#!/bin/bash

# Specify the directory you want to search
start_directory="/media/nikmin/arc/fotoarchive/2013_2001_Упорядоченное"

# Specify the output file to store the names
output_file="space_names.txt"

# Find folder and file names with space characters and write them to the output file
find "$start_directory" -name '* *' -print > "$output_file"


#Make sure to replace "/path/to/your/directory" with the actual path of the directory you want to search for names with spaces.
#Save the script in a file, for example, find_space_names.sh. Then, open a terminal, navigate to the directory where the script is saved, and run the following command to make it executable:
#chmod +x find_space_names.sh
#Finally, you can execute the script by running:
#./find_space_names.sh
#The script will perform a recursive search in the specified directory for files and folders with space characters in their names and write these names to the file specified by output_file (in this case, "space_names.txt"). Each name will be written on a new line in the ​output file for better readability.
