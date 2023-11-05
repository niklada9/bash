# You can use the following Python script to recursively replace space signs with underscore signs
# in folder and file names while handling naming collisions by adding _1, _2, etc. to the new names when necessary.
# Make sure you have a backup of your data before running such a script, as it can modify file and folder names.
# This script uses os.walk to traverse through the directory structure, renames both directories and files,
# and handles naming collisions by adding _1, _2, etc. to the new names. Please exercise caution when using this script,
# especially on important directories, as it can change file and folder names.
# !!! Make sure you have a backup of your data before running it.

import sys
import os

def replace_spaces_with_underscores(path):
    for root, dirs, files in os.walk(path):
        for d in dirs:
            original_dir = os.path.join(root, d)
            new_dir = os.path.join(root, d.replace(" ", "_"))
            if original_dir != new_dir and os.path.exists(new_dir):
                i = 1
                while os.path.exists(new_dir):
                    i += 1
                    new_dir = os.path.join(root, f"{d.replace(' ', '_')}_{i}")
            os.rename(original_dir, new_dir)

        for f in files:
            original_file = os.path.join(root, f)
            new_file = os.path.join(root, f.replace(" ", "_"))
            if original_file != new_file and os.path.exists(new_file):
                i = 1
                while os.path.exists(new_file):
                    i += 1
                    base_name, extension = os.path.splitext(f)
                    new_file = os.path.join(root, f"{base_name.replace(' ', '_')}_{i}{extension}")
            os.rename(original_file, new_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
    print("Usage: python3 replace_spaces_with_underscores.py /path/to/dir")
    sys.exit(1)
    directory_path = sys.argv[1]
    # directory_path = input("Enter the directory path: ")
    # directory_path = "/media/nikmin/arc/Photos"
    if os.path.exists(directory_path):
        replace_spaces_with_underscores(directory_path)
        print("Spaces replaced with underscores successfully.")
    else:
        print("Directory not found.")


