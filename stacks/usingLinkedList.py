# The first node is referred to as the top element, not the last in the linked. Every new element is inserted at the beginning of the linked list

class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def __iter__(self):
    currentNode = self.head
    while currentNode:
      yield currentNode
      currentNode = currentNode.next

class Stack:
  def __init__(self):
    self.LinkedList = LinkedList()

  def __str__(self) -> str:
    values = [str(x.value) for x in self.LinkedList]
    return '\n'.join(values)
  
  def isEmpty(self):
    if self.LinkedList.head == None:
      return True
    else:
      return False
    
  def push(self,value):
    node = Node(value)
    node.next = self.LinkedList.head #pointing head to new node at beginning
    self.LinkedList.head = node # inserting the new node at the beginning

  def pop(self):
    if self.isEmpty():
      return "The stack is empty"
    else:
      nodeValue = self.LinkedList.head.value #storing head value to return it later.
      self.LinkedList.head = self.LinkedList.head.next # setting the head to the next node, replacing the original head.
      return nodeValue
  
  def peek(self):
    if self.isEmpty():
      return "The stack is empty"
    else:
      nodeValue = self.LinkedList.head.value #storing the head value(top element in the stack)
      return nodeValue
  
  def delete(self):
    self.LinkedList.head = None

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)

print(customStack.peek())
print('--------')
print(customStack.pop())
print('--------')
customStack.delete()
print(customStack)