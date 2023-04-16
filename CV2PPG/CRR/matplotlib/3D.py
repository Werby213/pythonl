import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создаем объект фигуры и оси
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Генерируем данные для графика
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Строим поверхность
surf = ax.plot_surface(X, Y, Z, cmap='viridis', rasterized=True, antialiased=False)
ax.set_rasterization_zorder(0)

# Отображаем график
plt.show()
