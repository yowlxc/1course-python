import math
from libc.math cimport sin

def integrate_cython(double a, double b, long n_iter):
    """Вычисляет интеграл методом прямоугольников (левых)."""
    cdef double acc = 0.0
    cdef double step = (b - a) / n_iter
    cdef long i
    cdef double x
    
    for i in range(n_iter):
        x = a + i * step
        acc += sin(x) * step
    
    return acc