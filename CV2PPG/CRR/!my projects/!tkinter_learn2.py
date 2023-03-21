from tkinter import *
import math
import subprocess
root = Tk()
root.geometry("320x150")

# Все переменные
equa = ""
expression = ""
total = ""

# Все кнопки
equation = StringVar()
expression = Entry(root, textvariable=equation)
expression.grid(columnspan=4, ipadx=70)
expression = Entry(root, textvariable=equation)
expression.grid(columnspan=8, ipadx=70)


def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

# Функция для вычисления тригонометрических функций
def trigonometry(trig, expression):
    total = eval(trig + '(' + expression + ')')
    equation.set(total)
    expression = ""
# Кнопка тангенс
tg = Button(root, text='tg', fg='black', bg='red',
				command=lambda: trigonometry('math.tan', expression.get()), height=1, width=7)
tg.grid(row=1, column='1')

# Кнопка косинус
cos = Button(root, text='cos', fg='black', bg='red',
				command=lambda: trigonometry('math.cos', expression.get()), height=1, width=7)
cos.grid(row=1, column='2')

# Кнопка синус
sin = Button(root, text='sin', fg='black', bg='red',
				command=lambda: trigonometry('math.sin', expression.get()), height=1, width=7)
sin.grid(row=1, column='3')
# Кнопка плюс
button1 = Button(root, text='+', fg='black', bg='red',
				command=lambda: trigonometry('+', expression.get()), height=1, width=7)
button1.grid(row=2, column='1')
snake = Button(root, text='Я устал, я хочу поиграть в змейку!', fg='black', bg='red',
				command=lambda: subprocess.call(["python", "C:\\Users\\User\\PycharmProjects\\CV2PPG\\CRR\\!my projects\\snake.py"]), height=1, width=27)
snake.grid(row=3, column='2')
root.mainloop()