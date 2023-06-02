import pyopencl as cl
import timeit
import numpy as np
from tqdm import tqdm

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)
a = np.ones(256, dtype=np.float64)
b = np.ones(256, dtype=np.float64)
c = np.ones(256, dtype=np.float64)
d = np.ones(256, dtype=np.float64)
iterations = 10000

prg = cl.Program(ctx, """
    __kernel void test(__global float* a,
                       __global float* b,
                       __global float* c,
                       __global float* d) {
        int gid = get_global_id(0);
        a[gid] = b[gid] * c[gid] + d[gid];
    }
""").build()

def run_test(iterations):
    progress = iterations
    work_size = a.shape[0]

    if progress:
        progress_bar = tqdm(total=iterations,
                            desc='Running test')

    # Операции для расчета производительности

    for i in range(iterations):
        prg.test(queue, (work_size,), None, cl.Buffer(ctx, cl.mem_flags.READ_WRITE, a.nbytes), cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=b),
                 cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=c), cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=d))
        if progress:
            progress_bar.update(1)

    if progress:
        progress_bar.close()

def benchmark_flops_opencl():

    start_time = timeit.default_timer()
    run_test(iterations)
    end_time = timeit.default_timer()

    total_ops = iterations * a.size * 2
    elapsed_time = end_time - start_time
    flops = total_ops / elapsed_time

    return flops

if __name__ == '__main__':
    result = benchmark_flops_opencl()

    if result > 1e9:
        result /= 1e9
        units = "GFLOPS"
    elif result > 1e6:
        result /= 1e6
        units = "MFLOPS"
    elif result > 1e3:
        result /= 1e3
        units = "KFLOPS"
    else:
        units = "FLOPS"

    print(f"Производительность видеокарты с использованием OpenCL: {result:.2f} {units}")
