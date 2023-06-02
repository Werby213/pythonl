import pygame
import numpy as np
import pycuda.driver as cuda
from pycuda.compiler import SourceModule

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Conway\'s Game of Life')

# Ебаная решетка размером 600 на 800
grid = np.random.randint(2, size=(600, 800))

mod = SourceModule("""
    __global__ void conway(int *grid, int *new_grid)
    {
        int x = threadIdx.x + blockIdx.x * blockDim.x;
        int y = threadIdx.y + blockIdx.y * blockDim.y;
        int neighbors = 0;

        // Идем нахуй вокруг текущей клетки
        for (int i = -1; i <= 1; i++)
        {
            for (int j = -1; j <= 1; j++)
            {
                if (x + i >= 0 && x + i < 800 && y + j >= 0 && y + j < 600)
                {
                    // Соседние пидорасы тоже засчитываются
                    neighbors += grid[(y + j) * 800 + (x + i)];
                }
            }
        }
        neighbors -= grid[y * 800 + x];

        if (grid[y * 800 + x] == 1 && (neighbors == 2 || neighbors == 3))
        {
            // Пидорасы продолжают жить
            new_grid[y * 800 + x] = 1;
        }
        else if (grid[y * 800 + x] == 0 && neighbors == 3)
        {
            // Рождается новый пидорас
            new_grid[y * 800 + x] = 1;
        }
        else
        {
            // Унылая одиночество или перенаселение
            new_grid[y * 800 + x] = 0;
        }
    }
""")

conway = mod.get_function("conway")

d_grid = cuda.mem_alloc(grid.nbytes)
d_new_grid = cuda.mem_alloc(grid.nbytes)

cuda.memcpy_htod(d_grid, grid)

# Размер блока, нахуй!
block_size = (8, 8)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    cuda.memcpy_htod(d_grid, grid)

    # Отправляем пидорасов на обработку
    conway(d_grid, d_new_grid, block=block_size)

    cuda.memcpy_dtoh(grid, d_new_grid)

    for y in range(600):
        for x in range(800):
            color = (255, 255, 255) if grid[y][x] == 1 else (0, 0, 0)
            # Рисуем прямоугольничек. Какой, конечно, выберешь, хули?
            pygame.draw.rect(window, color
