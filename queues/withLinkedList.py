class Node:
  def __init__(self,value=None):
    self.value = value
    self.next = None

  def __str__(self) -> str:
    return str(self.value)
  
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def __iter__(self):
    curNode = self.head
    while curNode:
      yield curNode 
      curNode = curNode.next 
  
class Queue:
  def __init__(self):
    self.linkedList = LinkedList()

  def __str__(self):
    values = [str(x.value) for x in self.linkedList]
    return ' '.join(values)

  def enqueue(self,value):
    newNode = Node(value)
    if self.linkedList.head is None: #if at beginning and only node
      self.linkedList.head = newNode
      self.linkedList.tail = newNode
    else:
      self.linkedList.tail.next = newNode
      self.linkedList.tail = newNode

  def isEmpty(self):
    if self.linkedList.head is None:
      return True
    else:
      return False

  def dequeue(self):
    if self.isEmpty():
      return "There is no element in the Queue"
    else:
      tempNode = self.linkedList.head
      if self.linkedList.head == self.linkedList.tail: #only one node
        self.linkedList.head = None
        self.linkedList.tail = None
      else:
        self.linkedList.head = self.linkedList.head.next
      return tempNode

  def peek(self):
    if self.isEmpty():
      return "There is no element in the Queue"
    else:
      return self.linkedList.head

  def delete(self):
    self.linkedList.head = None
    self.linkedList.tail = None

custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)
print(custQueue.dequeue())
print(custQueue)