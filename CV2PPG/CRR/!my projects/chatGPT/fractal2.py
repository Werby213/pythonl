import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, max_iter, horizon=2.0):
    X = np.linspace(xmin, xmax, xn, dtype=np.float32)
    Y = np.linspace(ymin, ymax, yn, dtype=np.float32)
    C = X + Y[:, None]*1j
    N = np.zeros_like(C, dtype=int)
    Z = np.zeros_like(C)
    for n in range(max_iter):
        I = np.less(abs(Z), horizon)
        N[I] = n
        Z[I] = Z[I]**2 + C[I]
    N[N == max_iter-1] = 0
    return Z, N

if __name__ == '__main__':
    xmin, xmax, ymin, ymax = -2.25, +0.75, -2.25, +2.25
    xn, yn = 3200, 3200
    max_iter = 256
    dpi = 72
    horizon=2.0**40
    Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, max_iter, horizon)
    plt.imshow(N, extent=(xmin, xmax, ymin, ymax), cmap='jet', origin='lower')
    plt.savefig('mandelbrot.png', dpi=dpi)
    plt.show()
