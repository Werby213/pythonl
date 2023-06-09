import numpy as np
import matplotlib.pyplot as plt


def plot4d(data):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(projection="3d")
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    mask = data > 0.01
    idx = np.arange(int(np.prod(data.shape)))
    x, y, z = np.unravel_index(idx, data.shape)
    ax.scatter(x, y, z, c=data.flatten(), s=10.0 * mask, edgecolor="face", alpha=0.2, marker="o", cmap="magma", linewidth=0)
    plt.tight_layout()
    plt.savefig("test_scatter_4d.png", dpi=250)
    plt.close(fig)



X = np.arange(-10, 10, 0.5)
Y = np.arange(-10, 10, 0.5)
Z = np.arange(-10, 10, 0.5)
X, Y, Z = np.meshgrid(X, Y, Z, indexing="ij")
density_matrix = np.sin(np.sqrt(X**2 + Y**2 + Z**2))
plot4d(density_matrix)