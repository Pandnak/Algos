from custom_types import Node

def find_middle(head:Node):
    slow = fast = head

    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next

    return slow
