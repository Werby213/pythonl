from tkinter import *
import math
import subprocess
root = Tk()
root.geometry("320x150")

# Все переменные
equa = ""
expression = ""
total = ""

course_dollar = 70.65
course_euro = 76,47

# Все кнопки
equation = StringVar()
expression = Entry(root, textvariable=equation)
expression.grid(columnspan=4, ipadx=70)


def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

# Функция для вычисления тригонометрических функций
def trigonometry(trig, expression):
    total = eval(trig + '(' + expression + ')')
    equation.set(total)
    expression = ""
# Функция для вычисления курса валют
def converter(convert, expression):
    total = eval(expression + '/' + str(course_dollar))
    equation.set(total)
    expression = ""
# Кнопка тангенс
rub_to_dollar = Button(root, text='₽->$', fg='black', bg='red',
				command=lambda: converter('60', expression.get()), height=1, width=7)
rub_to_dollar.grid(row=2, column='0')

to_euro = Button(root, text='₽->€', fg='black', bg='red',
				command=lambda: converter('60', expression.get()), height=1, width=7)
to_euro.grid(row=2, column='1')
# Кнопка тангенс
tg = Button(root, text='tg', fg='black', bg='red',
				command=lambda: trigonometry('math.tan', expression.get()), height=1, width=7)
tg.grid(row=1, column='0')

# Кнопка косинус
cos = Button(root, text='cos', fg='black', bg='red',
				command=lambda: trigonometry('math.cos', expression.get()), height=1, width=7)
cos.grid(row=1, column='1')

# Кнопка синус
sin = Button(root, text='sin', fg='black', bg='red',
				command=lambda: trigonometry('math.sin', expression.get()), height=1, width=7)
sin.grid(row=1, column='2')

snake = Button(root, text='Я устал, я хочу поиграть в змейку!', fg='black', bg='red',
				command=lambda: subprocess.call(["python", "C:\\Users\\User\\PycharmProjects\\CV2PPG\\CRR\\my_projects\\snake.py"]), height=1, width=27)
snake.place(x=10, y=80)
root.mainloop()