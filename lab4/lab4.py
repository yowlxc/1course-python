import timeit
import matplotlib.pyplot as plt
import random

from functools import lru_cache

def fact_recursive(n: int) -> int:
    """Рекурсивный факториал без кэширования"""
    if n == 0:
        return 1
    return n * fact_recursive(n - 1)

def fact_iterative(n: int) -> int:
    """Нерекурсивный факториал без кэширования"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

@lru_cache(maxsize=128)
def fact_recursive_cache(n: int) -> int:
    """Рекурсивный факториал с кэшированием"""
    if n == 0:
        return 1
    return n * fact_recursive_cache(n - 1)

@lru_cache(maxsize=128)
def fact_iterative_cache(n: int) -> int:
    """Нерекурсивный факториал с кэшированием"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def benchmark(func, data, number=1, repeat=10):
    """Возвращает среднее время выполнения func(n)"""
    ttl = 0
    for x in data:
        times = timeit.repeat(lambda: func(x), number=number, repeat=repeat)
        ttl += min(times)
    return ttl / len(data)


def main():
    # фиксированный набор данных
    random.seed(42)
    test_data = list(range(10, 300, 10))

    res_recursive = []
    res_iterative = []
    res_recursive_cache = []
    res_iterative_cache = []

    for n in test_data:
      res_recursive.append(benchmark(fact_recursive, [n], number=5000, repeat=5))
      res_iterative.append(benchmark(fact_iterative, [n], number=5000, repeat=5))
      res_recursive_cache.append(benchmark(fact_recursive_cache, [n], number=5000, repeat=5))
      res_iterative_cache.append(benchmark(fact_iterative_cache, [n], number=5000, repeat=5))

    # Визуализация
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(test_data, res_recursive, label="Рекурсивный без кэширования")
    plt.plot(test_data, res_iterative, label="Итеративный без кэширования")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение рекурсивного и итеративного факториала без кэширования")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(test_data, res_recursive_cache, label="Рекурсивный с кэшированием")
    plt.plot(test_data, res_iterative_cache, label="Итеративный с кэшированием")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение рекурсивного и итеративного факториала с кэшированием")
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()