import tkinter as tk
import numexpr

def get_input():
    global NumA, NumB, operator
    try:
        NumA = float(input_field.get())
        NumB = float(input_field2.get())
        operator = operator_var.get()
        if (NumA == 0 or NumB == 0 or NumA is None or NumB is None) or operator not in ["+", "-", "*", "/", "**"]:
            output_label.config(text="Invalid value")
        else:
            output_label.config(text=numexpr.evaluate(str(NumA) + operator + str(NumB)))
    except ValueError:
        output_label.config(text="Please enter a number")

def set_plus():
    global operator
    operator = "+"

def set_minus():
    global operator
    operator = "-"

def set_multiply():
    global operator
    operator = "*"

def set_divide():
    global operator
    operator = "/"

# Define similar functions for the other operators
root = tk.Tk()
root.title("My GUI")
operator_var = tk.StringVar()
operator_plus = tk.Radiobutton(root, text="+", variable=operator_var)
input_field = tk.Entry(root)
input_field.pack()
input_field2 = tk.Entry(root)
input_field2.pack()
#input_field3 = tk.Entry(root)
#input_field3.pack()

output_label = tk.Label(root, text="")
output_label.pack()
operator_plus = tk.Button(root, text="+", command=set_plus)
operator_plus.pack()
operator_minus = tk.Button(root, text="-", command=set_minus)
operator_minus.pack()
operator_multiply = tk.Button(root, text="*", command=set_multiply)
operator_multiply.pack()
operator_divide = tk.Button(root, text="/", command=set_minus)
operator_divide.pack()
# Create similar buttons for the other operators
#switch = tk.Button(root, text="Submit", command=calc)
#switch.pack()
set_plus()
set_minus()
get_input()
root.mainloop()
