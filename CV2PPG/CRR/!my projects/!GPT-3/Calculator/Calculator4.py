from tkinter import *
import math

# создание окна
root = Tk()
root.title('Calculator')

# все переменные
equa = ""
expression = ""

# функция для ввода числа в поле
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

# функция для вычисления и очистки
def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:
		equation.set(" error ")
		expression = ""

# функция для очистки поля
def clear():
	global expression
	expression = ""
	equation.set("")

# функция для квадратного корня
def sqrt():
	global expression
	total = math.sqrt(eval(expression))
	equation.set(total)
	expression = ""

# функция для вычисления тригонометрических функций
def trigonometry(trig):
	global expression
	total = eval(trig + '(' + expression + ')')
	equation.set(total)
	expression = ""

# функция для возведения в степень
def power():
	global expression
	total = eval(expression + '**2')
	equation.set(total)
	expression = ""

# Все кнопки
equation = StringVar()
expression_field = Entry(root, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)
equation.set('enter your expression')

# Кнопка 1
button1 = Button(root, text=' 1 ', fg='black', bg='red',
				command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

# Кнопка 2
button2 = Button(root, text=' 2 ', fg='black', bg='red',
				command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)

# Кнопка 3
button3 = Button(root, text=' 3 ', fg='black', bg='red',
				command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)

# Кнопка 4
button4 = Button(root, text=' 4 ', fg='black', bg='red',
				command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)

# Кнопка 5
button5 = Button(root, text=' 5 ', fg='black', bg='red',
				command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)

# Кнопка 6
button6 = Button(root, text=' 6 ', fg='black', bg='red',
				command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)

# Кнопка 7
button7 = Button(root, text=' 7 ', fg='black', bg='red',
				command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)

# Кнопка 8
button8 = Button(root, text=' 8 ', fg='black', bg='red',
				command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)

# Кнопка 9
button9 = Button(root, text=' 9 ', fg='black', bg='red',
				command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)

# Кнопка 0
button0 = Button(root, text=' 0 ', fg='black', bg='red',
				command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)

# Кнопка точка
point = Button(root, text=' . ', fg='black', bg='red',
				command=lambda: press('.'), height=1, width=7)
point.grid(row=5, column=1)

# Кнопка плюс
plus = Button(root, text=' + ', fg='black', bg='red',
				command=lambda: press('+'), height=1, width=7)
plus.grid(row=2, column=3)

# Кнопка минус
minus = Button(root, text=' - ', fg='black', bg='red',
				command=lambda: press('-'), height=1, width=7)
minus.grid(row=3, column=3)

# Кнопка умножить
multiply = Button(root, text=' * ', fg='black', bg='red',
				command=lambda: press('*'), height=1, width=7)
multiply.grid(row=4, column=3)

# Кнопка делить
divide = Button(root, text=' / ', fg='black', bg='red',
				command=lambda: press('/'), height=1, width=7)
divide.grid(row=5, column=3)

# Кнопка равно
equal = Button(root, text=' = ', fg='black', bg='red',
				command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)

# Кнопка очистки
clear = Button(root, text='Clear', fg='black', bg='red',
				command=clear, height=1, width=7)
clear.grid(row=5, column='1')

# Кнопка корня
sqrt = Button(root, text='sqrt', fg='black', bg='red',
				command=sqrt, height=1, width=7)
sqrt.grid(row=1, column='0')

# Кнопка тангенс
tg = Button(root, text='tg', fg='black', bg='red',
				command=lambda: trigonometry('math.tan'), height=1, width=7)
tg.grid(row=1, column='1')

# Кнопка косинус
cos = Button(root, text='cos', fg='black', bg='red',
				command=lambda: trigonometry('math.cos'), height=1, width=7)
cos.grid(row=1, column='2')

# Кнопка синус
sin = Button(root, text='sin', fg='black', bg='red',
				command=lambda: trigonometry('math.sin'), height=1, width=7)
sin.grid(row=1, column='3')

# Кнопка возведения в степень
power = Button(root, text='^2', fg='black', bg='red',
				command=power, height=1, width=7)
power.grid(row=2, column='4')

root.mainloop()