def oddeven(self,head):
    odd = head
    even = head.next
    while odd and odd.next.next:


#delete a node:
class listnode:
    def __init__(self, x):
        self.val = x
        self.next = None
class solution:
    def deletenode(self,node):
        node.val = node.next.val
        node.next = node.next.next
