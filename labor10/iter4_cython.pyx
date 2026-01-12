import math
from libc.math cimport cos, sin, sqrt

cdef double integrate_cython(double (*f)(double), double a, double b, long n_iter):
    """Вычисляет интеграл методом прямоугольников (левых)."""
    cdef double acc = 0.0
    cdef double step = (b - a) / n_iter
    cdef long i
    cdef double x
    
    for i in range(n_iter):
        x = a + i * step
        acc += f(x) * step
    
    return acc