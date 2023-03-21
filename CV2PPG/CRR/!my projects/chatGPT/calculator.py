import tkinter as tk
import numexpr

def calc():
    try:
        num1 = float(input_field.get())
        num2 = float(input_field2.get())
        operator = operator_var.get()
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        elif operator == "**":
            result = num1 ** num2
        else:
            result = "Invalid operator"
        output_label.config(text=result)
    except ValueError:
        output_label.config(text="Invalid value")

root = tk.Tk()
root.title("My GUI")

input_field = tk.Entry(root)
input_field.grid(row=0, column=0)
input_field2 = tk.Entry(root)
input_field2.grid(row=1, column=0)

output_label = tk.Label(root, text="")
output_label.grid(row=3, column=0)

operator_var = tk.StringVar(root)
operator_var.set("+")

operator_plus = tk.Radiobutton(root, text="+", variable=operator_var, value="+")
operator_plus.grid(row=2, column=0)
operator_minus = tk.Radiobutton(root, text="-", variable=operator_var, value="-")
operator_minus.grid(row=2, column=1)
root.mainloop()