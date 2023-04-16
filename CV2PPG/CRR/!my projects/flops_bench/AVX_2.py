import timeit
import numpy as np
import multiprocessing
from tqdm import tqdm

a = np.ones(256, dtype=np.float32)
b = np.ones(256, dtype=np.float32)
c = np.ones(256, dtype=np.float32)
d = np.ones(256, dtype=np.float32)


def run_test(args):
    iterations, progress = args
    if progress:
        progress_bar = tqdm(total=iterations, desc='Running test'+ " on " + str(multiprocessing.cpu_count())+ " cpu cores")

    # Операции для расчета производительности

    for i in range(iterations):
        a = np.add(np.multiply(b, c), d)

        if progress:
            progress_bar.update(1)

    if progress:
        progress_bar.close()


def benchmark_flops_avx():
    # Запускаем тест на 1 миллион итераций
    iterations = 1000000

    # Запускаем тест в несколько процессов для задействования всех ядер процессора
    with multiprocessing.Pool() as pool:
        start_time = timeit.default_timer()
        pool.map(run_test, [(iterations, True)] * multiprocessing.cpu_count())
        end_time = timeit.default_timer()

    # Определяем количество операций в тесте
    total_ops = iterations * a.size * 2 * multiprocessing.cpu_count()  # умножение и сложение в каждой итерации и на каждый элемент массива, умножаем на количество процессов
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

    print(f"Производительность процессора с использованием AVX и задействованием всех ядер: {result:.2f} {units}")
