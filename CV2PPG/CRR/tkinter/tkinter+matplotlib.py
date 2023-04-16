import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Создаем окно tkinter
root = tk.Tk()
root.title("Пример совмещения Tkinter и Matplotlib")

# Создаем объект фигуры Matplotlib
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

# Нарисуем график на фигуре
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]
ax.plot(x, y)

# Создаем объект для отображения фигуры на окне tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# Размещаем объект на окне tkinter
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Запускаем цикл обработки событий Tkinter
tk.mainloop()
