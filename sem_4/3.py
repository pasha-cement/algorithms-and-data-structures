from collections import deque


def min_depth(root):
    if root is None:
        return 0
    q = deque([(root, 1)])
    while q:
        node, d = q.popleft()
        if node.left is None and node.right is None:
            return d
        if node.left is not None:
            q.append((node.left, d + 1))
        if node.right is not None:
            q.append((node.right, d + 1))
