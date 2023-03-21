import dearpygui.dearpygui as dpg
import numexpr
a = 0
Result = 0
def calc(NumA, NumB, operator, switch):
    if switch == True:
        print(numexpr.evaluate(str(NumA + operator + NumB)))
    else:
        print("nothing")
dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()
with dpg.window(label="Egor's calculator v1", height=200, width=500):
    #name = dpg.add_input_text(label="Name")
    NumA = dpg.add_input_float(label="Number A")
    NumB= dpg.add_input_float(label="Number B")
    operator = dpg.add_input_text(label="math operator")
    switch = dpg.add_button(label="Calculate")
#    if switch == 1:
#        Result = NumA + NumB
#    calc(NumA, NumB, operator)
    print(calc(NumA, NumB, operator, switch))

#a=globals().get(str(btn1) + str(btn2) )

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
