def min_max_product(a):
    if not a or a[0] is None:
        return None
    i = 0
    j = 0
    while 2 * i + 1 < len(a) and a[2 * i + 1] is not None:
        i = 2 * i + 1
    while 2 * j + 2 < len(a) and a[2 * j + 2] is not None:
        j = 2 * j + 2
    return a[i] * a[j]
