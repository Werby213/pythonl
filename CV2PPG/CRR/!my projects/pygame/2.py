import pyautogui
import time
from tkinter import *

def press_button():
    button = button_var.get()
    interval = interval_var.get()
    while True:
        pyautogui.press(button)
        time.sleep(interval)

root = Tk()
root.title("Keyboard Button Presser")

button_var = StringVar(value=' ')
interval_var = DoubleVar(value=1.0)

button_label = Label(root, text="Button:")
button_label.grid(row=0, column=0)
button_entry = Entry(root, textvariable=button_var)
button_entry.grid(row=0, column=1)

interval_label = Label(root, text="Interval (seconds):")
interval_label.grid(row=1, column=0)
interval_entry = Entry(root, textvariable=interval_var)
interval_entry.grid(row=1, column=1)

press_button = Button(root, text="Press Button", command=press_button)
press_button.grid(row=2, column=0, columnspan=2)

root.mainloop()