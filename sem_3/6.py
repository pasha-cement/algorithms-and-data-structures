def group_anagrams(a):
    d = {}
    for s in a:
        count = {}
        for x in s:
            count[x] = count.get(x, 0) + 1
        k = frozenset(count.items())
        if k not in d:
            d[k] = []
        d[k].append(s)
    return list(d.values())
