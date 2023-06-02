import pyopencl as cl
import numpy
import time
# Получаем список доступных платформ
platforms = cl.get_platforms()

# Запрашиваем у пользователя выбор номера видеокарты, если их несколько
if len(platforms) > 1:
    print("Выберите номер платформы:")
    for i in range(len(platforms)):
        print("{}: {}".format(i, platforms[i].name))
    platform_num = int(input("Номер:"))
    platform = platforms[platform_num]
else:
    platform = platforms[0]

# Получаем список доступных устройств
devices = platform.get_devices()

# Запускаем бенчмарк
print("Бенчмарк для платформы {}".format(platform.name))
for device in devices:
    # Создаем контекст для устройства
    ctx = cl.Context([device])
    # Создаем очередь для выполнения команд
    queue = cl.CommandQueue(ctx)

    # Создаем хранилище данных
    a = numpy.random.rand(50000).astype(numpy.float32)
    b = numpy.random.rand(50000).astype(numpy.float32)
    dest = numpy.empty_like(a)

    # Создаем буферы для данных
    mf = cl.mem_flags
    a_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a)
    b_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b)
    dest_buf = cl.Buffer(ctx, mf.WRITE_ONLY, dest.nbytes)

    # Создаем программу
    prg = cl.Program(ctx, """
        __kernel void add(__global const float *a,
                        __global const float *b,
                        __global float *c)
        {
          int gid = get_global_id(0);
          c[gid] = a[gid] + b[gid];
        }
        """).build()

    # Запускаем программу
    start = time.time()
    prg.add(queue, a.shape, None, a_buf, b_buf, dest_buf)
    cl.enqueue_copy(queue, dest, dest_buf)
    end = time.time()

    print("Видеокарта: {}".format(device.name))
    print("Время бенчмарка: {} секунд".format(end - start))