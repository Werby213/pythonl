import os
import shutil
import tkinter as tk
from tkinter import filedialog


class SorterApp:

    def __init__(self, master):
        self.master = master
        master.title("File Sorter")

        self.source_folder_path = ""
        self.dest_folder_path = ""
        self.extension_folders = {}
        self.extension_entries = []
        self.category_entries = []

        self.source_folder_button = tk.Button(master, text="Select Source Folder", command=self.select_source_folder)
        self.source_folder_button.pack()

        self.dest_folder_button = tk.Button(master, text="Select Destination Folder", command=self.select_dest_folder)
        self.dest_folder_button.pack()

        self.extension_frame = tk.Frame(master)
        self.extension_frame.pack()
        self.add_extension_button = tk.Button(self.extension_frame, text="Add Extension",
                                              command=self.add_extension_entry)
        self.add_extension_button.grid(row=0, column=0, padx=5, pady=5)
        self.extension_label = tk.Label(self.extension_frame, text="Extension")
        self.extension_label.grid(row=0, column=1, padx=5, pady=5)
        self.category_label = tk.Label(self.extension_frame, text="Category")
        self.category_label.grid(row=0, column=2, padx=5, pady=5)

        self.add_extension_entry()

        self.copy_var = tk.BooleanVar()
        self.copy_checkbutton = tk.Checkbutton(master, text="Copy files (leave unchecked to move files)",
                                               variable=self.copy_var)
        self.copy_checkbutton.pack(pady=5)

        self.sort_button = tk.Button(master, text="Sort Files", command=self.sort_files)
        self.sort_button.pack(pady=10)

    def select_source_folder(self):
        self.source_folder_path = filedialog.askdirectory()
        print("Selected source folder:", self.source_folder_path)

    def select_dest_folder(self):
        self.dest_folder_path = filedialog.askdirectory()
        print("Selected destination folder:", self.dest_folder_path)

    def add_extension_entry(self):
        extension_entry = tk.Entry(self.extension_frame)
        extension_entry.grid(row=len(self.extension_entries) + 1, column=1, padx=5, pady=5)
        category_entry = tk.Entry(self.extension_frame)
        category_entry.grid(row=len(self.category_entries) + 1, column=2, padx=5, pady=5)
        self.extension_entries.append(extension_entry)
        self.category_entries.append(category_entry)

    def sort_files(self):
        for i in range(len(self.extension_entries)):
            extension = self.extension_entries[i].get().strip()
            category = self.category_entries[i].get().strip()
            if extension and category:
                self.extension_folders[extension] = os.path.join(self.dest_folder_path, category)

        if not self.source_folder_path:
            print("Please select source folder.")
            return
        if not self.dest_folder_path:
            print("Please select destination folder.")
            return
        if not self.extension_folders:
            print("Please add extensions and categories.")
            return

        for file_name in os.listdir(self.source_folder_path):
            extension = os.path.splitext(file_name)[1]

            if extension not in self.extension_folders:
                continue

            folder_path = self.extension_folders[extension]

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            file_path = os.path.join(folder_path, file_name)
            if self.copy_var.get():
                shutil.copy(os.path.join(self.source_folder_path, file_name), file_path)
            else:
                shutil.move(os.path.join(self.source_folder_path, file_name), file_path)

    print("Sorting completed.")
root = tk.Tk()
app = SorterApp(root)
root.mainloop()