#!/bin/bash
#This is an example of a Bash script that replaces spaces with underscores in file, folder, and path names:

# Specify the directory you want to start renaming from
start_directory="/media/nikmin/arc/fotoarchive/2013_2001_Упорядоченное"

# Recursively navigate through the directory and rename files, folders, and paths
find "$start_directory" -depth -name "* *" -type d | while read -r dir; do
    newdir=$(dirname "$dir")/$(basename "$dir" | tr ' ' '_')
    mv "$dir" "$newdir"
    echo “Sdir”
done
#find "$start_directory" -depth -name "* *" -type f | while read -r file; do
#    newfile=$(dirname "$file")/$(basename "$file" | tr ' ' '_')
#    mv "$file" "$newfile"
#done
#find "$start_directory" -depth -name "* *" -type l | while read -r link; do
#    newlink=$(readlink "$file" | tr ' ' '_')
#    ln -sf "$newlink" "$link"
#done
#Make sure to replace "/path/to/your/directory" with the actual path of the directory you want to start renaming from.
#Save the script in a file, for example, replace_spaces.sh. Then, open a terminal, navigate to the directory where the script is saved, and run the following command to make it executable:
#chmod +x replace_spaces.sh
#Finally, you can execute the script by running:
#./replace_spaces.sh
#The script will recursively search for files, folders, and links with spaces in their names within the specified ​directory and replace the spaces with underscores using the tr command. Please exercise caution when running this script and make sure to test it on a backup directory before using it on critical data.
