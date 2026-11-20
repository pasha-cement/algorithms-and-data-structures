def longest_increasing_run(a):
    if not a:
        return 0

    count = 1
    res = 1
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            count += 1
        else:
            count = 1
        res = max(res, count)
    return res
