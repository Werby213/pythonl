from tkinter import *
import tkinter.filedialog as fd
root = Tk()
def replace(openfile, replace_button):
	while replace_button == True:
		if openfile == whatreplace:


frame1 = Frame(root,bg='green', bd=5)
text.place(x=0, y=50)
button_open = Button(root, text='open', fg='black', bg='red',
				command=fd.askopenfilename(), height=1, width=7)
button_save = Button(root, text='save', fg='black', bg='red',
				command=, height=1, width=7)
button_replace = Button(root, text='save', fg='black', bg='red',
				command=replace_button, height=1, width=7)
replace = Entry(root, textvariable=openfile)
frame1.pack()
button_open.pack()
root.mainloop()