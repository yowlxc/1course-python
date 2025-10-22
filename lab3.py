def left_leaf(root: int):
    return root + 1

def right_leaf(root):
    return root - 1

def gen_bin_tree(height, root, l_leaf = left_leaf, r_leaf = right_leaf):
    if height <= 1:
        return {str(root): []}
    return {str(root): [gen_bin_tree(height - 1, l_leaf(root), l_leaf, r_leaf), gen_bin_tree(height - 1, r_leaf(root), l_leaf, r_leaf)]}


def main():
    print(gen_bin_tree(3, 13, left_leaf, right_leaf))
