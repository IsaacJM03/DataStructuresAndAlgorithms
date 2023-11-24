class Stack:
  def __init__(self):
    self.list = []

  def __str__(self):
    values = reversed(self.list)
    values = [str(x) for x in values]
    return '\n'.join(values)
  
# isEmpty
  def isEmpty(self):
      if self.list == []:
          return True
      else:
          return False
  # push
  def push(self, value):
      self.list.append(value)
      return "The element has been successfully inserted"

  # pop
  def pop(self):
      if self.isEmpty():
          return "There is not any element in the stack"
      else:
          return self.list.pop()
  
  # peek
  def peek(self):
      if self.isEmpty():
          return "There is not any element in the stack"
      else:
          return self.list[len(self.list)-1]
  
  # delete
  def delete(self):
      self.list = None


stack1 = Stack()
stack1.push(1)  
stack1.push(2)  
stack1.push(3)  
stack1.push(4)  
stack1.push(5)  
print(stack1.peek())
print('------------')
print(stack1)