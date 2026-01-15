import timeit
import math
import pyximport
pyximport.install()

from iter4_cython import integrate_cython
from iter1 import integrate

def run_cython_benchmark():
    print("замеры integrate на python и на cython")
    n_iter = 200_000

    python_time = timeit.timeit(lambda: integrate(math.sin, 0, math.pi, n_iter=n_iter), number=5) / 5

    cython_time = timeit.timeit(
        lambda: integrate_cython(0.0, math.pi, n_iter), number=5) / 5

    print(f"python: {python_time:.4f} сек")
    print(f"cython(noGIL): {cython_time:.4f} сек")

if __name__ == "__main__":
    run_cython_benchmark()