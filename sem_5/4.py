def kth_in_bst(root, k, largest=False):
    if k < 1:
        raise ValueError("k is out of range")

    stack = []
    node = root
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.right if largest else node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.data
        node = node.left if largest else node.right

    raise ValueError("k is out of range")
