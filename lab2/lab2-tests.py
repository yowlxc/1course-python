from lab2 import guess_number
from lab2 import helper

import unittest

# тесты
class TestMath(unittest.TestCase):
    def test_1(self):
        self.assertEqual(guess_number(12, helper([1, 70], 'interval'), 'seq'), [12, 12])                     # медленный поиск на интервале

    def test_2(self):
        self.assertEqual(guess_number(12, helper([1, 70], 'interval'), 'bin'), [12, 6])                      # бинарный поиск на интервале

    def test_3(self):
        self.assertEqual(guess_number(76, helper([1, 85, 34, 93, 258, 87, 45, 54, 67, 76, 91, 19, 57, 25, 123, 70], 'no'), 'seq'), [76, 10])       # медленный поиск по массиву

    def test_4(self):
        self.assertEqual(guess_number(76, helper([1, 85, 34, 93, 258, 87, 45, 54, 67, 76, 91, 19, 57, 25, 123, 70], '-'), 'bin'), [76, 3])              # бинарный поиск по массиву

    def test_5(self):
        self.assertEqual(guess_number(71, helper([1, 70], 'interval'), 'seq'), [None, 70])                        # медленный поиск числа вне интервала (больше максимального значения списка)

    def test_6(self):
        self.assertEqual(guess_number(71, helper([1, 70], 'interval'), 'bin'), [None, 0])                      # бинарный поиск вне массива (больше максимального элемента)

    def test_7(self):
        self.assertEqual(guess_number(0, helper([1, 70], 'interval'), 'seq'), [None, 70])                        # медленный поиск числа вне интервала (меньше максимального значения списка)

    def test_8(self):
        self.assertEqual(guess_number(0, helper([1, 70], 'interval'), 'bin'), [None, 0])                        # бинарный поиск вне массива (меньше максимального элемента)

    def test_9(self):
        self.assertEqual(guess_number(12, helper([1, 85, 34, 93, 258, 87, 45, 54, 67, 76, 91, 19, 57, 25, 123, 70], 'no'), 'seq'), [None, 16])       # ненаход числа (нет в списке)

    def test_10(self):
        self.assertEqual(guess_number(12, helper([1, 85, 34, 93, 258, 87, 45, 54, 67, 76, 91, 19, 57, 25, 123, 70], '-'), 'bin'), [None, 4])              # ненаход числа (нет в списке)

if __name__ == '__main__':
    unittest.main()




