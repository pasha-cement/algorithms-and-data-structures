def extra_letter(a, b):
    count = {}
    for x in b:
        count[x] = count.get(x, 0) + 1
    for x in a:
        count[x] -= 1
    for x in count:
        if count[x] > 0:
            return x
    return ""
