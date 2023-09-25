import os
import shutil

# Define the source folder where your files are located.
source_folder = '/path/to/source/folder'

# Create a list of file ranges and corresponding folder names.
file_ranges = [
    (1, 10, "01"),
    (11, 20, "02"),
    (21, 30, "03"),
    (31, 40, "04"),
    (41, 51, "05")
]

# Function to move files to the appropriate subfolder.
def organize_files(source, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    for filename in os.listdir(source):
        if filename.endswith(".jpg"):
            file_number = int(filename.split("_")[1].split(".")[0])
            for start, end, folder_name in file_ranges:
                if start <= file_number <= end:
                    destination = os.path.join(destination_folder, folder_name, filename)
                    shutil.move(os.path.join(source, filename), destination)
                    break

# Iterate through the source folder and organize the files.
for start, end, folder_name in file_ranges:
    organize_files(source_folder, os.path.join(source_folder, folder_name))

