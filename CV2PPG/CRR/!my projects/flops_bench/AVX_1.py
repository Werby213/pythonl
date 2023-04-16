import timeit
import numpy as np


def benchmark_flops_avx():
    # Операции для расчета производительности
    a = np.ones(256, dtype=np.float32)
    b = np.ones(256, dtype=np.float32) * 2
    c = np.ones(256, dtype=np.float32) * 3
    d = np.ones(256, dtype=np.float32) * 4

    # Запускаем тест на 1 миллион итераций
    iterations = 1000000

    start_time = timeit.default_timer()

    for i in range(iterations):
        a = np.add(np.multiply(b, c), d)

    end_time = timeit.default_timer()

    # Вычисляем количество операций в тесте
    total_ops = iterations * a.size * 2  # умножение и сложение в каждой итерации и на каждый элемент массива
    elapsed_time = end_time - start_time
    flops = total_ops / elapsed_time

    return flops


if __name__ == '__main__':
    # Запускаем бенчмарк и выводим результат в более понятном формате
    result = benchmark_flops_avx()

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

    print(f"Производительность процессора с использованием AVX: {result:.2f} {units}")
