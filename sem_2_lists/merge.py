from custom_types import Node

def merge_lists(a : Node, b:Node):
    a_node, b_node = a.head, b.head
    head = None
    while (a_node != None and b_node != None):
        if (a_node.value > b_node.value):
            p = b_node.next
            b_node.next = a_node
            if (head == None):
                head = b_node
            b_node = p
        else:
            p = a_node.next
            a_node.next = b_node
            if (head == None):
                head = a_node
            a_node = p

    return head
