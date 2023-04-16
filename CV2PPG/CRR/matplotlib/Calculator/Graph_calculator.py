import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class Calculator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        self.expression = tk.StringVar()
        self.expression.set("0")
        self.result = tk.StringVar()
        self.result.set("0")

        self.create_widgets()

    def create_widgets(self):
        self.expression_entry = ttk.Entry(self.master, textvariable=self.expression, font=("Arial", 20), width=25)
        self.expression_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.result_label = ttk.Label(self.master, textvariable=self.result, font=("Arial", 20), anchor="e")
        self.result_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        self.create_number_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_number_buttons(self):
        buttons = [
            {"text": "1", "row": 2, "column": 0},
            {"text": "2", "row": 2, "column": 1},
            {"text": "3", "row": 2, "column": 2},
            {"text": "4", "row": 3, "column": 0},
            {"text": "5", "row": 3, "column": 1},
            {"text": "6", "row": 3, "column": 2},
            {"text": "7", "row": 4, "column": 0},
            {"text": "8", "row": 4, "column": 1},
            {"text": "9", "row": 4, "column": 2},
            {"text": "0", "row": 5, "column": 1},
            {"text": ".", "row": 5, "column": 2},
        ]
        for button in buttons:
            ttk.Button(
                self.master,
                text=button["text"],
                command=lambda text=button["text"]: self.on_button_click(text)
            ).grid(row=button["row"], column=button["column"], padx=5, pady=5)

    def create_operator_buttons(self):
        buttons = [
            {"text": "+", "row": 2, "column": 3},
            {"text": "-", "row": 3, "column": 3},
            {"text": "*", "row": 4, "column": 3},
            {"text": "/", "row": 5, "column": 3},
            {"text": "(", "row": 5, "column": 0},
            {"text": ")", "row": 5, "column": 2},
        ]
        for button in buttons:
            ttk.Button(
                self.master,
                text=button["text"],
                command=lambda text=button["text"]: self.on_button_click(text)
            ).grid(row=button["row"], column=button["column"], padx=5, pady=5)

    def create_special_buttons(self):
        buttons = [
            {"text": "Clear", "row": 6, "column": 0},
            {"text": "AC", "row": 6, "column": 1},
            {"text": "=", "row": 6, "column": 2},
            {"text": "sin", "row": 2, "column": 4},
            {"text": "cos", "row": 3, "column": 4},
            {"text": "tan", "row": 4, "column": 4},
        ]
        for button in buttons:
            ttk.Button(
                self.master,
                text=button["text"],
                command=lambda text=button["text"]: self.on_button_click(text)
            ).grid(row=button["row"], column=button["column"], padx=5, pady=5)

    def on_button_click(self, text):
        if text == "Clear":
            self.expression.set("0")
            self.result.set("0")
        elif text == "AC":
            self.expression.set(self.expression.get()[:-1])
            self.result.set("0")
        elif text == "=":
            try:
                expr = self.expression.get()
                x = np.linspace(-10, 10, 1000)
                y = eval(expr)

                if np.size(y) == 1:
                    y = np.full_like(x, y)

                plt.clf()
                plt.plot(x, y)
                plt.title("Graph of " + expr)
                plt.xlabel("x")
                plt.ylabel("y")
                plt.show()
            except:
                messagebox.showerror("Error", "Invalid expression")

        elif text in ["sin", "cos", "tan"]:
            self.expression.set(self.expression.get() + text + "(")
        else:
            if self.expression.get() == "0":
                self.expression.set("")
            self.expression.set(self.expression.get() + text)
root = tk.Tk()
app = Calculator(root)
app.mainloop()
