def fill_balance_factors(root):
    if root is None:
        return 0

    left_height = fill_balance_factors(root.left)
    right_height = fill_balance_factors(root.right)
    root.balance_factor = left_height - right_height
    return 1 + max(left_height, right_height)
