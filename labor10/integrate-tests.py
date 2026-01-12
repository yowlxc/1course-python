import unittest
import math
from iter_1 import integrate

# тесты
class TestMath(unittest.TestCase):
    def test_command_cases(self):
        self.assertAlmostEqual(integrate(math.cos, 0, math.pi, n_iter = 1000), 0, delta = 0.01)
        self.assertAlmostEqual(integrate(lambda x: 4*x**2 + 5*x + 1, -4, -1), 49.5, places = 2)

    def test_precision(self):
        # precision - 0.001
        try:
            self.assertAlmostEqual(integrate(math.cos, 0, math.pi, n_iter = 1000), 0, delta = 0.001)
        except Exception as e:
            self.assertIsInstance(e, AssertionError)
        self.assertAlmostEqual(integrate(math.cos, 0, math.pi, n_iter = 10000), 0, delta = 0.001)

        # precision - 0.0001
        try:
            self.assertAlmostEqual(integrate(math.cos, 0, math.pi, n_iter = 10000), 0, delta = 0.0001)
        except Exception as e:
            self.assertIsInstance(e, AssertionError)
        self.assertAlmostEqual(integrate(math.cos, 0, math.pi, n_iter = 100000), 0, delta = 0.0001)

if __name__ == '__main__':
    unittest.main()


