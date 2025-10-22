def guess_number(target, mas, method):
    k = 0

    if method == "seq":
        for num in mas:
            k += 1
            if num == target:
                return [num, k]
        return [None, k]
    
    elif method == "bin":
        mas.sort()
        if target > mas[len(mas) - 1] or target < mas[0]:
            return [None, 0]
        
        left = 0
        right = len(mas) - 1

        while True:
            k += 1
            if right - left < 2:
                return [None, k]
            
            mid = (right - left) // 2 + left
            
            if mas[mid] > target:
                right = mid
            elif mas[mid] < target:
                left = mid
            elif mas[mid] == target:
                return [mas[mid], k]
            
def helper(mas, format):
    if format == 'interval':
        return [x for x in range (mas[0], mas[1] + 1)]
    else: 
        return mas
