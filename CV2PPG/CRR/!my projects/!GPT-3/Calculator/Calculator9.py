import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.operations = ['C', 'CE', '/', '*', '-', '+', '=', '.', '+/-']

        self.buttons = [['7', '8', '9'],
                        ['4', '5', '6'],
                        ['1', '2', '3'],
                        ['0', '00', self.operations[7]]]

        self.display = tk.Entry(self.master, width=30, justify='right', font=('Arial', 20))
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        for row in range(4):
            for col in range(3):
                button = tk.Button(self.master, text=self.buttons[row][col], width=7, height=2,
                                   font=('Arial', 12), command=lambda row=row, col=col: self.click_button(row, col))
                button.grid(row=row+1, column=col, padx=5, pady=5)

        for i in range(len(self.operations)):
            button = tk.Button(self.master, text=self.operations[i], width=7, height=2,
                               font=('Arial', 12), command=lambda i=i: self.click_operation(self.operations[i]))
            button.grid(row=i % 4 + 1, column=3, padx=5, pady=5)

        self.reset()

    def reset(self):
        self.operator = ''
        self.first_num = ''
        self.second_num = ''
        self.result = 0
        self.display.delete(0, 'end')

    def click_button(self, row, col):
        if self.display.get() == '0':
            self.display.delete(0, 'end')

        self.display.insert('end', self.buttons[row][col])

    def click_operation(self, op):
        if op == 'C':
            self.reset()

        elif op == 'CE':
            self.display.delete(len(self.display.get()) - 1, 'end')

        elif op == '+/-':
            if self.display.get()[0] == '-':
                self.display.delete(0)
            else:
                self.display.insert(0, '-')

        elif op == '=':
            self.second_num = self.display.get()
            self.calculate()

        else:
            self.first_num = self.display.get()
            self.operator = op
            self.display.delete(0, 'end')

    def calculate(self):
        if self.operator == '/':
            self.result = float(self.first_num) / float(self.second_num)
        elif self.operator == '*':
            self.result = float(self.first_num) * float(self.second_num)
        elif self.operator == '-':
            self.result = float(self.first_num) - float(self.second_num)
        elif self.operator == '+':
            self.result = float(self.first_num) + float(self.second_num)

        self.display.delete(0, 'end')
        self.display.insert(0, self.result)

root = tk.Tk()
app = Calculator(root)
root.mainloop()
