class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def middle_node(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
