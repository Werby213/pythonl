from tkinter import *
import tkinter.filedialog as fd
import zipfile
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

keywords = ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'None', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield']

root = Tk()
root.geometry("1000x640")
root.title("Notepad -- 1.0 by Egor M")

def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"

def compress_file():
    file_path = fd.askopenfilename()
    if file_path:
        original_size = file_size(file_path)
        original_size_hr = human_readable_size(original_size)
        compressed_file_path = file_path + ".zip"
        with zipfile.ZipFile(compressed_file_path, "w") as compressed_file:
            compressed_file.write(file_path, compress_type=zipfile.ZIP_DEFLATED)
        compressed_size = file_size(compressed_file_path)
        compressed_size_hr = human_readable_size(compressed_size)
        compression_percent = (original_size - compressed_size) / original_size * 100
        result_text.set("Оригинальный размер: " + original_size_hr + "\n" +
                        "Сжатый размер: " + compressed_size_hr + "\n" +
                        "Процент сжатия: " + "{:.2f}".format(compression_percent) + "%")

def extract_file():
    file_path = fd.askopenfilename(filetypes=[("Zip files", "*.zip")])
    if file_path:
        with zipfile.ZipFile(file_path, "r") as compressed_file:
            compressed_file.extractall()
        result_text.set("Файл успешно распакован")

def file_size(file_path):
    return sum(1 for _ in open(file_path, "rb"))

def askopen():
    filepath = fd.askopenfilename(filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if not filepath:
        print("Ничего не выбрано")
        return
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text1.insert(END, text)
def asksave():
    filepath = fd.asksaveasfilename(defaultextension= "txt", filetypes= [("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if not filepath:
        print("Не сохранено")
        return
    with open(filepath, "w") as output_file:
        text = text1.get("1.0", END)
        output_file.write(text)
def replace():
    old = entryold.get()
    new = entrynew.get()
    str = text1.get("1.0", END)
    str = str.replace(old, new)
    text1.delete("1.0", END)
    text1.insert("1.0", str)
def highlight_keywords(event=None):
    text = text1.get("1.0", "end")
    for word in keywords:
        start_index = '1.0'
        while True:
            start_index = text1.search(word, start_index, nocase=1, stopindex=END)
            if not start_index:
                break
            end_index = f'{start_index}+{len(word)}c'
            text1.tag_add('keyword', start_index, end_index)
            start_index = end_index
root = Tk()
root.geometry("1000x640")
root.title("Notepad -- 1.0 by Egor M")

text1 = Text(root, width=1000, height=640)
scrollbar = Scrollbar(root, command=text1.yview)
text1.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
text1.pack(expand=YES, fill=BOTH)

def word_count():
    text = text1.get("1.0", "end")
    words = len(text.split())
    characters = len(text)
    lines = text.count("\n") + 1
    result_text.set(f"Words: {words}\nCharacters: {characters}\nLines: {lines}")

result_text = StringVar()
result_text.set("Words: 0\nCharacters: 0\nLines: 0")
label = Label(root, textvariable=result_text)
label.pack(side=BOTTOM)

text1.bind("<KeyRelease>", highlight_keywords)
text1.focus_set()

def highlight_keywords(event=None):
    text = text1.get("1.0", "end")
    new_text = ""
    for word in text.split():
        if word in keywords:
            new_text += f"\033[91m{word}\033[0m "
        else:
            new_text += f"{word} "
            text1.delete("1.0", "end")
            text1.insert("1.0", new_text)
            word_count()

mainloop()
