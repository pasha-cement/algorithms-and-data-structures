def integer_sqrt(n):
    l = 0
    r = n
    while l <= r:
        m = (l + r) // 2
        if m * m > n:
            r = m - 1
        elif m * m < n:
            l = m + 1
        else:
            return m
    return r
