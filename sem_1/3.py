def merge(a, b):
    i = len(a) - len(b) - 1
    j = len(b) - 1
    k = len(a) - 1
    while j >= 0:
        if i >= 0 and a[i] > b[j]:
            a[k] = a[i]
            i -= 1
        else:
            a[k] = b[j]
            j -= 1
        k -= 1
    return a
