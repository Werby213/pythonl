
import pygame
import numpy as np
import pycuda.driver as cuda
from pycuda.compiler import SourceModule

# Create a PyGame window
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Conway\'s Game of Life')

# Create a 2D array with initial conditions
grid = np.random.randint(2, size=(600, 800))

# Create a CUDA module
mod = SourceModule("""
    __global__ void conway(int *grid, int *new_grid)
    {
        int x = threadIdx.x + blockIdx.x * blockDim.x;
        int y = threadIdx.y + blockIdx.y * blockDim.y;
        int neighbors = 0;

        //Count neighbors
        for (int i = -1; i <= 1; i++)
        {
            for (int j = -1; j <= 1; j++)
            {
                if (x + i >= 0 && x + i < 800 && y + j >= 0 && y + j < 600)
                {
                    neighbors += grid[(y + j) * 800 + (x + i)];
                }
            }
        }
        neighbors -= grid[y * 800 + x];

        //Rules
        if (grid[y * 800 + x] == 1 && (neighbors == 2 || neighbors == 3))
        {
            new_grid[y * 800 + x] = 1;
        }
        else if (grid[y * 800 + x] == 0 && neighbors == 3)
        {
            new_grid[y * 800 + x] = 1;
        }
        else
        {
            new_grid[y * 800 + x] = 0;
        }
    }
""")

# Get the function from the module
conway = mod.get_function("conway")

# Allocate memory on the device
d_grid = cuda.mem_alloc(grid.nbytes)
d_new_grid = cuda.mem_alloc(grid.nbytes)

# Copy the data from the host to the device
cuda.memcpy_htod(d_grid, grid)

# Specify the block size
block_size = (8, 8)

# Run the kernel
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Copy the data from the host to the device
    cuda.memcpy_htod(d_grid, grid)

    # Run the kernel
    conway(d_grid, d_new_grid, block=block_size)

    # Copy the data from the device to the host
    cuda.memcpy_dtoh(grid, d_new_grid)

    # Draw the grid
    for y in range(600):
        for x in range(800):
            color = (255, 255, 255) if grid[y][x] == 1 else (0, 0, 0)
            pygame.draw.rect(window, color, (x * 1, y * 1, 1, 1))
    pygame.display.update()