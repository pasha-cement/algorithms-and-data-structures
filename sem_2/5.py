def two_sum(a, target):
    l = 0
    r = len(a) - 1
    while l < r:
        s = a[l] + a[r]
        if s == target:
            return True
        elif s < target:
            l += 1
        else:
            r -= 1
    return False
