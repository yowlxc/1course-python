import math
from typing import Callable

# итерация 1
def integrate(f: Callable[[float], float], a: float, b: float, *, n_iter: int = 100000) -> float:
    """Вычисляет интеграл непрерывной функции на отрезке.

    Аргументы:
        f (float -> float): Интегрируемая функция.
        a (float): Левая граница интервала.
        b (float): Правая граница интеграла.
        n_iter (int): Количество итераций.

    Возвращает:
        float: Определенный интегрпал функции на интервале.

    Пример:
        >>> integrate(math.cos, 0, math.pi, n_iter = 1000)
        0.0031415926535898094

        >>> integrate(lambda x: 4*x**2 + 5*x + 1, -4, -1)
        49.500675001800865
    """
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i*step) * step
    return acc

if __name__ == "__main__":
    import doctest
    doctest.testmod()
# print(integrate(math.cos, 0, math.pi, n_iter = 1000))