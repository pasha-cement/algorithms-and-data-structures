class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head):
    prev = None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
