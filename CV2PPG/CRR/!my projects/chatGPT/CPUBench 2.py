import numpy as np
import pygame as pg
import pyopencl as cl

# Initialize Pygame
pg.init()

# Create a window for the simulation
width, height = 512, 512
screen = pg.display.set_mode((width, height))
pg.display.set_caption("The Game of Life")

# Create a random initial state for the Game of Life
state = np.random.randint(2, size=(width, height)).astype(np.int32)

# Create an OpenCL context and command queue
ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

# Allocate memory on the device for the current and next state
state_buf = cl.Buffer(ctx, cl.mem_flags.READ_WRITE, state.nbytes)
next_state_buf = cl.Buffer(ctx, cl.mem_flags.READ_WRITE, state.nbytes)

# Copy the initial state to the device
cl.enqueue_copy(queue, state_buf, state)

# Create a kernel to update the state of the Game of Life
kernel = """
    __kernel void update_state(__global int *state, __global int *next_state) {
        int gid = get_global_id(0);
        int x = gid % 512;
        int y = gid / 512;

        int alive_neighbors = 0;
        for (int dx = -1; dx <= 1; dx++) {
            for (int dy = -1; dy <= 1; dy++) {
                if (dx == 0 && dy == 0) continue;
                int x_neighbor = (x + dx + 512) % 512;
                int y_neighbor = (y + dy + 512) % 512;
                alive_neighbors += state[y_neighbor * 512 + x_neighbor];
            }
        }

        int is_alive = state[gid];
        next_state[gid] = (is_alive && (alive_neighbors == 2 || alive_neighbors == 3)) || (!is_alive && alive_neighbors == 3);
    }
"""

# Compile the kernel
program = cl.Program(ctx, kernel).build()

# Create a sliding bar to control the simulation speed
slider_rect = pg.Rect(10, 10, 200, 20)
slider_color = pg.Color("white")
slider_knob_color = pg.Color("black")
slider_value = 0.0

# Run the simulation loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and slider_rect.collidepoint(event.pos):
                slider_value = (event.pos[0] - slider_rect.x) / slider_rect.w
        elif event.type == pg.MOUSEMOTION:
            if event.buttons[0] and slider_rect.collidepoint(event.pos):
                slider_value = (event.pos[0] - slider_rect.x) / slider_rect.w
# Clear the screen
screen.fill((0, 0, 0))

# Draw the current state of the Game of Life
for x in range(width):
    for y in range(height):
        color = (255, 255, 255) if state[y, x] else (0, 0, 0)
        pg.draw.rect(screen, color, (x, y, 1, 1))

# Draw the sliding bar
pg.draw.rect(screen, slider_color, slider_rect)
pg.draw.rect(screen, slider_knob_color, (slider_rect.x + slider_value * slider_rect.w - 5, slider_rect.y - 5, 10, 30))

# Update the state of the Game of Life
global_size = (width * height,)
local_size = None
program.update_state(queue, global_size, local_size, state_buf, next_state_buf)

# Copy the next state back to the host
cl.enqueue_copy(queue, state, next_state_buf)

# Update the display
pg.display.flip()

# Control the speed of the simulation with the sliding bar
delay = int((1.0 - slider_value) * 1000)
pg.time.wait(delay)
pg.quit()