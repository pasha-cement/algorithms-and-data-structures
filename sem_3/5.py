def two_sum(a, target):
    d = {}
    for i in range(len(a)):
        x = target - a[i]
        if x in d:
            return [d[x], i]
        d[a[i]] = i
    return []
