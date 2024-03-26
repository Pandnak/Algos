class Node:
    def __init__(self, val = 0):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, list:list):
        self.head = Node(list[0])
        prev = self.head
        for x in list[1:]:
            cur = Node(x)
            prev.next = cur
            prev = cur
        self.head

def print_list(head):
    cur = head
    while (cur != None):
        print(cur.value, '->', sep = '', end = '')
        cur = cur.next
    print(cur)
