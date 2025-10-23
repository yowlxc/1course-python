from lab3 import left_leaf
from lab3 import right_leaf
from lab3 import gen_bin_tree

import unittest

# тесты
class TestMath(unittest.TestCase):
    def test_1(self):
        self.assertEqual(gen_bin_tree(3, 10, left_leaf, right_leaf), ({'10': [{'11': [{'12': []}, {'10': []}]}, {'9': [{'10': []}, {'8': []}]}]}))

    def test_2(self):
        self.assertEqual(gen_bin_tree(4, 23, left_leaf, right_leaf), ({'23': [{'24': [{'25': [{'26': []}, {'24': []}]}, {'23': [{'24': []}, {'22': []}]}]}, {'22': [{'23': [{'24': []}, {'22': []}]}, {'21': [{'22': []}, {'20': []}]}]}]}))
                         
    def test_3(self):
        self.assertEqual(gen_bin_tree(2, 15, left_leaf, right_leaf), ({'15': [{'16': []}, {'14': []}]})) 

    def test_4(self):
        self.assertEqual(gen_bin_tree(1, 256, left_leaf, right_leaf), ({'256': []}))

if __name__ == '__main__':
    unittest.main()
