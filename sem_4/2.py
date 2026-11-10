def mirror(a, b):
    if a is None or b is None:
        return a is b
    if a.data != b.data:
        return False
    return mirror(a.left, b.right) and mirror(a.right, b.left)


def is_symmetric(root):
    if root is None:
        return True
    return mirror(root.left, root.right)
