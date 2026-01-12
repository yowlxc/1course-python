import math
from typing import Callable
import concurrent.futures as ftres
from functools import partial
from iter_1 import integrate


def integrate_processes(f: Callable[[float], float], a: float, b: float, *, n_jobs: int = 2, n_iter: int = 1000) -> float:
    """
    Вычисляет интеграл с использованием ProcessPoolExecutor.

    Аргументы:
        f: Интегрируемая функция.
        a: Левая граница.
        b: Правая граница.
        n_jobs: Количество процессов.
        n_iter: Общее количество итераций.

    Возвращает:
        Приближённое значение интеграла.
    """
    if n_jobs <= 0:
        n_jobs = 1
    if n_iter < n_jobs:
        n_jobs = n_iter or 1

    with ftres.ProcessPoolExecutor(max_workers=n_jobs) as executor:
        step = (b - a) / n_jobs
        fs = []
        for i in range(n_jobs):
            left = a + i * step
            right = a + (i + 1) * step
            iters = n_iter // n_jobs
            if i == n_jobs - 1:
                iters += n_iter % n_jobs
            future = executor.submit(integrate, f, left, right, n_iter=iters)
            fs.append(future)

        return sum(f.result() for f in ftres.as_completed(fs))


# === Пример использования и замер времени ===
if __name__ == "__main__":
    import time

    def benchmark(func, name, f, a, b, n_iter=1_000_000, n_jobs_list=(2, 4, 6, 8)):
        print(f"\n=== {name} ===")
        for n_jobs in n_jobs_list:
            start = time.time()
            result = func(f, a, b, n_jobs=n_jobs, n_iter=n_iter)
            elapsed = time.time() - start
            print(f"n_jobs={n_jobs:2d} → результат: {result:8.6f}, время: {elapsed:.3f} сек")

    # Тестируем на cos(x) от 0 до π
    f = math.cos
    a, b = 0