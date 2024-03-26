from custom_types import Node

def delete(head:Node, value):
   prev = None

   while (head != None and head.value == value):
      prev = head
      head = head.next

   cur = head
   while (cur != None):
      if (cur.value == value):
         prev.next = cur.next
      else:
         prev = cur
      cur = cur.next

   return head

def removeElements(head:Node, val):
   dummy = Node()
   dummy.next = head
   prev = dummy
   cur = head
   while (cur != None):
      if (cur.value == val):
         prev.next = cur.next
      else:
         prev = cur
      cur = cur.next

   return dummy.next
