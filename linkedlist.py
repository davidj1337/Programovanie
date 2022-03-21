class LinkedList:
    def __init__(self):
        self.length = 0
        self.headNode = None
        self.tail = None

    def addNode(self, value):
        newNode = Node(value)
        if (self.headNode == None):
            self.headNode = newNode
            return
        else:
            temp = self.headNode
            while (temp.nextNode != None):
                temp = temp.nextNode
            temp.nextNode = newNode

    def getValues(self):
        temp = self.headNode
        if (temp != None):
            print("The list contains:", end=" ")
            while (temp != None):
                print(temp.value, end=" ")
                temp = temp.nextNode
            print()
        else:
            print("The list is empty.")

    def getHead(self):
        return self.headNode


    def getTail(self):
        return self.tail

    def removeValues(self, value):
        if self.headNode is None:
            return None
        else:
            cur = self.headNode
            prev = None
            while cur.value != value and cur.nextNode is not None:
                prev = cur
                cur = cur.nextNode

            # when found
            if cur.value == value:
                # if head
                if cur == self.headNode:
                    if cur.nextNode is None:
                        self.headNode = None
                    else:
                        self.headNode = cur.nextNode
                else:
                    if cur.nextNode is None:
                        prev.nextNode = None
                    else:
                        prev.nextNode = cur.nextNode
            else:
                return None



    def insert(self, value, position):
        newNode = Node(value)
        if (position < 1):
            print("\nposition should be >= 1.")
        elif (position == 1):
            newNode.nextNode = self.headNode
            self.headNode = newNode
        else:
            temp = self.headNode
            for i in range(1, position - 1):
                if (temp != None):
                    temp = temp.nextNode
            if (temp != None):
                newNode.nextNode = temp.nextNode
                temp.nextNode = newNode
            else:
                print("\nThe previous node is null.")

class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

    def getValue(self):
        return self.value

    def setNextNode(self, node):
        self.nextNode = node

dll = LinkedList()
dll.addNode(5)
dll.addNode(4)
dll.addNode(2)
dll.addNode(1)
dll.addNode(0)
dll.insert(10, 2)
dll.removeValues(2)

dll.getValues()
