import tkinter as tk

def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

def add_to_input(value):
    entry.insert(tk.END, value)

root = tk.Tk()
root.title("Калькулятор")

# Создаем виджет Entry для ввода чисел и выражений
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Создаем кнопки с цифрами и операторами
buttons = [
    {"text": "7", "command": lambda: add_to_input("7")},
    {"text": "8", "command": lambda: add_to_input("8")},
    {"text": "9", "command": lambda: add_to_input("9")},
    {"text": "+", "command": lambda: add_to_input("+")},
    {"text": "4", "command": lambda: add_to_input("4")},
    {"text": "5", "command": lambda: add_to_input("5")},
    {"text": "6", "command": lambda: add_to_input("6")},
    {"text": "-", "command": lambda: add_to_input("-")},
    {"text": "1", "command": lambda: add_to_input("1")},
    {"text": "2", "command": lambda: add_to_input("2")},
    {"text": "3", "command": lambda: add_to_input("3")},
    {"text": "*", "command": lambda: add_to_input("*")},
    {"text": "0", "command": lambda: add_to_input("0")},
    {"text": ".", "command": lambda: add_to_input(".")},
    {"text": "/", "command": lambda: add_to_input("/")},
    {"text": "=", "command": calculate},
]

# Размещаем кнопки на GUI
row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button["text"], padx=40, pady=20, command=button["command"]).grid(row=row, column=col)
    col += 1
    if col == 4:
        col = 0
        row += 1

root.mainloop()
