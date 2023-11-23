from random import randint

class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = None
    self.prev = None
  
  def __str__(self):
    return str(self.value) #printin values as string
  
class LinkedList:
  def __init__(self,values = None):
    self.head = None
    self.tail = None

  def __iter__(self):
    currentNode = self.head
    while currentNode: #enables us to iterate over each value
      yield currentNode
      currentNode = currentNode.next

  def __str__(self):
    values = [str(x.value) for x in self]
    return ' -> '.join(values) #printing them to look like a real list
  
  def __len__(self):
    result = 0 #initializing
    node = self.head  #starting from the beginning
    while node:
      result += 1
      node = node.next
    return result
  
  def add(self,value):
    if self.head is None:
      newNode = Node(value)
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = Node(value) #adding at the end of the list
      self.tail = self.tail.next 
    return self.tail
  
  def generate(self,n,min_value,max_value): # enables us generate/randomize a list
    self.head = None
    self.tail = None
    for i in range(n):
      self.add(randint(min_value,max_value))
    return self
  
# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# print(len(customLL))