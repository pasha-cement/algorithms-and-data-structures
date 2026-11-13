from collections import deque


def is_complete_tree(root):
    queue = deque([root])
    gap = False
    while queue:
        node = queue.popleft()
        if node is None:
            gap = True
        else:
            if gap:
                return False
            queue.append(node.left)
            queue.append(node.right)
    return True
