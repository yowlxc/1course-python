import timeit
import math
import pyximport
pyximport.install()
import concurrent.futures

from iter4_cython import integrate_cython
from iter1 import integrate

def threads_cython(n_jobs, n_iter):
    step = math.pi / n_jobs
    n_per = n_iter // n_jobs
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as ex:
        futures = [
            ex.submit(integrate_cython, i * step, (i + 1) * step, n_per)
            for i in range(n_jobs)
        ]
        return sum(f.result() for f in futures)

print("замеры cython + многопоточность")
for n_jobs in [4, 6, 8]:
    n_iter = 100000
    time = timeit.timeit(lambda: threads_cython(n_jobs, n_iter), number=5) / 5
    print(f"при n_jobs = {n_jobs} и n_iter = 100000: {time:.4f} сек")