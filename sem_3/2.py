def copy_time(n, x, y):
    l = 0
    r = (n - 1) * max(x, y)
    while l < r:
        m = (l + r) // 2
        if m // x + m // y >= n - 1:
            r = m
        else:
            l = m + 1
    return l + min(x, y)
