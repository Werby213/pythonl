import tkinter.ttk
from tkinter import *
from tkinter import ttk
import tkinter.font as Font
import tkinter.filedialog as fd
from termcolor import colored
import subprocess
from tkinterhtml import HtmlFrame
import time
import multiprocessing
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import jedi

class Notepad:
    def __init__(self):
        self.root = Tk()
        self.font_size = 10
        self.debug = False
        self.start_message = "Проверка"
        self.programming_language = ("Python", "C", "C++", "C#", "Pascal", "Basic", "Html")
        self.fonts = ("Arial", "Crixus", "Segoe", "Consolas")
        self.font = self.fonts[0]
        self.root.geometry("1920x1080+100+100")
        self.root.title("Notepad -- 1.0 by Egor M")

        self.frame = LabelFrame(self.root, bg='lightgray', bd=5, relief=RAISED, text="работа с текстовыми файлами")
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.text1 = Text(self.frame, font=self.font + str(self.font_size), fg="white", bg="black", wrap=WORD)
        self.text1.pack(fill="both", expand=True, padx=0, pady=(82, 0))
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.scroll = Scrollbar(self.root, command=self.text1.yview)
        self.scroll.grid(row=0, column=2, sticky="nsew")
        self.text1.tag_config("sel", font=(self.font, self.font_size))
        self.text1.tag_add("bigfont", "1.0", "end")
        self.text1.insert("1.0", self.start_message, "font_size")

        self.font_size_text = StringVar()
        self.font_size_entry = Entry(self.frame, textvariable=self.font_size_text, width=4)
        self.font_size_text.set(self.font_size)
        self.font_size_entry.place(x=195, y=8)
        self.sel_font = ttk.Combobox(self.frame, values=self.fonts)
        self.sel_font.current(0)
        self.sel_font.place(x=246, y=7)

        self.btn_up = Button(self.frame, text="↑", command=self.increase_font_size)
        self.btn_down = Button(self.frame, text="↓", command=self.decrease_font_size)
        self.btn_up.place(x=226, y=5)
        self.btn_down.place(x=176, y=5)
        self.btn_open = Button(self.frame, text='Открыть', height=1, width=7, fg='black', command=self.askopen)
        self.btn_saveas = Button(self.frame, text='Coxpанить как...', height=1, width=13, fg='black',
                                 command=self.asksave)
        self.btn_replace = Button(self.frame, text='Заменить', height=2, width=7, fg='black', command=self.replace)
        self.entryold = Entry(self.frame, width=50)
        self.entryold.insert(0, "что заменить")
        self.entryold.bind("<FocusIn>", self.clear_entry_old)
        self.entrynew = Entry(self.frame, width=50)
        self.entrynew.insert(0, "на что заменить")
        self.entrynew.bind("<FocusIn>", self.clear_entry_new)
        self.btn_open.place(x=5, y=5)
        self.btn_saveas.place(x=70, y=5)
        self.btn_replace.place(x=321, y=34)
        self.entryold.place(x=5, y=35)
        self.entrynew.place(x=5, y=55)
        self.count = StringVar()
        self.count1 = Label(self.root, textvariable=self.count)
        self.count1.place(x=1000, y=10)
        self.word_count()
        self.btn_start_code = Button(self.frame, text='Выполнить код', height=1, width=12, fg='black',
                                     command=self.run_code)
        self.btn_start_code.place(x=600, y=50)
        self.select_programming_lang = ttk.Combobox(self.frame, values=self.programming_language)
        self.select_programming_lang.current(0)
        self.select_programming_lang.place(x=450, y=5)
        self.btn_console = Button(self.frame, text="Обновить подсветку", command=self.highlight_syntax)
        self.btn_console.place(x=600, y=20)
        self.root.update_idletasks()
        self.run_code()
        self.text1.bind('<KeyRelease>', lambda event: self.word_count())
        self.btn_start_code.bind('<KeyRelease>', lambda event: self.run_code())

        self.root.mainloop()  # Добавлен вызов mainloop() для окна Tk

    def autocomplete(self):
        text = self.text1.get("1.0", "insert")
        line, column = self.text1.index("insert").split(".")
        script = jedi.Script(text, int(line), int(column), self.select_programming_lang.get())
        completions = script.completions()
        # Вывод completions в нужном вам формате (например, в выпадающем списке или всплывающем окне)

    def highlight_syntax(self):
        text = self.text1.get("1.0", END)
        language = self.select_programming_lang.get()
        lexer = get_lexer_by_name(language)
        formatter = HtmlFormatter(style="colorful")
        highlighted_code = highlight(text, lexer, formatter)
        self.text1.delete("1.0", END)
        self.text1.insert(END, highlighted_code)

        # Вывод highlighted_code в нужный вам формат (например, в WebView или в файл HTML)

    def file_size(self, file_path):
        return sum(1 for _ in open(file_path, "rb"))

    def askopen(self):
        filepath = fd.askopenfilename(filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
        if not filepath:
            print("Ничего не выбрано")
            return
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.text1.insert(END, text)

    def asksave(self):
        filepath = fd.asksaveasfilename(defaultextension="txt",
                                        filetypes=[("Текстовые файлы", "*.txt", "*.py"), ("Все файлы", "*.*")])
        if not filepath:
            print("Не сохранено")
            return
        with open(filepath, "w") as output_file:
            text = self.text1.get("1.0", END)
            output_file.write(text)

    def replace(self):
        old = self.entryold.get()
        new = self.entrynew.get()
        text = self.text1.get("1.0", END)
        text = text.replace(old, new)
        self.text1.delete("1.0", END)
        self.text1.insert("1.0", text)

    def word_count(self):
        text = self.text1.get("1.0", "end")
        words = text.count(" ") + 1
        characters = len(text.replace(" ", "")) - 1
        lines = text.count("\n")
        self.count.set(f"Слов: {words} Символов: {characters} Строк: {lines}")

    def increase_font_size(self):
        self.font_size += 1
        self.font_size_text.set(self.font_size)
        self.text1.update()
        self.text1.tag_add("bigfont", "1.0", "end")
        self.text1.tag_config("sel", font=(self.font, self.font_size))
        self.text1.tag_configure("bigfont", font=(self.font, self.font_size))
        self.select_font()

        if self.debug == True:
            print(self.font_size, self.font)

    def decrease_font_size(self):
        self.font_size -= 1
        self.font_size_text.set(self.font_size)
        self.text1.tag_add("bigfont", "1.0", "end")
        self.text1.tag_config("sel", font=(self.font, self.font_size))
        self.text1.tag_configure("bigfont", font=(self.font, self.font_size))
        self.text1.update()
        self.select_font()
        if self.debug == True:
            print(self.font_size, self.font)

    def run_code(self):
        text = self.text1.get("1.0", "end")
        process = subprocess.Popen([self.select_programming_lang.get(), "-c", text], stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        self.output, self.error = process.communicate()
        if self.debug == True:
            print(self.output.decode("utf-8"))
            if self.error:
                print(colored("Subprocces", 'yellow'))
                print(colored(self.error.decode("utf-8"), 'red'))

    def refresh_console(self, text2):
        text2.config(state=NORMAL)
        text2.delete("1.0", END)
        output_text = self.output.decode("utf-8")
        if self.error:
            output_text = colored("Subprocces", 'yellow') + colored(self.error.decode("utf-8"), 'red')
        text2.insert(INSERT, output_text)
        text2.config(state=DISABLED)

    def open_console_window(self):
        console_window = Toplevel(self.root)
        console_window.title("Python Console Subprocces")
        console_window.geometry("1280x800+880+100")
        frame_console = LabelFrame(console_window, bg='lightgray', bd=5, relief=RAISED, text="Python консоль")
        text2 = Text(console_window, font=self.font + str(self.font_size), fg="white", bg="black", wrap=WORD, width=140,
                     height=39)
        text2.place(x=0, y=100)
        btn_start_code = Button(console_window, text='Выполнить код', height=1, width=12, fg='black',
                                command=self.run_code)
        btn_start_code.place(x=10, y=10)
        btn_start_code.bind('<KeyRelease>', lambda event: self.refresh_console())
        output_text = self.output.decode("utf-8") or colored("Subprocces", 'yellow') and colored(
            self.error.decode("utf-8"), 'red')
        text2.config(state=NORMAL)
        text2.delete("1.0", END)
        text2.insert("1.0", output_text)
        text2.config(state=DISABLED)
        self.refresh_console(text2)
        console_window.mainloop()

    def select_font(self):
        self.font = self.sel_font.get()

    def clear_entry_new(self, event):
        if self.entrynew.get() == "на что заменить":
            self.entrynew.delete(0, 'end')

    def clear_entry_old(self, event):
        if self.entryold.get() == "что заменить":
            self.entryold.delete(0, 'end')


Notepad()
