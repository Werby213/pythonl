import tkinter.ttk
from tkinter import *
from tkinter import ttk
import tkinter.font as Font
import tkinter.filedialog as fd
from termcolor import colored
import subprocess
import time
import multiprocessing
root = Tk()
font_size = 11
debug = False
start_message = "почему здесь не работает подсчет символов, слов и строк? подсчет идет только при запуске программы с тестовым текстом."
programming_language = ("Python", "C", "C++", "C#", "Pascal", "Basic")
fonts = ("Arial", "Crixus", "Segoe", "Consolas")
font = fonts[0]
root.geometry("1920x1080+100+100")
root.title("Notepad -- 1.0 by Egor M")
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
    filepath = fd.asksaveasfilename(defaultextension="txt",
                                    filetypes=[("Текстовые файлы", "*.txt", "*.py"), ("Все файлы", "*.*")])
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
def word_count():
    text = text1.get("1.0", "end")
    words = len(text.split())
    characters = len(text) - 1
    lines = text.count("\n")
    count.set(f"Слов: {words} Символов: {characters} Строк: {lines}")
def increase_font_size():
    global font_size
    font_size += 1
    font_size_text.set(font_size)
    text1.update()
    text1.tag_add("bigfont", "1.0", "end")
    text1.tag_config("sel", font=(font, font_size))
    text1.tag_configure("bigfont", font=(font, font_size))
    select_font()

    if debug == True:
        print(font_size, font)
def decrease_font_size():
    global font_size
    font_size -= 1
    font_size_text.set(font_size)
    text1.tag_add("bigfont", "1.0", "end")
    text1.tag_config("sel", font=(font, font_size))
    text1.tag_configure("bigfont", font=(font, font_size))
    text1.update()
    select_font()
    if debug == True:
        print(font_size, font)
def run_code():
    global output, error
    text = text1.get("1.0", "end")
    process = subprocess.Popen([select_programming_lang.get(), "-c", text], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if debug == True:
        print(output.decode("utf-8"))
        if error:
            print(colored("Subprocces", 'yellow'))
            print(colored(error.decode("utf-8"), 'red'))
def refresh_console(text2):
    text2.config(state=NORMAL)
    text2.delete("1.0", END)
    output_text = output.decode("utf-8")
    if error:
        output_text = colored("Subprocces", 'yellow') + colored(error.decode("utf-8"), 'red')
    text2.insert(INSERT, output_text)
    text2.config(state=DISABLED)
def open_console_window():
    global output, error
    console_window = Toplevel(root)
    console_window.title("Python Console Subprocces")
    console_window.geometry("1000x800+880+100")
    frame_console = LabelFrame(console_window, bg='lightgray', bd=5, relief=RAISED, text="Python консоль")
    text2 = Text(console_window, font=font + str(font_size), fg="white", bg="black", wrap=WORD, width=140, height=39)
    text2.place(x=0, y=100)
    output_text = output.decode("utf-8") or colored("Subprocces", 'yellow') and colored(error.decode("utf-8"), 'red')
    text2.config(state=NORMAL)
    text2.delete("1.0", END)
    text2.insert("1.0", output_text)
    text2.config(state=DISABLED)
    refresh_console(text2)
    console_window.mainloop()
def select_font():
    global font
    font = sel_font.get()
def clear_entry_new(event):
    if entrynew.get() == "на что заменить":
        entrynew.delete(0, 'end')
def clear_entry_old(event):
    if entryold.get() == "что заменить":
        entryold.delete(0, 'end')
frame = LabelFrame(root, bg='lightgray', bd=5, relief=RAISED, text="работа с текстовыми файлами",)
frame.grid(row=0, column=0, sticky="nsew")
frame_archive = LabelFrame(root, bg='lightgray', bd=5, relief=RAISED, text="placeholder")
frame_ide = LabelFrame(root, bg='lightgray', bd=5, relief=RAISED, text="работа с программным кодом")
frame_count = LabelFrame(root, bg='gray', bd=5)
text1 = Text(root, font=font  + str(font_size), fg="white", bg="black", wrap=WORD, width=140, height=39)
text1.grid(row=1, column=0, sticky="nsew")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
text1.tag_config("sel", font=(font, font_size))
text1.tag_add("bigfont", "1.0", "end")
text1.insert("1.0", start_message, "font_size")
# установка параметра шрифта
font_size_text = StringVar()
font_size_entry = Entry(frame, textvariable= font_size_text, width=4)
font_size_text.set(9)
font_size_entry.place(x=195, y=8)
sel_font= ttk.Combobox(frame, values=fonts)
sel_font.current(0)
sel_font.place(x=246, y=7)
# модуль редактора текста
#scroll = Scrollbar(root, command=text1.yview)
#scroll.grid(row=0, column=2, sticky="nsew")
btn_up = Button(frame, text="↑", command=increase_font_size)
btn_down = Button(frame, text="↓", command=decrease_font_size)
btn_up.place(x=226, y=5)
btn_down.place(x=176, y=5)
btn_open = Button(frame, text='Открыть', height=1, width=7, fg='black', command=askopen)
btn_saveas = Button(frame, text='Coxpанить как...', height=1, width=13, fg='black', command=asksave)
btn_replace = Button(frame, text='Заменить', height=2, width=7, fg='black', command=replace)
entryold = Entry(frame, width=50)
entryold.insert(0, "что заменить")
entryold.bind("<FocusIn>", clear_entry_old)
entrynew = Entry(frame, width=50)
entrynew.insert(0, "на что заменить")
entrynew.bind("<FocusIn>", clear_entry_new)
btn_open.place(x=5, y=5)
btn_saveas.place(x=70, y=5)
btn_replace.place(x=321, y=34)
entryold.place(x=5, y=35)
entrynew.place(x=5, y=55)
# статистика текстого поля
count = StringVar()
count1 = Label(root, textvariable=count)
count1.place(x=1000, y=10)
word_count()
# модуль IDE
frame_ide.place(x=700, y=0, width=282, height=100)
btn_start_code = Button(frame_ide, text='Выполнить код', height=1, width=12, fg='black', command=run_code)
btn_start_code.place(x=5, y=30)
select_programming_lang = ttk.Combobox(frame_ide, values=programming_language)
select_programming_lang.current(0)
select_programming_lang.place(x=5, y=5)
btn_console = Button(frame_ide, text="Python консоль", command=open_console_window)
btn_console.place(x=105, y=30)
root.update_idletasks()
run_code()
text1.bind('<KeyRelease>', lambda event: word_count())
open_console_window()
root.mainloop()