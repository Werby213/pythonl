from tkinter import *
from math import *

class Calculator():

    def __init__(self, master):
        self.master = master
        master.title('Advanced Calculator')
        master.geometry('400x500')

        #Create the display
        self.display = Label(master, text="", font=("Helvetica", 20), bg="white", anchor=E)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        #Create the buttons
        self.button1 = Button(master, text="1", font=("Helvetica", 20), command=lambda: self.add_char('1'), height=2, width=5, bg="white", relief=GROOVE)
        self.button1.grid(row=1, column=0, padx=10, pady=10)
        self.button2 = Button(master, text="2", font=("Helvetica", 20), command=lambda: self.add_char('2'), height=2, width=5, bg="white", relief=GROOVE)
        self.button2.grid(row=1, column=1, padx=10, pady=10)
        self.button3 = Button(master, text="3", font=("Helvetica", 20), command=lambda: self.add_char('3'), height=2, width=5, bg="white", relief=GROOVE)
        self.button3.grid(row=1, column=2, padx=10, pady=10)
        self.button4 = Button(master, text="4", font=("Helvetica", 20), command=lambda: self.add_char('4'), height=2, width=5, bg="white", relief=GROOVE)
        self.button4.grid(row=2, column=0, padx=10, pady=10)
        self.button5 = Button(master, text="5", font=("Helvetica", 20), command=lambda: self.add_char('5'), height=2, width=5, bg="white", relief=GROOVE)
        self.button5.grid(row=2, column=1, padx=10, pady=10)
        self.button6 = Button(master, text="6", font=("Helvetica", 20), command=lambda: self.add_char('6'), height=2, width=5, bg="white", relief=GROOVE)
        self.button6.grid(row=2, column=2, padx=10, pady=10)
        self.button7 = Button(master, text="7", font=("Helvetica", 20), command=lambda: self.add_char('7'), height=2, width=5, bg="white", relief=GROOVE)
        self.button7.grid(row=3, column=0, padx=10, pady=10)
        self.button8 = Button(master, text="8", font=("Helvetica", 20), command=lambda: self.add_char('8'), height=2, width=5, bg="white", relief=GROOVE)
        self.button8.grid(row=3, column=1, padx=10, pady=10)
        self.button9 = Button(master, text="9", font=("Helvetica", 20), command=lambda: self.add_char('9'), height=2, width=5, bg="white", relief=GROOVE)
        self.button9.grid(row=3, column=2, padx=10, pady=10)
        self.button0 = Button(master, text="0", font=("Helvetica", 20), command=lambda: self.add_char('0'), height=2, width=5, bg="white", relief=GROOVE)
        self.button0.grid(row=4, column=1, padx=10, pady=10)
        self.button_dot = Button(master, text=".", font=("Helvetica", 20), command=lambda: self.add_char('.'), height=2, width=5, bg="white", relief=GROOVE)
        self.button_dot.grid(row=4, column=0, padx=10, pady=10)
        self.button_plus = Button(master, text="+", font=("Helvetica", 20), command=lambda: self.add_char('+'), height=2, width=5, bg="white", relief=GROOVE)
        self.button_plus.grid(row=1, column=3, padx=10, pady=10)
        self.button_minus = Button(master, text="-", font=("Helvetica", 20), command=lambda: self.add_char('-'), height=2, width=5, bg="white", relief=GROOVE)
        self.button_minus.grid(row=2, column=3, padx=10, pady=10)
        self.button_multiply = Button(master, text="x", font=("Helvetica", 20), command=lambda: self.add_char('*'), height=2, width=5, bg="white", relief=GROOVE)
        self.button_multiply.grid(row=3, column=3, padx=10, pady=10)
        self.button_divide = Button(master, text="/", font=("Helvetica", 20), command=lambda: self.add_char('/'), height=2, width=5, bg="white", relief=GROOVE)
        self.button_divide.grid(row=4, column=3, padx=10, pady=10)
        self.button_equal = Button(master, text="=", font=("Helvetica", 20), command=self.calculate, height=2, width=5, bg="white", relief=GROOVE)
        self.button_equal.grid(row=4, column=2, padx=10, pady=10)
        self.button_sqrt = Button(master, text="sqrt", font=("Helvetica", 20), command=self.sqrt, height=2, width=5, bg="white", relief=GROOVE)
        self.button_sqrt.grid(row=5, column=0, padx=10, pady=10)
        self.button_power = Button(master, text="^", font=("Helvetica", 20), command=lambda: self.add_char('**'), height=2, width=5, bg="white", relief=GROOVE)
        self.button_power.grid(row=5, column=1, padx=10, pady=10)
        self.button_sin = Button(master, text="sin", font=("Helvetica", 20), command=self.sin, height=2, width=5, bg="white", relief=GROOVE)
        self.button_sin.grid(row=5, column=2, padx=10, pady=10)
        self.button_cos = Button(master, text="cos", font=("Helvetica", 20), command=self.cos, height=2, width=5, bg="white", relief=GROOVE)
        self.button_cos.grid(row=5, column=3, padx=10, pady=10)
        self.button_clear = Button(master, text="clear", font=("Helvetica", 20), command=self.clear, height=2, width=5, bg="white", relief=GROOVE)
        self.button_clear.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

    def add_char(self, char):
        self.display.config(text=self.display.cget("text") + char)

    def calculate(self):
        try:
            self.display.config(text=eval(self.display.cget("text")))
        except:
            self.display.config(text="error")

    def sqrt(self):
        try:
            self.display.config(text=sqrt(float(self.display.cget("text"))))
        except:
            self.display.config(text="error")

    def sin(self):
        try:
            self.display.config(text=sin(radians(float(self.display.cget("text")))))
        except:
            self.display.config(text="error")

    def cos(self):
        try:
            self.display.config(text=cos(radians(float(self.display.cget("text")))))
        except:
            self.display.config(text="error")

    def clear(self):
        self.display.config(text="")

root = Tk()
my_gui = Calculator(root)
root.mainloop()