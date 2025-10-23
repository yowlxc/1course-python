import timeit
import matplotlib.pyplot as plt

## РЕКУРСИВНЫЙ АЛГОРИТМ
def left_leaf(root):
    return root + 1

def right_leaf(root):
    return root - 1

def gen_bin_tree_recursive(height, root = 0, lt = left_leaf, rt = right_leaf):
    if height <= 1:
        return {str(root): []}
    return {str(root): [gen_bin_tree_recursive(height - 1, lt(root), lt, rt), 
                        gen_bin_tree_recursive(height - 1, rt(root), lt, rt)]}



## ИТЕРАТИВНЫЙ АЛГОРИТМ
def gen_bin_tree_iterative(height, root = 0, lt=lambda x: x + 1, rt=lambda x: x - 1):

    queue = []
    bin_tree = {str(root): []}

    if height > 1:
        queue.append((str(root), bin_tree[str(root)]))

    while height - 1 > 0:
        for i in range(len(queue)):
            current_root, current_list = queue.pop(0)

            left_leaf = lt(int(current_root))
            right_leaf = rt(int(current_root))
            left_root = {str(left_leaf): []}
            right_root = {str(right_leaf): []}
            current_list.extend([left_root, right_root])

            if height - 2 > 0:
                queue.append((str(left_leaf), left_root[str(left_leaf)]))
                queue.append((str(right_leaf), right_root[str(right_leaf)]))

        height -= 1

    return bin_tree



def benchmark(func, n, number=1, repeat=5):

    times = timeit.repeat(lambda: func(height=n), number=number, repeat=repeat)
    return min(times)


def main():
    test_data = list(range(1, 10))

    res_recursive = []
    res_without_recursive = []

    for n in test_data:
        res_without_recursive.append(benchmark(gen_bin_tree_iterative, n, repeat=3, number=10))
        res_recursive.append(benchmark(gen_bin_tree_recursive, n, repeat=3, number=10))

    # Визуализация
    plt.plot(test_data, res_recursive, label="Рекурсивный")
    plt.plot(test_data, res_without_recursive, label="Итеративный")
    plt.xlabel("Высота дерева")
    plt.ylabel("Время (сек)")
    plt.title("Алгоритмы построения бинарного дерева рекурсивным и итеративным методом")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()