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

  # deletion of a node
  def delNode(self,location):
    if self.head is None:
      print("There is no element in this list")
    else:
      if location == 0:
        if self.head == self.tail: # only one node at beginning of list
          self.head = None
          self.tail = None
        else:
          self.head = self.head.next
          self.head.prev = None
      elif location == -1: 
        if self.head == self.tail: #only one node at the end of the list
          self.head = None
          self.tail = None
        else:
          self.tail = self.tail.prev
          self.tail.next = None
      else:
        curNode = self.head
        index = 0
        while index < location - 1:
          curNode = curNode.next
          index += 1
        curNode.next = curNode.next.next
        curNode.next.prev = curNode
      print("The node has successfully been deleted")

    # deleting entire list

  def delDLL(self):
    if self.head is None:
      print("There is no element in this list")
    else:
      tempNode = self.head
      while tempNode:
        tempNode.prev = None
        tempNode = tempNode.next
      self.head = None
      self.tail = None
      print("The list has been successfully deleted")



doublylist = DoublyLinkedList()
doublylist.createDLL(3)
doublylist.insertDLL(2,0)
doublylist.insertDLL(2,1)
doublylist.insertDLL(2,2)
doublylist.insertDLL(5,-1)
doublylist.insertDLL(15,-1)

print([node.value for node in doublylist])
doublylist.delNode(-1)
print([node.value for node in doublylist])
doublylist.delDLL()
print([node.value for node in doublylist])