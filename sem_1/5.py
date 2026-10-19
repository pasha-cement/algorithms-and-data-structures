def sort_colors(a):
    l = 0
    i = 0
    r = len(a) - 1
    while i <= r:
        if a[i] == 0:
            a[l], a[i] = a[i], a[l]
            l += 1
            i += 1
        elif a[i] == 1:
            i += 1
        else:
            a[i], a[r] = a[r], a[i]
            r -= 1
    return a
