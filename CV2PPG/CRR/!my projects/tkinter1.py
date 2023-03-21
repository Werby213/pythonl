from tkinter import *
from tkinter import ttk
import numexpr
def calc(NumA, NumB, operator, switch):
  if switch == True:
    print(numexpr.evaluate(NumA + operator + NumB))
  else:
    print("nothing")
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Egor's calculator v1").grid(column=0, row=0)
ttk.Button(frm, text=, command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()


with dpg.window(label="", height=200, width=350):
  #name = dpg.add_input_text(label="Name")
  #создание кнопки, полей float, текстого поля для ввода символа оператора
  NumA = dpg.add_input_float(label="Number A", callback=calc, user_data="NumA")
  NumB = dpg.add_input_float(label="Number B", callback=calc, user_data="NumB")
  operator = dpg.add_input_text(label="math operator", callback=calc, user_data="operator")
  #при нажатаии кнопки Calculate п
  switch = dpg.add_button(label="Calculate", callback=calc, user_data="calculate")
calc(NumA, NumB, operator, switch)
#при запуске ничего не выдает в консоль, только Null
#такое ощущение что данные просто не записываются в переменные

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


