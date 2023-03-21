from tkinter import *
root = Tk()
root.geometry("300x300+100+100")
root.title("Log/Reg by Egor M")
users= {
    "Egor":"test",
    "lalka228":"debil",
    "baclan3000":"kavo"
}
attempts = 5
i = 1
def window_back():
    root.deiconify()

def new_window():
    new_window1 = Toplevel(root)
    new_window1.title("Python Subprocces")
    new_window1.geometry("200x200+400+100")
    welcome = Label(new_window1, text="Welcome!")
    welcome.pack()
    btn_back = Button(new_window1, text="Back", command=window_back)
    btn_back.pack()
    root.mainloop()
def bruteforce():
    bruteforce = Toplevel(root)
    bruteforce.title("Python Subprocces")
    bruteforce.geometry("200x200+400+100")
    label = Label(bruteforce, text="bruteforce")
    label.pack()
    btn_back = Button(bruteforce, text="Back", command=window_back)
    btn_back.pack()
    root.mainloop()
def clear_entry_Login(event):
    if entry_Login.get() == "Логин":
        entry_Login.delete(0, 'end')
def clear_entry_Password(event):
    if entry_password.get() == "Пароль":
        entry_password.delete(0, 'end')
        entry_password.config(show="*")
def enter():
    global password, login, guess, i
    if users.get(entry_Login.get()) == entry_password.get():
        label_out.config(text="user found")
        label_out.update()
        root.withdraw()
        new_window()
    else:
        label_out.config(text="user NOT found")
        label_out.update()
        i = i + 1
        if i > attempts:
            print("Неправильный пароль")
            label_out.config(text="вы ввели 5 раз неправильный пароль!")
def register():
    users [entry_Login.get()]=entry_password.get()
    entry_Login.delete(0, 'end')
    entry_password.delete(0, 'end')
    entry_password.config(show="*")

Label_Login = Label(root, text="Login")
Label_Login.pack()
entry_Login = Entry(root, width=40)
entry_Login.pack()
entry_Login.insert(0, "Логин")
entry_Login.bind("<FocusIn>", clear_entry_Login)
entry_password = Entry(root, width=40)
entry_password.pack()
entry_password.insert(0, "Пароль")
entry_password.bind("<FocusIn>", clear_entry_Password)
btn_Enter = Button(root, text="Enter", command=enter)
btn_Enter.pack()
btn_register = Button(root, text="Registration", command=register)
btn_register.pack()
label_out = Label(root, text="Enter please")
label_out.pack()

root.mainloop()