def sum_of_2(nums, target):
    if int(len(num)) < 2: return None                           # проверка на пустой массив/массив с одним элементом
    for x in nums: if int(x) != x: return None                  # проверка на другой тип данных (не int)
    for i in range(0, int(len(nums)) - 1):                      # проход по массиву
        for j in range (i + 1, int(len(nums))):                 # проход по массиву от индекса i до конца (перебор всех пар массива)
            if nums[i] + nums[j] == target:
                res = []
                res = res + [i] + [j]
                return res
    return None                                                 # None, когда не нашлись подходящие по условию числа в массиве

