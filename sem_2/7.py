def remove_duplicates(a):
    j = 0
    for i in range(len(a)):
        if j == 0 or a[i] != a[j - 1]:
            a[j] = a[i]
            j += 1
    while len(a) > j:
        a.pop()
    return a
