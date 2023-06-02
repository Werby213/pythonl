import numpy as np
import pygame as pg
import pyopencl as cl

pg.init()
width, height = 512, 512
screen = pg.display.set_mode((width, height))
pg.display.set_caption("The Game of Life")

state = np.random.randint(2, size=(height, width)).astype(np.int32)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)
state_buf = cl.Buffer(ctx, cl.mem_flags.READ_WRITE, state.nbytes)
next_state_buf = cl.Buffer(ctx, cl.mem_flags.READ_WRITE, state.nbytes)

kernel = """
    __kernel void update_state(__global int* state, __global int* next_state, int width, int height) {
        int gid = get_global_id(0);
        int x = gid % width;
        int y = gid / width;

        int live_neighbors = 0;
        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                if (i == 0 && j == 0) continue;
                int nx = (x + i + width) % width;
                int ny = (y + j + height) % height;
                live_neighbors += state[ny * width + nx];
            }
        }

        int cell = state[y * width + x];
        next_state[y * width + x] = (live_neighbors == 3 || (live_neighbors == 2 && cell)) ? 1 : 0;
    }
"""

program = cl.Program(ctx, kernel).build()

slider_color = pg.Color("gray")
slider_knob_color = pg.Color("white")
slider_rect = pg.Rect(width - 30, height - 30, 20, 200)
slider_value = 0.5

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEMOTION:
            if event.buttons[0] and slider_rect.collidepoint(event.pos):
                slider_value = (event.pos[0] - slider_rect.x) / slider_rect.w

    screen.fill((0, 0, 0))
    for x in range(width):
        for y in range(height):
            color = (255, 255, 255) if state[y, x] else (0, 0, 0)
            pg.draw.rect(screen, color, (x, y, 1, 1))
    pg.draw.rect(screen, slider_color, slider_rect)
    pg.draw.rect(screen, slider_knob_color, pg.Rect(slider_rect.x, slider_rect.y + (1 - slider_value) * slider_rect.h, slider_rect.w, slider_rect.h * slider_value))
    pg.display.flip()

    cl.enqueue_copy(queue, state_buf, state)
    program.update_state(queue, state.shape, None, state_buf, next_state_buf, np.int32(width), np.int32(height))
    cl.enqueue_copy(queue, state, next_state_buf)

    pg.time.wait(int(1000 * (1 - slider_value)))

pg.quit()

