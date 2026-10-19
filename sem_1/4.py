def sort_binary(a):
    l = 0
    r = len(a) - 1
    while l < r:
        if a[l] == 0:
            l += 1
        else:
            a[l], a[r] = a[r], a[l]
            r -= 1
    return a
