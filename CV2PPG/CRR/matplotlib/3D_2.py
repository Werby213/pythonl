from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


# function for julia set calculation
def julia_set(z, c, max_iter):
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iter


# set constants
width = 1000
height = 1000
max_iter = 100
c = complex(-0.8, 0.156)

# initialize array of zeros
julia = np.zeros((height, width))

# iterate over each pixel
for x in range(width):
    for y in range(height):
        # scale x and y coordinates to be between -1 and 1
        zx = (x - width / 2) * 2 / width
        zy = (y - height / 2) * 2 / height
        # calculate julia set for each pixel
        julia[y, x] = julia_set(complex(zx, zy), c, max_iter)

# plot julia set in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y = np.meshgrid(np.arange(width), np.arange(height))
ax.plot_surface(x, y, julia)
plt.show()
