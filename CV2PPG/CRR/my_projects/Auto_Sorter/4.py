import os
import shutil
import tkinter as tk
from tkinter import filedialog
import configparser


class SorterApp:

    CONFIG_FILE = "config.ini"

    def __init__(self, master):
        self.master = master
        master.title("File Sorter")

        # Load settings from config file if it exists
        self.config = configparser.ConfigParser()
        if os.path.isfile(self.CONFIG_FILE):
            self.config.read(self.CONFIG_FILE)
            self.source_folder_path = self.config.get("Settings", "source_folder_path", fallback="")
            self.dest_folder_path = self.config.get("Settings", "dest_folder_path", fallback="")
            self.extension_folders = dict(self.config.items("ExtensionFolders"))
        else:
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

        self.load_extension_entries()

        self.copy_var = tk.BooleanVar()
        self.copy_checkbutton = tk.Checkbutton(master, text="Copy files (leave unchecked to move files)",
                                               variable=self.copy_var)
        self.copy_checkbutton.pack(pady=5)

        self.sort_button = tk.Button(master, text="Sort Files", command=self.sort_files)
        self.sort_button.pack(pady=10)

    def select_source_folder(self):
        self.source_folder_path = filedialog.askdirectory()
        print("Selected source folder:", self.source_folder_path)
        self.save_config()

    def select_dest_folder(self):
        self.dest_folder_path = filedialog.askdirectory()
        print("Selected destination folder:", self.dest_folder_path)
        self.save_config()

    def add_extension_entry(self):
        extension_entry = tk.Entry(self.extension_frame)
        extension_entry.grid(row=len(self.extension_entries) + 1, column=1, padx=5, pady=5)
        category_entry = tk.Entry(self.extension_frame)
        category_entry.grid(row=len(self.category_entries) + 1, column=2, padx=5, pady=5)
        self.extension_entries.append(extension_entry)
        self.category_entries.append(category_entry)
        self.save_config()

    def load_extension_entries(self):
        for extension, category in self.extension_folders.items():
            extension_entry = tk.Entry(self.extension_frame)
            extension_entry.grid(row=len(self.extension_entries) + 1, column=1, padx=5, pady=5)
            extension_entry.insert(0, extension)
            category_entry = tk.Entry(self.extension_frame)
            category_entry.grid(row=len(self.category_entries) + 1, column=2, padx=5, pady=5)
            category_entry.insert(0, category)
            self.extension_entries.append(extension_entry)
            self.category_entries.append(category_entry)

    def save_config(self):
        self.config["Settings"] = {
            "source_folder_path": self.source_folder_path,
            "dest_folder_path": self.dest_folder_path
        }
        self.config["ExtensionFolders"] = {}
        for i in range(len(self.extension_entries)):
            extension = self.extension_entries[i].get().lower()
            category = self.category_entries[i].get()
            if extension != "" and category != "":
                self.config["ExtensionFolders"][extension] = category
        with open(self.CONFIG_FILE, "w") as configfile:
            self.config.write(configfile)

    def sort_files(self):
        if not self.source_folder_path or not self.dest_folder_path:
            print("Please select source and destination folders.")
            return
        if not self.extension_folders:
            print("Please add extensions and categories.")
            return

        for file in os.listdir(self.source_folder_path):
            if os.path.isfile(os.path.join(self.source_folder_path, file)):
                file_extension = os.path.splitext(file)[1].lower()
                if file_extension in self.extension_folders:
                    category_folder = os.path.join(self.dest_folder_path, self.extension_folders[file_extension])
                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)
                    if self.copy_var.get():
                        shutil.copy2(os.path.join(self.source_folder_path, file), category_folder)
                    else:
                        shutil.move(os.path.join(self.source_folder_path, file), category_folder)
        print("Files sorted successfully!")
root = tk.Tk()
app = SorterApp(root)
root.mainloop()