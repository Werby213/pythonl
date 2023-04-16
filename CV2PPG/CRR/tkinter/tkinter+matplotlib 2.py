import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt

# Создаем окно tkinter
root = tk.Tk()
root.title("Пример совместной работы Tkinter и Matplotlib")

# Создаем объекты фигуры и осей Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Создаем начальный график
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]
z = [5, 4, 3, 2, 1]
ax.plot(x, y, z)

# Функции для обновления графика
def update_x(value):
    x = [float(i) for i in value.split(",")]
    ax.clear()
    ax.plot(x, y, z)
    fig.canvas.draw()

def update_y(value):
    y = [float(i) for i in value.split(",")]
    ax.clear()
    ax.plot(x, y, z)
    fig.canvas.draw()

def update_z(value):
    z = [float(i) for i in value.split(",")]
    ax.clear()
    ax.plot(x, y, z)
    fig.canvas.draw()

# Создаем элементы управления Tkinter
x_label = tk.Label(root, text="X:")
x_label.pack()
x_entry = tk.Entry(root)
x_entry.pack()
x_button = tk.Button(root, text="Обновить X", command=lambda: update_x(x_entry.get()))
x_button.pack()

y_label = tk.Label(root, text="Y:")
y_label.pack()
y_entry = tk.Entry(root)
y_entry.pack()
y_button = tk.Button(root, text="Обновить Y", command=lambda: update_y(y_entry.get()))
y_button.pack()

z_label = tk.Label(root, text="Z:")
z_label.pack()
z_entry = tk.Entry(root)
z_entry.pack()
z_button = tk.Button(root, text="Обновить Z", command=lambda: update_z(z_entry.get()))
z_button.pack()

# Размещаем объекты на окне Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)

canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Запускаем цикл обработки событий Tkinter
tk.mainloop()
