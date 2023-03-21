import pygame
import pyopencl as cl
import numpy as np

# OpenCL context and queue
ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

pygame.init()
screen_size = 800, 600
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

# Particle data
particle_count = 1000
particles = np.zeros((particle_count, 4), dtype=np.float32)
particles[:, :2] = np.random.rand(particle_count, 2) * screen_size
particles[:, 2:] = np.zeros((particle_count, 2), dtype=np.float32)

# Transfer particle data to GPU
particles_buf = cl.Buffer(ctx, cl.mem_flags.READ_WRITE, size=particles.nbytes)
cl.enqueue_copy(queue, particles_buf, particles)

# OpenCL kernel to update particle positions
kernel = """
__kernel void update_particles(__global float4 *particles, int screen_w, int screen_h)
{
    int gid = get_global_id(0);
    float4 p = particles[gid];
    p.x += p.z;
    p.y += p.w;
    p.w += 0.01f;  // Apply gravity
    if (p.x > screen_w) {  // Collide with right boundary
        p.x = screen_w;
        p.z = -p.z;
    }
    if (p.x < 0) {  // Collide with left boundary
        p.x = 0;
        p.z = -p.z;
    }
    if (p.y > screen_h) {  // Collide with bottom boundary
        p.y = screen_h;
        p.w = -p.w;
    }
    if (p.y < 0) {  // Collide with top boundary
        p.y = 0;
        p.w = -p.w;
    }
    particles[gid] = p;
}
"""

# Compile the kernel
prg = cl.Program(ctx, kernel).build()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rest of the code

    # Clear screen
    screen.fill((255, 255, 255))

    # Update particle positions on GPU
    global_size = (particle_count,)
    local_size = None
    prg.update_particles(queue, global_size, local_size, particles_buf, np.int32(screen_size[0]),
                         np.int32(screen_size[1]))

    # Transfer updated particle data to CPU
    cl.enqueue_copy(queue, particles, particles_buf)

    # Draw particles
    for particle in particles:
        x, y = particle[:2].astype(int)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 5)

        pygame.display.flip()
        clock.tick(0)

    pygame.quit()