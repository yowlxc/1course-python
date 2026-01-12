import timeit
import math
from iter1 import integrate

def integrate_benchmark():
    print('Замеры времени для простой integrate на python')
    for n in [10_000, 50_000, 100_000]:
        time_taken = timeit.timeit(lambda: integrate(math.sin, 0, math.pi, n_iter=n), number=5) / 5
        print(f"для n_iter = {n:>6,} : {time_taken:.4f} секунд")

if __name__ == "__main__":
    integrate_benchmark()