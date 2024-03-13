class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def val(self):
        return self._value

    def write(self, val):
        self._value = val

    def next(self):
        return self._next

    def new_next(self, ptr):
        self._next = ptr


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add(self, node: Node, idx=0):
        if (self.head is None and idx == 0):
            self.head = node
            self.head.new_next(None)
        elif (idx != 0):
            Exception("idx > length of list. Choose another idx <= length of list")
            return
        else:
            for i in range(idx):
                i += 1
                self.head = self.head.next()
