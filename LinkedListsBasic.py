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
        newNode = Node(val)
        if self.head:
            current = self.head
            while current.next:
                if current.val == 3:
                    newNode.next = current.next
                    current.next = newNode
                    break  # Inserted the new node, exit loop
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
