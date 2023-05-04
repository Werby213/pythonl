import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Создаем объект фигуры и оси
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Генерируем данные для графика
x = np.linspace(-5, 5, 101)
y = np.linspace(-5, 5, 101)
X, Y = np.meshgrid(x, y)

# Определяем начальное и конечное значения для функции
start = np.arctan(np.linalg.norm([X, Y], axis=0))
end = np.arctan(np.linalg.norm([X-1, Y-1], axis=0))

# Создаем функцию анимации
def animate(i):
    # Вычисляем значение функции для текущего шага
    t = i / 100
    X = (1 - t) * start + t * end
    Y = (1 - t) * start + t * end
    Z = (1 - t) * start + t * end



    # Обновляем поверхность
    ax.clear()
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', rasterized=True, antialiased=False)
    ax.set_rasterization_zorder(0)

# Создаем объект анимации
anim = FuncAnimation(fig, animate, frames=100, interval=50)

# Отображаем анимацию
plt.show()
