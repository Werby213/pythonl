import os
import shutil
import tkinter as tk
from tkinter import filedialog

class SortApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Сортировка файлов по расширениям")
        self.master.geometry("600x400")

        # Исходная папка
        self.source_folder_path = tk.StringVar()
        tk.Label(self.master, text="Выберите исходную папку:").pack()
        tk.Entry(self.master, textvariable=self.source_folder_path).pack()
        tk.Button(self.master, text="Выбрать папку", command=self.choose_source_folder).pack()

        # Папка назначения
        self.dest_folder_path = tk.StringVar()
        tk.Label(self.master, text="Выберите папку назначения:").pack()
        tk.Entry(self.master, textvariable=self.dest_folder_path).pack()
        tk.Button(self.master, text="Выбрать папку", command=self.choose_dest_folder).pack()

        # Расширения и категории
        self.extensions_folders = {}
        self.extension_entry = tk.StringVar()
        self.category_entry = tk.StringVar()
        tk.Label(self.master, text="Добавить расширение и категорию:").pack()
        tk.Entry(self.master, textvariable=self.extension_entry).pack()
        tk.Entry(self.master, textvariable=self.category_entry).pack()
        tk.Button(self.master, text="Добавить", command=self.add_extension_category).pack()

        # Список расширений и категорий
        self.extension_category_listbox = tk.Listbox(self.master)
        self.extension_category_listbox.pack()

        # Копирование или перемещение
        self.copy_or_move = tk.StringVar()
        self.copy_or_move.set("Копировать")
        tk.Radiobutton(self.master, text="Копировать", variable=self.copy_or_move, value="Копировать").pack()
        tk.Radiobutton(self.master, text="Переместить", variable=self.copy_or_move, value="Переместить").pack()

        # Кнопка "Сортировать"
        tk.Button(self.master, text="Сортировать", command=self.sort_files).pack()

    def choose_source_folder(self):
        self.source_folder_path.set(filedialog.askdirectory())

    def choose_dest_folder(self):
        self.dest_folder_path.set(filedialog.askdirectory())

    def add_extension_category(self):
        extension = self.extension_entry.get()
        category = self.category_entry.get()

        if extension and category:
            self.extensions_folders[extension] = category
            self.extension_category_listbox.insert(tk.END, f"{extension}: {category}")

    def sort_files(self):
        if not self.extensions_folders:
            tk.messagebox.showerror("Ошибка", "Добавьте хотя бы одно расширение и категорию.")
            return

        source_folder_path = self.source_folder_path.get()
        dest_folder_path = self.dest_folder_path.get()

        if not os.path.exists(source_folder_path):
            tk.messagebox.showerror("Ошибка", "Выбрана некорректная исходная папка.")
            return

        if not os.path.exists(dest_folder_path):
            tk.messagebox.showerror("Ошибка", "Выбрана некорректная папка назначения.")
        return

        for file_name in os.listdir(source_folder_path):
            extension = os.path.splitext(file_name)[1]

            if extension not in self.extensions_folders:
                continue

            folder_path = os.path.join(dest_folder_path, self.extensions_folders[extension])

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            file_path = os.path.join(folder_path, file_name)

            if self.copy_or_move.get() == "Копировать":
                shutil.copy(os.path.join(source_folder_path, file_name), file_path)
            else:
                shutil.move(os.path.join(source_folder_path, file_name), file_path)

        tk.messagebox.showinfo("Сортировка завершена", "Все файлы были успешно отсортированы.")
root = tk.Tk()
app = SortApp(root)
root.mainloop()
