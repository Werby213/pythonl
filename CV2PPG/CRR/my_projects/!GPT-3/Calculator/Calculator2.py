from tkinter import *

root = Tk()
root.title("Advanced Calculator")
root.geometry("250x250")

# Создаем текстовое поле
text_input = StringVar()
operator = ""

txtDisplay = Entry(root, textvariable = text_input, bd=20, insertwidth=4, font=30, justify="right").grid(columnspan=4)

# Создаем функции
def btnClick (numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""

# Создаем кнопки
btn7 = Button(root, text="7", width=5, height=2, command=lambda:btnClick(7)).grid(row=1, column=0)
btn8 = Button(root, text="8", width=5, height=2, command=lambda:btnClick(8)).grid(row=1, column=1)
btn9 = Button(root, text="9", width=5, height=2, command=lambda:btnClick(9)).grid(row=1, column=2)
btnPlus = Button(root, text="+", width=5, height=2, command=lambda:btnClick("+")).grid(row=1, column=3)

btn4 = Button(root, text="4", width=5, height=2, command=lambda:btnClick(4)).grid(row=2, column=0)
btn5 = Button(root, text="5", width=5, height=2, command=lambda:btnClick(5)).grid(row=2, column=1)
btn6 = Button(root, text="6", width=5, height=2, command=lambda:btnClick(6)).grid(row=2, column=2)
btnMinus = Button(root, text="-", width=5, height=2, command=lambda:btnClick("-")).grid(row=2, column=3)

btn1 = Button(root, text="1", width=5, height=2, command=lambda:btnClick(1)).grid(row=3, column=0)
btn2 = Button(root, text="2", width=5, height=2, command=lambda:btnClick(2)).grid(row=3, column=1)
btn3 = Button(root, text="3", width=5, height=2, command=lambda:btnClick(3)).grid(row=3, column=2)
btnMultiply = Button(root, text="*", width=5, height=2, command=lambda:btnClick("*")).grid(row=3, column=3)

btn0 = Button(root, text="0", width=5, height=2, command=lambda:btnClick(0)).grid(row=4, column=0)
btnClear = Button(root, text="C", width=5, height=2, command=btnClearDisplay).grid(row=4, column=1)
btnEquals = Button(root, text="=", width=5, height=2, command=btnEqualsInput).grid(row=4, column=2)
btnDivide = Button(root, text="/", width=5, height=2, command=lambda:btnClick("/")).grid(row=4, column=3)

root.mainloop()