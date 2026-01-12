import math
from typing import Callable
import concurrent.futures as ftres
from functools import partial
from iter1 import integrate


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