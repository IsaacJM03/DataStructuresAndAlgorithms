# stack of plates , go to next stack in case too many

class PlateStack():
  def __init__(self,capacity) -> None:
    self.capacity = capacity
    self.stacks = []

  def __str__(self) -> str:
    return self.stacks
  
  def push(self,item):
    if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity: # if the stacks exist and the last stack is not full 
      self.stacks[-1].append([item]) # add item to the last stack
    else:
      self.stacks.append([item]) # create a new stack with that item as the first

  def pop(self):
    while len(self.stacks) and len(self.stacks[-1]) == 0: # if the last stack is empty
      self.stacks.pop() # remove top element of (pop) that stack
    if len(self.stacks) == 0:
      return None
    else:
      return self.stacks[-1].pop() # return the top element of the last stack
    
  def popAt(self,stackNumber):
    if len(self.stacks[stackNumber]) > 0:
      return self.stacks[stackNumber].pop()
    else:
      return None
    
customStack= PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.popAt(1))