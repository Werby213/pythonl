import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < 100:
        z = z*z + c
        n += 1
    return n

xmin, xmax, ymin, ymax = -2, 1, -1.5, 1.5

X, Y = np.linspace(xmin, xmax, 1000), np.linspace(ymin, ymax, 1000)
Z = np.array([[mandelbrot(complex(x, y)) for x, y in zip(X, Y)]])
plt.imshow(Z, cmap='hot')
plt.show()