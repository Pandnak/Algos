from custom_types import Node

def reverseLinkedList(head : Node):
    prev = None
    current = head

    while (current != None):
        next = current.next
        current.next = prev
        prev = current
        current = next

    head = prev
    return head
