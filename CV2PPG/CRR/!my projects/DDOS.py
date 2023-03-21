import pygame
import numpy as np
import pyopencl as cl
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
class Particle:
    def __init__(self, x, y, mass, velocity):
        self.x = x
        self.y = y
        self.mass = mass
        self.velocity = velocity
        self.radius = int(mass * 10)
ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)
kernel = """
__kernel void update_particles(__global float2 *pos, __global float2 *vel, __global float2 *forces, float dt, int num_particles) {
    int gid = get_global_id(0);
    if (gid >= num_particles) return;

    float2 force = (float2)(0.0f, 0.0f);
    for (int i = 0; i < num_particles; i++) {
        if (i == gid) continue;
        float2 delta = pos[i] - pos[gid];
        float distance = length(delta);
        float2 direction = delta / distance;
        force += direction / distance * forces[i] * forces[gid];
    }
    vel[gid] += force * dt;
    pos[gid] += vel[gid] * dt;
}
"""
particles = []
forces = np.zeros(100, dtype=np.float32)
positions = np.zeros((100, 2), dtype=np.float32)
velocities = np.zeros((100, 2), dtype=np.float32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            particles.append(Particle(pos[0], pos[1], 1.0, (0, 0)))

    pos_buf = cl.Buffer(ctx, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, hostbuf=positions)
    vel_buf = cl.Buffer(ctx, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, hostbuf=velocities)
    forces_buf = cl.Buffer(ctx, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, hostbuf=forces)
    prg = cl.Program(ctx, kernel).build()
    global_size = (len(particles),)
    local_size = None
    prg.update_particles(queue, global_size, local_size, pos_buf, vel_buf, forces_buf, np.float32(0.1), np.int32(len(particles)))
    cl.enqueue_copy(queue, positions, pos_buf)
    cl.enqueue_copy(queue, velocities, vel_buf)

    screen.fill((255, 255, 255))
    for particle in particles:
        pygame.draw.circle(screen, (0, 0, 0), (int(particle.x), int(particle.y)), particle.radius)
    pygame.display.update()
    clock.tick(1000)
