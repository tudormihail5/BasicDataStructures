class Node:
    def __init__(self, val = None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        newNode = Node(val)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        current = self.head
        while(current):
            print(current.val)
            current = current.next

    def insertMid(self, val):
        if(self.head):
            current = self.head
            while(current.next != None):
                if current.val == 3:
                    newNode = Node(val)
                    a = current.next
                    current.next = newNode
                    newNode.next = a
                current = current.next
        else:
            self.head = newNode


    def deleteLast(self):
        if(self.head):
            current = self.head
            while(current.next.next != None):
                current = current.next
            current.next = None
        else:
            self.head = None

    
    def delete(self, val):
        if(self.head):
            current = self.head
            while(current.next != None):
                if current.next.val == val:
                    a = current.next.next
                    current.next = None
                    current.next = a
                current = current.next
        else:
            self.head = None


    def deleteFirst(self):
        if(self.head):
            current = self.head
            self.head = current.next
        else:
            self.head = None


def main():
    LL = LinkedList()
    LL.insert(3)
    LL.insert(3)
    LL.insert(10)
    LL.insert(3)
    LL.insert(4)
    LL.insert(5)
    LL.insert(6)
    LL.insert(4)
    LL.insert(7)
    LL.printLL()
    print()
    #LL.insertMid(4)
    #LL.printLL()
    x = []
    current = LL.head
    while(current):
        x.append(current.val)
        current = current.next
    x.sort()
    sortedList = LinkedList()
    for i in x:
        sortedList.insert(i)
    sortedList.printLL()
    print()
    current = LL.head
    while(current.next):
        current = current.next
    current.next = sortedList.head
    LL.printLL()


main()
