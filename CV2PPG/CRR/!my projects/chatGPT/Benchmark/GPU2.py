import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import pygame

width, height = 256, 256
cell_size = 2

# Create a Pygame window
pygame.init()
screen = pygame.display.set_mode((width*cell_size, height*cell_size))
pygame.display.set_caption("Game of Life")

# Create initial state
state = np.random.randint(0, 2, (height, width), np.uint8)

# CUDA kernel
mod = SourceModule("""
    __global__ void game_of_life(unsigned char *state, int width, int height) {
        int x = blockIdx.x*blockDim.x + threadIdx.x;
        int y = blockIdx.y*blockDim.y + threadIdx.y;
        if (x >= width || y >= height) return;

        int n = 0;
        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                if (i == 0 && j == 0) continue;
                int xx = x + i;
                int yy = y + j;
                if (xx < 0) xx = width-1;
                if (xx >= width) xx = 0;
                if (yy < 0) yy = height-1;
                if (yy >= height) yy = 0;
                n += state[yy*width + xx];
            }
        }

        int cur = state[y*width + x];
        if (cur == 1 && (n < 2 || n > 3)) {
            state[y*width + x] = 0;
        } else if (cur == 0 && n == 3) {
            state[y*width + x] = 1;
        }
    }
""")
game_of_life = mod.get_function("game_of_life")

# Main loop
speed = 50
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get new simulation speed
    try:
        speed = int(input("Enter the simulation speed: "))
    except:
        pass

    # Run CUDA kernel
    state_gpu = cuda.mem_alloc(state.nbytes)
    cuda.memcpy_htod(state_gpu, state)
    game_of_life(state_gpu, np.int32(width), np.int32(height), block=(16, 16, 1), grid=(width//16, height//16))
    cuda.memcpy_dtoh(state, state_gpu)

    # Draw cells
    screen.fill((0, 0, 0))
    for y in range(height):
        for x in range(width):
            if state[y, x] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (x*cell_size, y*cell_size, cell_size, cell_size))
    pygame.display.flip()
    pygame.quit()
