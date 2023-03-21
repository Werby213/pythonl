import pyopencl as cl
import numpy as np
import time

# Запрашиваем номер видеокарты для проверки и сложность
try:
    dev_num = int(input('Input device number: '))
    difficulty = int(input('Input difficulty (1-10): '))
except ValueError:
    print('Incorrect value')
    dev_num = 0
    difficulty = 1

# Создаём контекст
context = cl.create_some_context()

# Получаем дескриптор устройства
device = context.devices[dev_num]

# Создаём очередь команд
queue = cl.CommandQueue(context, device)

# Создаём буфер с данными
N = difficulty * 10000
data = np.zeros(N, dtype=np.float32)

mf = cl.mem_flags
data_buf = cl.Buffer(context, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=data)

# Задаём исходник программы
prg = cl.Program(context, """
    __kernel void benchmark(__global float *data) {
        int gid = get_global_id(0);
        float a = 0;
        for (int i = 0; i < 1000; i++) {
            a += sqrt(1.0f * gid);
        }
        data[gid] = a;
    }
    """).build()

# Запускаем программу
start_time = time.time()
prg.benchmark(queue, (N, ), None, data_buf)

# Перемещаем результат в основную память
cl.enqueue_copy(queue, data, data_buf)

end_time = time.time()
score = (end_time - start_time) * 1000

# Выводим результат
print('Score:', score)