import time
import numpy as np
import cupy as cp

# Generate random data
data_size = 100000000
data = np.random.rand(data_size)

# Transfer data to the GPU
start_time = time.time()
gpu_data = cp.asarray(data)
transfer_time = time.time() - start_time

# Perform computation on the GPU
start_time = time.time()
result = cp.exp(gpu_data)
gpu_time = time.time() - start_time

# Transfer result back to CPU
start_time = time.time()
result_cpu = cp.asnumpy(result)
transfer_time_back = time.time() - start_time

# Print benchmark results
print(f"Data transfer to GPU: {transfer_time:.5f} seconds")
print(f"GPU computation time: {gpu_time:.5f} seconds")
print(f"Data transfer back to CPU: {transfer_time_back:.5f} seconds")
