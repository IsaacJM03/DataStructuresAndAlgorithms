class Node:
    def __init__(self, value=None):
        # defining the next reference on each node
        self.value = value
        self.next = None

class CSLinkedList:
    # defining the head and tail of list
    def __init__(self):
        self.head = None
        self.tail = None

  # helps us to iterate over the linked list

    '''
    This code defines an iterator for a linked list. It starts from the head of the list and yields each node in the list until it reaches the tail. The yield keyword allows the iterator to be used in a for loop. The if statement checks if the iterator has reached the end of the list and breaks the loop if it has.
    '''
    def __iter__(self):
      node = self.head
      while node:
        yield node
        node = node.next
        if node == self.tail.next:
           break

  # creation of circular singly linked list with one node
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The Circular Singly Linked List has been created"
    
  # insertion of node
    def insertCSLL(self,value,location):
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
             while index < location -1: #the one just before the location
                tempNode = tempNode.next
                index += 1
             nextNode = tempNode.next
             tempNode.next = newNode
             newNode.next = nextNode
          return "The node has been successfully inserted"

circular = CSLinkedList()
circular.createCSLL(0)
circular.createCSLL(2)
circular.insertCSLL(3,0)
circular.insertCSLL(1,1)
circular.insertCSLL(2,1)
circular.insertCSLL(3,1)
circular.insertCSLL(4,2)
circular.insertCSLL(0,-1)

print([node.value for node in circular])
