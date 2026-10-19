def move_zeros(a):
    j = 0
    for i in range(len(a)):
        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j += 1
    return a
