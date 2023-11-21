# node class different from singly linked one

from lib2to3.pgen2.token import DOUBLESLASH


class Node:
  def __init__(self,value = None):
    self.value = value
    self.next = None
    self.prev = None
  
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next

  # Creation of Doubly Linked list
  def createDLL(self, nodeValue):
    node = Node(nodeValue)
    node.prev = None
    node.next = None
    self.head = node
    self.tail = node
    return "The Doubly Linked List has been created"
  
  # insertion
  def insertDLL(self, nodeValue, location):
    if self.head is None:
      print("This Linked List does not exist")
    else:
      newNode = Node(nodeValue)
      if location == 0:
        newNode.prev = None
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
      elif location == -1:
        newNode.next = None
        newNode.prev = self.tail 
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

  # reverse traversal
  def reverseTraverseDLL(self):
    if self.head is None:
      return "This Linked List does not exist"
    else:
      tempNode = self.tail
      while tempNode is not None:
        print(tempNode.value)
        tempNode = tempNode.prev

  # linear search
  def searchDLL(self, nodeValue):
    if self.head is None:
      return "This Linked List does not exist"
    else:
      tempNode = self.head
      while tempNode is not None:
        if tempNode.value == nodeValue:
          return "Value {}".format(tempNode.value) + " exists in the DLL"
        tempNode = tempNode.next
      return "The value does not exist"


doublylist = DoublyLinkedList()
doublylist.createDLL(3)
doublylist.insertDLL(2,0)
doublylist.insertDLL(2,1)
doublylist.insertDLL(2,2)
doublylist.insertDLL(5,-1)
doublylist.insertDLL(15,-1)

print([node.value for node in doublylist])
print(doublylist.searchDLL(15))
print([node.value for node in doublylist])