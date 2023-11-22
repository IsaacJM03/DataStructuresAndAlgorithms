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

  # delete node
  def delNode(self,location):
    if self.head is None:
      print("The Circular Doubly Linked List does not exist")
    else:
      if location == 0:
        if self.head == self.tail:
          self.head.prev = None
          self.head.next = None
          self.head = None
          self.tail = None
        else:
          self.head = self.head.next
          self.head.prev = self.tail
          self.tail.next = self.head
      elif location == -1:
        if self.head == self.tail:
          self.head.prev = None
          self.head.next = None
          self.head = None
          self.tail = None
        else:
          self.tail = self.tail.prev
          self.tail.next = self.head
          self.head.prev = self.tail
      else:
        currentNode = self.head
        index = 0
        while index < location - 1:
          currentNode = currentNode.next
          index += 1
        currentNode.next = currentNode.next.next 
        currentNode.next.prev = currentNode
      print("The node has been successfully deleted")

  # deleting entire list
  def delEntireCDLL(self):
    if self.head is None:
      print("The Circular Doubly Linked List does not exist")
    else:
      self.tail.next = None
      tempNode = self.head
      while tempNode:
        tempNode.prev = None
        tempNode = tempNode.next
      self.head = None 
      self.tail = None
      print("The List has been successfully deleted")

circularDLL = CircularDLL()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
print([node.value for node in circularDLL])
circularDLL.delNode(5)
circularDLL.delEntireCDLL()
print([node.value for node in circularDLL])