class Node():
  def __init__(self,value=None,next=None):
    self.value = value
    self.next = next

  def __str__(self) -> str:
    string = str(self.value)
    if self.next:
      string += ',' + str(self.next)
    return string
  
class Stack():
  def __init__(self) -> None:
    self.top = None
    self.minNode = None
  
  def min(self):
    if not self.minNode:
      return None
    return self.minNode.value
  
  def push(self,item):
    if self.minNode and (self.minNode.value < item): #if min node exists and is less than the item pushed/added to the top of stack
      self.minNode = Node(value=self.minNode.value, next=self.minNode) # In this case, it creates a new node (Node(value=self.minNode.value, next=self.minNode)) with the same value as the current minNode and sets it as the new minNode. This preserves the previous minimum value.
    else:
      self.minNode = Node(value=item,next=self.minNode) #In this case, it creates a new node (Node(value=item, next=self.minNode)) with the value of the new item and sets it as the new minNode.
      self.top = Node(value=item,next=self.top)

  def pop(self):
    if not self.top: #stack not empty
      return None
    self.minNode = self.minNode.next
    item = self.top.value
    self.top = self.top.next
    return item
  


customStack = Stack()

# Push some values onto the stack
customStack.push(5)
print("Minimum value in the stack:", customStack.min())  # Output: 5
customStack.push(6)
print("Minimum value in the stack:", customStack.min())  # Output: 5
customStack.push(3)
print("Minimum value in the stack:", customStack.min())  # Output: 3

# Pop a value from the stack
popped_value = customStack.pop()
print("Popped value:", popped_value)  # Output: 3
print("Minimum value in the stack:", customStack.min())  # Output: 5

# Push another value onto the stack
customStack.push(2)
print("Minimum value in the stack:", customStack.min())  # Output: 2
