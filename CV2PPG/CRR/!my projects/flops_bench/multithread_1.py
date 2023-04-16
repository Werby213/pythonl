import timeit


def benchmark_flops():
    # Операции для расчета производительности
    a = 1.0
    b = 2.0
    c = 3.0
    d = 4.0

    # Запускаем тест на 1 миллион итераций
    iterations = 10000000

    start_time = timeit.default_timer()

    for i in range(iterations):
        a = b * c + d

    end_time = timeit.default_timer()

    # Вычисляем количество операций в тесте
    total_ops = iterations * 2  # умножение и сложение в каждой итерации
    elapsed_time = end_time - start_time
    flops = total_ops / elapsed_time

    return flops


if __name__ == '__main__':
    # Запускаем бенчмарк и выводим результат в более понятном формате
    result = benchmark_flops()

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

    print(f"Производительность процессора: {result:.2f} {units}")