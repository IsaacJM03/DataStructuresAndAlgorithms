class Queue:
  def __init__(self,maxSize):
    self.items = maxSize * [None]
    self.maxSize = maxSize
    self.start = -1
    self.top = -1

  def __str__(self) -> str:
    values = [str(x) for x in self.items]
    return ' '.join(values)
  
  def isFull(self):
    if self.top + 1 == self.start:
      return True
    elif self.start == 0 and self.top + 1 == self.maxSize:
      return True
    else:
      return False
    
  def isEmpty(self):
    if self.top == -1: # because it was initialized like so
      return True
    else:
      return False
    
  def enqueue(self,value):
    if self.isFull():
      return "The queue is full"
    else:
      if self.top + 1 == self.maxSize: 
        self.top = 0 #move to beginning so that new element can be inserted(always inserted at top, FIFO!)
      else:
        self.top += 1 #increment top
        if self.start == -1: #if the queue was empty
          self.start = 0 #start from the beginning
        self.items[self.top] = value #Inserts the new element at the updated top index.
        return "The element has been inserted to the end of the Queue"
  
  def dequeue(self):
    if self.isEmpty():
      return "There is no element in the Queue"
    else:
      firstElement = self.items[self.start]
      start = self.start
      if self.start == self.top: #only one element
        self.top = -1
      elif self.start + 1 == self.maxSize: # if start is the last element
        self.start = 0 #start from the beginning
      else:
        self.start += 1
      self.items[start] = None #deletes the element
      return "{} has been dequeued".format(firstElement)
    
  def peek(self):
    if self.isEmpty():
      return "There is no element in the Queue"
    else:
      return self.items[self.start]
    
  def delete(self):
    self.items = self.maxSize * [None]
    self.top = -1 #re-intialize
    self.start = -1 #re-intialize

  
customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.delete()
print(customQueue)

