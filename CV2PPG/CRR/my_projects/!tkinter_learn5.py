import tkinter as tk
from tkinter import ttk
import win32api

root = tk.Tk()
root.title("Font Selector")

font_names = sorted([f for f in win32api.GetFontFamilyName()])


font_selector = ttk.Combobox(root, values=font_names)
font_selector.pack()

root.mainloop()