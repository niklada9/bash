#!/bin/bash

# Set the source directory and destination directory on Yandex Disk
source_dir="/media/nikmin/arc/fotoarchive/2013_2001_Упорядоченное"
destination_dir="ya:/onedrv/fo/2013_2001_Упорядоченное"

# List all the folders in the source directory
folders=$(find "$source_dir" -mindepth 1 -maxdepth 1 -type d)

# Loop through each folder and copy it to the corresponding folder on Yandex Disk
for folder in $folders; do
    # Extract the folder name from the path
    folder_name=$(basename "$folder")
    
    # Construct the destination folder path on Yandex Disk
    destination_folder="$destination_dir/$folder_name"
    
    # Use rcopy to copy the folder recursively to Yandex Disk
    rclone copy "$folder" "$destination_folder"
    
    # Print the status of the copy operation
    echo "Copied $folder_name to $destination_folder"
done

#Make sure to replace the /path/to/local/source with the actual path to your source directory, and /path/to/yandex/disk with the appropriate path of your Yandex Disk.

#Save the script in a file, for example, copy_to_yandex.sh. Then, open a terminal, navigate to the directory where the script is saved, and run the following command to make it executable:

#chmod +x copy_to_yandex.sh

#Finally, you can execute the script by running:

#./copy_to_yandex.sh
