class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_lists(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.val <= b.val:
        head = a
        a = a.next
    else:
        head = b
        b = b.next
    cur = head
    while a is not None and b is not None:
        if a.val <= b.val:
            cur.next = a
            a = a.next
        else:
            cur.next = b
            b = b.next
        cur = cur.next
    if a is not None:
        cur.next = a
    else:
        cur.next = b
    return head
