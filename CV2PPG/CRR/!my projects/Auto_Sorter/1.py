import os
import shutil

source_folder_path = "D:/test1"

extensions_folders = {
    ".click": "D:/1212"
}

for file_name in os.listdir(source_folder_path):
    extension = os.path.splitext(file_name)[1]

    if extension not in extensions_folders:
        continue

    folder_path = extensions_folders[extension]

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, file_name)

    shutil.move(os.path.join(source_folder_path, file_name), file_path)

print("Сортировка завершена.")
