def reverse(a, l, r):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1


def rotate(a, k):
    n = len(a)
    if n == 0:
        return a
    k %= n
    reverse(a, 0, n - 1)
    reverse(a, 0, k - 1)
    reverse(a, k, n - 1)
    return a
