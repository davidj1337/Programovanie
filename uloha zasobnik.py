class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None
        self.nodesCount = 0

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):

        self.nodesCount += 1

        if self.head == None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):

        self.nodesCount -= 1

        if self.isempty():
            return None

        else:

            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def top(self):

        if self.isempty():
            return None

        else:
            return self.head.data

    def size(self):
        return self.nodesCount


MyStack = Stack()

MyStack.push(5)
MyStack.push(2)
MyStack.pop()
MyStack.push(6)

print("Veľkosť zásobníka je",MyStack.size())
print('Vrchné číslo je', MyStack.top())

if MyStack.isempty():
    print('Zásobník je prázdny')
else:
    print('Zásobník nie je prázdny')
