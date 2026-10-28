def feed_animals(a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if b[j] >= a[i]:
            i += 1
        j += 1
    return i
