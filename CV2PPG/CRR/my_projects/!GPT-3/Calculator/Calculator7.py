import tkinter
from tkinter import *
import matplotlib.pyplot as plt
import math

# Создание окна
root = Tk()
root.title("Calculator")

# Для ввода чисел
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Функция для отображения результата вычислений
def button_click(number):
    # Удаляем старое значение и заменяем его новым
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# Функция для очистки поля
def clear():
    e.delete(0, END)


# Задаем функцию для вычисления результата
def add():
    second_number = e.get()
    e.delete(0, END)

    if math_operator == "add":
        e.insert(0, f_num + float(second_number))
    if math_operator == "subtract":
        e.insert(0, f_num - float(second_number))
    if math_operator == "multiply":
        e.insert(0, f_num * float(second_number))
    if math_operator == "divide":
        e.insert(0, f_num / float(second_number))


# Функция для задания типа вычисления и первого числа
def button_math(operator):
    global f_num
    global math_operator
    math_operator = operator
    f_num = float(e.get())
    e.delete(0, END)


# Функция для вычисления квадратного корня
def square_root():
    first_number = e.get()
    e.delete(0, END)
    e.insert(0, math.sqrt(float(first_number)))


# Функция для вычисления тригонометрических функций
def trigonometric_functions(func):
    first_number = e.get()
    e.delete(0, END)
    if func == "sin":
        e.insert(0, math.sin(float(first_number)))
    if func == "cos":
        e.insert(0, math.cos(float(first_number)))
    if func == "tan":
        e.insert(0, math.tan(float(first_number)))


# Функция для подсчета степеней
def power_function():
    first_number = e.get()
    e.delete(0, END)
    e.insert(0, math.pow(float(first_number), 2))


# Функция для прорисовки графика
def graph():
    x = []
    y = []
    num = e.get()
    # Создаем лист значений x и y
    for i in range(int(num)):
        x.append(i)
        y.append(i * i)
    # Прорисовываем график
    plt.plot(x, y, marker='o')
    plt.title('Graph')
    plt.show()


# Функция для ведения журнала вычислений
def journal():
    # Задаем переменные для сохранения в журнал
    str1 = e.get()
    str2 = str1 + ' '
    str3 = str2 + math_operator
    str4 = str3 + ' '
    e.delete(0, END)
    # Создаем ведение журнала
    if journal_number == 1:
        label_journal1 = Label(root, text=str4)
        label_journal1.grid(row=1, column=3)
    if journal_number == 2:
        label_journal2 = Label(root, text=str4)
        label_journal2.grid(row=2, column=3)
    if journal_number == 3:
        label_journal3 = Label(root, text=str4)
        label_journal3.grid(row=3, column=3)
    journal_number += 1
    if journal_number == 4:
        journal_number = 1


# Для визульного представления и назначения функций кнопкам
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_math("add"))
button_equal = Button(root, text="=", padx=91, pady=20, command=add)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=clear)

button_subtract = Button(root, text="-", padx=41, pady=20, command=lambda: button_math("subtract"))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: button_math("multiply"))
button_divide = Button(root, text="/", padx=41, pady=20, command=lambda: button_math("divide"))
button_sqrt = Button(root, text="sqrt", padx=31, pady=20, command=square_root)
button_sin = Button(root, text="sin", padx=34, pady=20, command=lambda: trigonometric_functions("sin"))
button_cos = Button(root, text="cos", padx=34, pady=20, command=lambda: trigonometric_functions("cos"))
button_tan = Button(root, text="tan", padx=34, pady=20, command=lambda: trigonometric_functions("tan"))
button_power = Button(root, text="^2", padx=34, pady=20, command=power_function)
button_graph = Button(root, text="Graph", padx=29, pady=20, command=graph)
button_journal = Button(root, text="Save", padx=29, pady=20, command=journal)

# Показатель сохраняемых строк в журнале
journal_number = 1

# Размещение кнопок на экране
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_sqrt.grid(row=7, column=0)
button_sin.grid(row=7, column=1)
button_cos.grid(row=7, column=2)

button_tan.grid(row=8, column=0)
button_power.grid(row=8, column=1)
button_graph.grid(row=8, column=2)
button_journal.grid(row=9, column=0, columnspan=3)

# Запускаем программу
root.mainloop()