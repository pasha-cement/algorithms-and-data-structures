from heapq import heapify, heappop, heappush


def merge_sorted_arrays(arrays):
    heap = []
    for i, array in enumerate(arrays):
        if array:
            heap.append((array[0], i, 0))
    heapify(heap)

    result = []
    while heap:
        value, i, j = heappop(heap)
        result.append(value)
        j += 1
        if j < len(arrays[i]):
            heappush(heap, (arrays[i][j], i, j))
    return result
