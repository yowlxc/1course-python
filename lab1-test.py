import unittest

def sum_of_2(nums, target):
    if int(len(nums)) < 2: return None 
    for x in nums: 
        if int(x) != x: return None 
    for i in range(0, int(len(nums)) - 1):
        for j in range (i + 1, int(len(nums))):
            if nums[i] + nums[j] == target:
                res = []
                res = res + [i] + [j]
                return res
    return None 

# тесты
class TestMath(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_of_2([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(sum_of_2([3, 2, 4], 6), [1, 2])
        self.assertEqual(sum_of_2([3, 3], 6), [0, 1])

    def test_2_positive(self):
        self.assertEqual(sum_of_2([7, 3, 2, 10], 10), [0, 1])                     # крайние значение слева

    def test_3_positive(self):
        self.assertEqual(sum_of_2([1, 1, 2, 3, 5, 8, 13, 21], 34), [6, 7])        # крайние значения справа 

    def test_4_positive(self):
        self.assertEqual(sum_of_2([3, 3, 3, 3, 3, 3], 6), [0, 1])                 # любые два различных индекса подходят под условие

    def test_5_negative(self):
        self.assertEqual(sum_of_2([7, 3, 2, 56], 6), None)                        # нет подходящих чисел в массиве

    def test_6_negative(self):
        self.assertEqual(sum_of_2([1], 0), None)                                  # недостаточно элементов в массиве

    def test_7_negative(self):
        self.assertEqual(sum_of_2(['456', 3], 6), None)                           # в массиве есть не int-овые элементы (string)

if __name__ == '__main__':
    unittest.main()


