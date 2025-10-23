def gen_bin_tree_iterative(height, root, lt=lambda x: x + 1, rt=lambda x: x - 1):

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


print(gen_bin_tree_iterative(3, 13, lambda x: x + 1, lambda x: x - 1))