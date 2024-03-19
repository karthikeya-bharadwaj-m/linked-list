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
                while t.next:
                    break
            i+=1
        newnode.next = self.head.next
    def show(self):
        t=self.head
        while t:
            print(t.value,end="->")
            t=t.next
            ch = input("enter (y/n)")
            if ch == 'n' :
                break
            


obj = Linkedlist()
obj.createll(4)
obj.show()
