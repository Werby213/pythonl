import os
import shutil
import tkinter as tk
from tkinter import filedialog


def browse_button():
    global source_folder_path
    source_folder_path = filedialog.askdirectory()
    source_folder_path_label.config(text=source_folder_path)


def destination_button():
    global destination_folder_path
    destination_folder_path = filedialog.askdirectory()
    destination_folder_path_label.config(text=destination_folder_path)


def add_extension():
    extension = extension_entry.get()
    folder_path = folder_entry.get()
    extensions_folders[extension] = folder_path
    extension_entry.delete(0, tk.END)
    folder_entry.delete(0, tk.END)


def sort_files():
    for file_name in os.listdir(source_folder_path):
        extension = os.path.splitext(file_name)[1]

        if extension not in extensions_folders:
            continue

        folder_path = extensions_folders[extension]

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_path = os.path.join(folder_path, file_name)

        shutil.move(os.path.join(source_folder_path, file_name), file_path)

    sort_complete_label.config(text="Сортировка завершена.")


root = tk.Tk()

source_folder_path = ""
destination_folder_path = ""
extensions_folders = {".click": "D:/1212"}

# Source Folder
source_folder_label = tk.Label(root, text="Исходная папка: ")
source_folder_label.grid(column=0, row=0)

source_folder_path_label = tk.Label(root, text="")
source_folder_path_label.grid(column=1, row=0)

browse_button = tk.Button(text="Выберите исходную папку", command=browse_button)
browse_button.grid(column=2, row=0)

# Destination Folder
destination_folder_label = tk.Label(root, text="Папка назначения: ")
destination_folder_label.grid(column=0, row=1)

destination_folder_path_label = tk.Label(root, text="")
destination_folder_path_label.grid(column=1, row=1)

destination_button = tk.Button(text="Выберите папку назначения", command=destination_button)
destination_button.grid(column=2, row=1)

# Add Extension and Folder
extension_label = tk.Label(root, text="Добавить расширение и папку")
extension_label.grid(column=0, row=2)

extension_entry = tk.Entry(root)
extension_entry.grid(column=1, row=2)

folder_entry = tk.Entry(root)
folder_entry.grid(column=2, row=2)

add_extension_button = tk.Button(text="Добавить", command=add_extension)
add_extension_button.grid(column=3, row=2)

# Sort Files
sort_files_button = tk.Button(text="Сортировать файлы", command=sort_files)
sort_files_button.grid(column=1, row=3)

sort_complete_label = tk.Label(root, text="")
sort_complete_label.grid(column=1, row=4)

root.mainloop()