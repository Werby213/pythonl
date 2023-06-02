import tkinter
from math import *

class Calculator():

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("150x500")
        self.main_window.title("Calculator")

       # create and place widgets
        self.result_text = tkinter.StringVar()
        self.result = tkinter.Label(self.main_window, textvariable=self.result_text, width=20)
        self.result.grid(row=0, column=0, columnspan=4)

        self.btn_1 = tkinter.Button(self.main_window, text="1", command=lambda: self.update_result("1"))
        self.btn_1.grid(row=1, column=0)

        self.btn_2 = tkinter.Button(self.main_window, text="2", command=lambda: self.update_result("2"))
        self.btn_2.grid(row=1, column=1)

        self.btn_3 = tkinter.Button(self.main_window, text="3", command=lambda: self.update_result("3"))
        self.btn_3.grid(row=1, column=2)

        self.btn_4 = tkinter.Button(self.main_window, text="4", command=lambda: self.update_result("4"))
        self.btn_4.grid(row=2, column=0)

        self.btn_5 = tkinter.Button(self.main_window, text="5", command=lambda: self.update_result("5"))
        self.btn_5.grid(row=2, column=1)

        self.btn_6 = tkinter.Button(self.main_window, text="6", command=lambda: self.update_result("6"))
        self.btn_6.grid(row=2, column=2)

        self.btn_7 = tkinter.Button(self.main_window, text="7", command=lambda: self.update_result("7"))
        self.btn_7.grid(row=3, column=0)

        self.btn_8 = tkinter.Button(self.main_window, text="8", command=lambda: self.update_result("8"))
        self.btn_8.grid(row=3, column=1)

        self.btn_9 = tkinter.Button(self.main_window, text="9", command=lambda: self.update_result("9"))
        self.btn_9.grid(row=3, column=2)

        self.btn_0 = tkinter.Button(self.main_window, text="0", command=lambda: self.update_result("0"))
        self.btn_0.grid(row=4, column=1)

        self.btn_plus = tkinter.Button(self.main_window, text="+", command=lambda: self.update_result("+"))
        self.btn_plus.grid(row=1, column=3)

        self.btn_minus = tkinter.Button(self.main_window, text="-", command=lambda: self.update_result("-"))
        self.btn_minus.grid(row=2, column=3)

        self.btn_multiply = tkinter.Button(self.main_window, text="*", command=lambda: self.update_result("*"))
        self.btn_multiply.grid(row=3, column=3)

        self.btn_divide = tkinter.Button(self.main_window, text="/", command=lambda: self.update_result("/"))
        self.btn_divide.grid(row=4, column=3)

        self.btn_equal = tkinter.Button(self.main_window, text="=", command=self.calculate_result)
        self.btn_equal.grid(row=4, column=2)

        self.btn_ac = tkinter.Button(self.main_window, text="AC", command=self.clear)
        self.btn_ac.grid(row=4, column=0)

        self.btn_square = tkinter.Button(self.main_window, text="x^2", command=lambda: self.update_result("**2"))
        self.btn_square.grid(row=5, column=0)

        self.btn_sqrt = tkinter.Button(self.main_window, text="sqrt", command=lambda: self.update_result("sqrt"))
        self.btn_sqrt.grid(row=5, column=1)

        self.btn_sin = tkinter.Button(self.main_window, text="sin", command=lambda: self.update_result("sin"))
        self.btn_sin.grid(row=5, column=2)

        self.btn_cos = tkinter.Button(self.main_window, text="cos", command=lambda: self.update_result("cos"))
        self.btn_cos.grid(row=5, column=3)

        self.btn_log = tkinter.Button(self.main_window, text="log", command=lambda: self.update_result("log"))
        self.btn_log.grid(row=6, column=0)

        self.btn_ln = tkinter.Button(self.main_window, text="ln", command=lambda: self.update_result("ln"))
        self.btn_ln.grid(row=6, column=1)

        self.btn_exp = tkinter.Button(self.main_window, text="exp", command=lambda: self.update_result("exp"))
        self.btn_exp.grid(row=6, column=2)

        self.btn_tan = tkinter.Button(self.main_window, text="tan", command=lambda: self.update_result("tan"))
        self.btn_tan.grid(row=6, column=3)

        self.btn_dec = tkinter.Button(self.main_window, text=".", command=lambda: self.update_result("."))
        self.btn_dec.grid(row=4, column=3)

        # logbook
        self.logbook_frame = tkinter.Frame(self.main_window)
        self.logbook_frame.grid(row=7, column=0, columnspan=4)
        self.logbook_text = tkinter.StringVar()
        self.logbook_label = tkinter.Label(self.logbook_frame, textvariable=self.logbook_text)
        self.logbook_label.grid(row=0, column=0)
        self.logbook = []
        self.logbook_row = 0
        self.logbook_rows = 3

        # Increase logbook rows
        self.btn_logbook_rows_up = tkinter.Button(self.main_window, text="+", command=self.increase_logbook_rows)
        self.btn_logbook_rows_up.grid(row=8, column=3)

        # Decrease logbook rows
        self.btn_logbook_rows_down = tkinter.Button(self.main_window, text="-", command=self.decrease_logbook_rows)
        self.btn_logbook_rows_down.grid(row=8, column=2)

        self.expression = ""

    def calculate_result(self):
        self.expression = self.result_text.get()
        try:
            self.result_text.set(eval(self.expression))
            self.add_logbook_row(self.expression + "=" + self.result_text.get())
        except:
            self.result_text.set("ERROR")

    def update_result(self, value):
        self.expression = self.result_text.get()
        self.expression += value
        self.result_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.result_text.set("")

    def add_logbook_row(self, value):
        self.logbook.append(value)
        if len(self.logbook) > self.logbook_rows:
            del self.logbook[0]
        self.update_logbook()

    def update_logbook(self):
        self.logbook_text.set("\n".join(self.logbook))

    def increase_logbook_rows(self):
        self.logbook_rows += 1
        self.update_logbook()

    def decrease_logbook_rows(self):
        if self.logbook_rows > 3:
            self.logbook_rows -= 1
            self.update_logbook()

calculator = Calculator()
calculator.main_window.mainloop()