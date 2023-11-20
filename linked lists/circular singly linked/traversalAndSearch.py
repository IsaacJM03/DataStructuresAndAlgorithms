class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
            

    #  Creation of circular singly linked list
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"
    
    #  Insertion of a node in circular singly linked list

    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node has been successfully inserted"
    
    # traversal 
    def traverseCSLL(self):
        if self.head is None:
            print("The CSLL does not exist")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
          
    # search(linear) with traversal
    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "The CSLL does not exist"
        else:
            tempNode = self.head #starting from the beginning
            while tempNode:
                if tempNode.value == nodeValue:
                    return "Is at index {}".format(tempNode.value)
                if tempNode == self.tail:
                    return "The value does not exist"
                tempNode = tempNode.next


circular = CircularSinglyLinkedList()
circular.createCSLL(0)
circular.insertCSLL(3,0)
circular.insertCSLL(1,1)
circular.insertCSLL(2,1)
circular.insertCSLL(3,1)
circular.insertCSLL(4,1)
circular.insertCSLL(0,-1)
print(circular.searchCSLL(3))
print([node.value for node in circular]) 