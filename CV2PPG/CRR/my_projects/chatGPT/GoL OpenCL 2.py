import pyopencl as cl
import pygame
import numpy as np

width, height = 800, 800
size = 2

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

pygame.init()
screen = pygame.display.set_mode((width, height))

state = np.random.randint(2, size=(height // size, width // size), dtype=np.int32)
state_buf = cl.Buffer(ctx, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, hostbuf=state)

kernel = """
    __kernel void life(__global int* state, int width, int height) {
        int x = get_global_id(0);
        int y = get_global_id(1);
        int sum = 0;
        for(int i = -1; i <= 1; i++) {
            for(int j = -1; j <= 1; j++) {
                if(x + i < 0 || x + i >= height || y + j < 0 || y + j >= width) {
                    continue;
                }
                if(i == 0 && j == 0) {
                    continue;
                }
                sum += state[(x + i) * width + (y + j)];
            }
        }
        if(state[x * width + y]) {
            if(sum < 2 || sum > 3) {
                state[x * width + y] = 0;
            }
        } else {
            if(sum == 3) {
                state[x * width + y] = 1;
            }
        }
    }
"""

prg = cl.Program(ctx, kernel).build()
speed = int(input("Enter the simulation speed: "))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                speed = int(input("Enter the simulation speed: "))

    prg.life(queue, state.shape, None, state_buf, np.int32(width // size), np.int32(height // size))
    cl.enqueue_copy(queue, state, state_buf)

    for x in range(height // size):
        for y in range(width // size):
            color = (255, 255, 255) if state[x, y] else (0, 0, 0)
            pygame.draw.rect(screen, color, (y * size, x * size, size, size))

    pygame.display.flip()
    pygame.time.wait(speed)

pygame.quit()
