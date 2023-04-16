import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np

# Создаем объект фигуры и оси
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([0, 1])

# Создаем объект линии на оси
line, = ax.plot([], [])

# Функция для обновления данных на графике
def update_line(num):
    x = np.linspace(0, 10, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * num))
    line.set_data(x, y)
    return line,

# Анимируем график
ani = FuncAnimation(fig, update_line, frames=100, interval=50, blit=True)

# Отображаем график
plt.show()
