import timeit
import math
from iter2_threads import integrate_threads
from iter3_processes import integrate_processes

def bench(func, *args, **kwargs):
    return timeit.timeit(lambda: func(*args, **kwargs), number=5) / 5

def iter23_benchmark():
    print("Сравнение потоков и процессов")
    for n_jobs in [2, 4, 6, 8]:
        for n_iter in [10_000, 50_000, 100_000]:
            t_threads = bench(integrate_threads, math.sin, 0, math.pi,
                          n_jobs=n_jobs, n_iter=n_iter)
            t_procs = bench(integrate_processes, math.sin, 0, math.pi,
                        n_jobs=n_jobs, n_iter=n_iter)
            print(f"при n_iter={n_iter} и n_jobs={n_jobs}: используя потоки - {t_threads:.4f} сек, используя процессы - {t_procs:.4f} сек")

if __name__ == "__main__":
    iter23_benchmark()