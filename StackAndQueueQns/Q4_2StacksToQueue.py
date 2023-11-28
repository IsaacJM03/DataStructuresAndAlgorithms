class Stack():
  def __init__(self) -> None:
    self.list = []

  def __len__(self):
    return len(self.list)
  
  
  def push(self,item):
    self.list.append(item)

  def pop(self):
    if len(self.list) == 0:
      return None
    return self.list.pop()
  

class QueueViaStack():
  def __init__(self) -> None:
    self.inStack = Stack() # for enqueuing
    self.outStack = Stack() # for dequeuing

# When you call enqueue(item), the item is added to the inStack.
  def enqueue(self,item):
    self.inStack.push(item)

# When you call dequeue(), the code checks if the outStack is empty. If it is, it transfers elements from the inStack to the outStack.
# The front/first item is then dequeued from the outStack.
  def dequeue(self):
    while len(self.inStack):
      self.outStack.push(self.inStack.pop())
    result = self.outStack.pop()
    while len(self.outStack):
      self.inStack.push(self.outStack.pop())
    return result
  
customQueue = QueueViaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
customQueue.enqueue(4)
print(customQueue.dequeue())

