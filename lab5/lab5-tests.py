from lab5 import gen_bin_tree_iterative

import unittest

# тесты
class TestMath(unittest.TestCase):
    def test_1(self):
        self.assertEqual(gen_bin_tree_iterative(3, 10, lambda x: x + 1, lambda x: x - 1), ({'10': [{'11': [{'12': []}, {'10': []}]}, {'9': [{'10': []}, {'8': []}]}]}))

    def test_2(self):
        self.assertEqual(gen_bin_tree_iterative(4, 23, lambda x: x + 1, lambda x: x - 1), ({'23': [{'24': [{'25': [{'26': []}, {'24': []}]}, {'23': [{'24': []}, {'22': []}]}]}, {'22': [{'23': [{'24': []}, {'22': []}]}, {'21': [{'22': []}, {'20': []}]}]}]}))
                         
    def test_3(self):
        self.assertEqual(gen_bin_tree_iterative(2, 15, lambda x: x + 1, lambda x: x - 1), ({'15': [{'16': []}, {'14': []}]})) 

    def test_4(self):
        self.assertEqual(gen_bin_tree_iterative(1, 256, lambda x: x + 1, lambda x: x - 1), ({'256': []}))

if __name__ == '__main__':
    unittest.main()
