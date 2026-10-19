class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_elements(head, val):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    cur = head
    while cur is not None:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return dummy.next
