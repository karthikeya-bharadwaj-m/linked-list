class node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def createll(self,n):#dynamic linked list creation
        i = 0
        while i<n:
            newnode = node(input("enter values:"))
            if self.head == None:
                self.head = newnode
            else:
                t = self.head
                while t.next:
                    t = t.next
                t.next = newnode
            i+=1
            
        
    def show(self):
        t=self.head
        while t:
            print(t.value,end="->")
            t=t.next
    def reverse(self,head):
        prev=None
        while head:
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
        self.head=prev
        return prev
obj=Linkedlist() #object creation
'''obj.head=node(1)
obj.head.next=node(2)
obj.head.next.next=node(3)
obj.head.next.next.next=node(4)
obj.head.next.next.next.next=node(5)'''
obj.createll(5)
obj.show()
obj.reverse(obj.head)
print("\n reverselist")
obj.show()
