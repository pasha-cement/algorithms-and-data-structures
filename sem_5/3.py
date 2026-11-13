from heapq import heapify, heapreplace


def kth_element(a, k, largest=False):
    if not 1 <= k <= len(a):
        raise ValueError("k is out of range")

    sign = 1 if largest else -1
    heap = [sign * a[i] for i in range(k)]
    heapify(heap)
    for i in range(k, len(a)):
        value = sign * a[i]
        if value > heap[0]:
            heapreplace(heap, value)
    return sign * heap[0]
