def left_leaf(root):
    return root + 1

def right_leaf(root):
    return root - 1

def gen_bin_tree(height, root, lt = left_leaf, rt = right_leaf):
    if height <= 1:
        return {str(root): []}
    return {str(root): [gen_bin_tree(height - 1, lt(root), lt, rt), 
                        gen_bin_tree(height - 1, rt(root), lt, rt)]}

print(gen_bin_tree(3, 13, left_leaf, right_leaf))
