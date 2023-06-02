from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
from PIL import ImageTk, Image
img=Image.open("/CRR/my_projects\\Image_Tkinter\\Image1.jpg")
img=img.resize((350,350))
img=ImageTk.PhotoImage(img)
app = Tk()
app.geometry('500x500')
list_images = {"1":"Image (1).jpg",
               "2":"Image (2).jpg",
               "3":"Image (3).jpg"}
def askopen():
    with fd.askopenfilename(filetypes=[("Изображения", "*.jpg"), ("Все файлы", "*.*")]) as input_file:
        image = input_file.read()
btn_open = Button(app, command = askopen, height=1, width=10, text="Open")
btn_refresh = Button(app, command = askopen, height=1, width=10, text="Refresh")
comboImages = ttk.Combobox(app, values=list_images)
lbl_image = Label(app, text="Выберите Изборажение", image=img)
comboImages.place(x=100, y=50)
btn_open.place(x=250, y=48)
btn_refresh.place(x=250, y=68)
mainloop()