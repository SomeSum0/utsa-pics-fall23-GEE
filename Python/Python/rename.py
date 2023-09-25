import os

def rename_images(folder_path, base_name):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)
    image_files = [file for file in file_list if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # Sort the image files alphabetically
    image_files.sort()

    # Rename images sequentially
    for index, old_name in enumerate(image_files):
        extension = os.path.splitext(old_name)[1]
        new_name = f"{base_name}_{index + 1:03d}{extension}"
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")

if __name__ == "__main__":
    folder_path = "C:\\Python"
    base_name = "IMAGE_"
    rename_images(folder_path, base_name)
