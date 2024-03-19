# find middle of list
# leetcode:

'''
class ListNode:
    def __init__(self,val=0,next = None):
        self.val = val
        self.next = next
class solution:
    def middlenode(self,head:Optional[ListNode])->Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
        return slow
    '''
# idle:


