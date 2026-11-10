def is_same_tree(a, b):
    if a is None or b is None:
        return a is b
    if a.data != b.data:
        return False
    return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)
