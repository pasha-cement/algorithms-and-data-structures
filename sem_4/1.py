class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(a, i=0):
    if i >= len(a) or a[i] is None:
        return None
    root = TreeNode(a[i])
    root.left = build_tree(a, 2 * i + 1)
    root.right = build_tree(a, 2 * i + 2)
    return root
