import os
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import configparser
import time

class SorterApp:
    file_count = 0
    CONFIG_FILE = "config.ini"

    def __init__(self, master):
        self.master = master
        master.title("Сортировщик файлов")

        # Load settings from config file if it exists


        self.extension_entries = []
        self.category_entries = []

        self.folder_select = tk.Frame(master)
        self.folder_select.pack()
        self.source_folder_button = tk.Button(self.folder_select, text="Выберите исходную папку", command=self.select_source_folder)
        self.source_folder_button.grid(row=0, column=0, padx=0, pady=5)

        self.dest_folder_button = tk.Button(self.folder_select, text="Выберите папку назначения", command=self.select_dest_folder)
        self.dest_folder_button.grid(row=1, column=0, padx=0, pady=5)

        self.source_folder_entry = tk.Entry(self.folder_select)
        self.source_folder_entry.grid(row=0, column=1, padx=20, pady=5)

        self.dest_folder_entry = tk.Entry(self.folder_select)
        self.dest_folder_entry.grid(row=1, column=1, padx=20, pady=5)

        self.config = configparser.ConfigParser()
        if os.path.isfile(self.CONFIG_FILE):
            self.config.read(self.CONFIG_FILE)
            self.source_folder_path = self.config.get("Settings", "source_folder_path", fallback="")
            self.source_folder_entry.insert(0, self.source_folder_path)

            self.dest_folder_path = self.config.get("Settings", "dest_folder_path", fallback="")
            self.dest_folder_entry.insert(0, self.dest_folder_path)
            self.extension_folders = dict(self.config.items("ExtensionFolders"))
        else:
            self.source_folder_path = ""
            self.dest_folder_path = ""
            self.extension_folders = {}


        self.extension_frame = tk.Frame(master)
        self.extension_frame.pack()
        self.add_extension_button = tk.Button(self.extension_frame, text="Добавить расширение",
                                              command=self.add_extension_entry)
        self.add_extension_button.grid(row=0, column=0, padx=5, pady=5)
        self.extension_label = tk.Label(self.extension_frame, text="Расширение")
        self.extension_label.grid(row=0, column=1, padx=5, pady=5)
        self.category_label = tk.Label(self.extension_frame, text="Категория")
        self.category_label.grid(row=0, column=2, padx=5, pady=5)

        self.load_extension_entries()

        self.copy_var = tk.BooleanVar()
        self.copy_checkbutton = tk.Checkbutton(master, text="Копировать файлы (оставьте не отмеченным для перемещения файлов)",
                                               variable=self.copy_var)
        self.copy_checkbutton.pack(pady=5)

        self.overwrite_var = tk.BooleanVar(value=False)
        self.overwrite_checkbox = tk.Checkbutton(master, text="Перезаписать файлы, если они уже существуют",
                                                 variable=self.overwrite_var, onvalue=True, offvalue=False)
        self.overwrite_checkbox.pack(pady=5)

        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack()
        self.sort_button = tk.Button(self.buttons_frame, text="Сортировка файлов", command=self.sort_files)
        self.sort_button.place(x= 0, y=10)

        self.save_config_button = tk.Button(self.buttons_frame, text="Сохранить конфиг", command=self.save_config)
        self.save_config_button.place(x= 0, y=40)

        self.clear_config_button  = tk.Button(self.buttons_frame, text="Очистить конфиг", command=self.clear_config)
        self.clear_config_button.place(x= 0, y=70)

        self.information = tk.Label(self.buttons_frame, textvariable="11")
        self.information.place(x= 0, y=10)

        self.progress_bar = ttk.Progressbar(self.buttons_frame, orient='horizontal', length=300, mode='determinate')
        self.progress_bar.pack(pady=100, padx=0)

    def select_source_folder(self):
        self.source_folder_path = filedialog.askdirectory()
        self.source_folder_entry.insert(0, self.source_folder_path)
        print("Выбранная исходная папка:", self.source_folder_path)
        self.save_config()

    def select_dest_folder(self):
        self.dest_folder_path = filedialog.askdirectory()
        self.dest_folder_entry.insert(0, self.dest_folder_path)
        print("Выбранная папка назначения:", self.dest_folder_path)
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

    def clear_config(self):
        self.extension_entries = []
        self.category_entries = []

        self.config["Settings"] = {
            "source_folder_path": "",
            "dest_folder_path": ""
        }
        self.config["ExtensionFolders"] = {}
        for i in range(len(self.extension_entries)):
            extension = ""
            category = ""
            if extension != "" and category != "":
                self.config["ExtensionFolders"][extension] = category
        with open(self.CONFIG_FILE, "w") as configfile:
            self.config.write(configfile)


    def sort_files(self):
        self.progress_bar.start()
        if not self.source_folder_path or not self.dest_folder_path:
            print("Пожалуйста, выберите исходную и конечную папки.")
            return
        if not self.extension_folders:
            print("Пожалуйста, добавьте расширения и категории.")
            return

        for file in os.listdir(self.source_folder_path):
            try:
                self.progress_bar['value'] = int(self.file_count) + 1
                print(file)
            except ValueError:
                print("Invalid file name: ", file)

            for file in os.listdir(self.source_folder_path):
                self.file_count +=1
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
        print("Файлы успешно отсортированы!")
        self.progress_bar.stop()
root = tk.Tk()
app = SorterApp(root)
root.mainloop()