class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = None
    self.prev = None

class CircularDLL:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next
      if node == self.tail.next: #to prevent infinite loops
        break
  
  # creation
  def createCDLL(self, nodeValue):
    newNode = Node(nodeValue)
    self.head = newNode
    self.tail = newNode
    newNode.prev = newNode
    newNode.next = newNode
  
  # insertion
  def insertCDLL(self, value, location):
    if self.head is None:
      return "The CDLL does not exist"
    else:
      newNode = Node(value)
      if location == 0:
        newNode.next = self.head
        newNode.prev = self.tail
        self.head.prev = newNode
        self.head = newNode
        self.tail.next =  newNode
      elif location == -1:
        newNode.next = self.head
        newNode.prev = self.tail
        self.head.prev = newNode
        self.tail.next = newNode
        self.tail = newNode
      else:
        tempNode = self.head
        index = 0
        while index < location - 1:
          tempNode = tempNode.next
          index += 1
        newNode.next = tempNode.next
        newNode.prev = tempNode
        newNode.next.prev = newNode
        tempNode.next = newNode
      return "The node has been successfully inserted"
    
  # reverse traversal
  def reverseTraverseCDLL(self):
    if self.head is None:
      return "The Circular Doubly Linked List does not exist"
    else:
      tempNode = self.tail
      while tempNode:
        print(tempNode.value)
        if tempNode == self.head:
          break
        tempNode = tempNode.prev

  # searching
  def searchCDLL(self,nodeValue):
    if self.head is None:
      return "The List does not exist"
    else:
      tempNode = self.head
      while tempNode:
        if tempNode.value == nodeValue:
          return "The value {} exists in the List.".format(tempNode.value)
        if tempNode == self.tail:
          return "The value {} does not exist in the List.".format(nodeValue)
        tempNode = tempNode.next
    


circularDLL = CircularDLL()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
circularDLL.reverseTraverseCDLL()
print(circularDLL.searchCDLL(4))
print([node.value for node in circularDLL])