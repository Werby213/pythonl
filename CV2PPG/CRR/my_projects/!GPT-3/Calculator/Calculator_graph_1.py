import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from mpl_toolkits.mplot3d import Axes3D
colors_list = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white", "gray", "teal", "maroon", "navy", "magenta", "cyan", "olive", "lime", "aqua", "silver", "gold", "violet", "indigo", "coral", "turquoise", "salmon", "tan", "lavender", "peach", "periwinkle"]
def add_function_entry():
    entry_frame = tk.Frame(frame_functions)
    entry_frame.pack(side=tk.TOP, padx=5, pady=5)

    entry = tk.Entry(entry_frame, width=30)
    entry.pack(side=tk.LEFT)
    entry_functions.append(entry)

    sel_color = random.choice(colors_list)
    color_entry = tk.Entry(entry_frame, width=10)
    color_entry.insert(0, str(sel_color))
    color_entry.pack(side=tk.LEFT)
    color_entries.append(color_entry)

    delete_button = tk.Button(entry_frame, text="X", command=lambda: delete_function_entry(entry, color_entry))
    delete_button.pack(side=tk.LEFT)
    delete_buttons.append(delete_button)

def delete_function_entry(entry, color_entry):
    index = entry_functions.index(entry)
    entry.destroy()
    color_entry.destroy()
    delete_buttons[index].destroy()
    entry_functions.pop(index)
    color_entries.pop(index)
    delete_buttons.pop(index)

def plot_graph():
    functions = [entry.get() for entry in entry_functions]  # Получаем список введенных пользователем функций
    colors = [color_entry.get() for color_entry in color_entries]

    x = np.linspace(-10, 10, 1000)  # Задаем диапазон значений по оси x

    if graph_mode.get() == 2:  # Если выбран режим 2D
        try:
            namespace = {"__builtins__": None, "x": x}
            namespace.update(vars(math))
            for function, color in zip(functions, colors):
                y = eval(function, namespace)
                plt.plot(x, y, color=color)  # Строим график
        except Exception as e:
            print("Ошибка вычисления функции:", e)
            return

        # Вычисляем значения функции для каждого x

        plt.xlabel('x')  # Задаем подпись оси x
        plt.ylabel('y')  # Задаем подпись оси y
        plt.title('График функции')  # Задаем заголовок графика
        plt.grid(True)  # Включаем отображение сетки
        plt.show()  # Отображаем график

    elif graph_mode.get() == 3:  # Если выбран режим 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        try:
            namespace = {"__builtins__": None, "x": x}
            namespace.update(vars(math))
            for function, color in zip(functions, colors):
                y = eval(function, namespace)
                plt.plot(x, y, color=color)  # Строим график
        except Exception as e:
            print("Ошибка вычисления функции:", e)
            return
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title('3D График функции')
        plt.show()


# Создаем графический интерфейс с использованием tkinter
root = tk.Tk()
root.title("Калькулятор с графиками")

frame_functions = tk.Frame(root)
frame_functions.pack(side=tk.TOP, padx=10, pady=10)

entry_functions = []
color_entries = []
delete_buttons = []

add_button = tk.Button(root, text="Добавить функцию", command=add_function_entry)
add_button.pack(padx=10, pady=10)

plot_button = tk.Button(root, text="Построить график", command=plot_graph)
plot_button.pack(padx=10, pady=10)

# Создаем переключатель для выбора режима графика
graph_mode = tk.IntVar()
graph_mode.set(2)  # По умолчанию установлен режим 2D

mode_2d = tk.Radiobutton(root, text="2D", variable=graph_mode, value=2)
mode_2d.pack()

mode_3d = tk.Radiobutton(root, text="3D", variable=graph_mode, value=3)
mode_3d.pack()

root.mainloop()
