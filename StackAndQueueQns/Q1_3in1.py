class MultiStack:
    def __init__(self, stacksize):
        # Initializes the MultiStack class with the number of stacks, a custom list to store values,
        # sizes of each stack, and the specified stack size.
        self.numberstacks = 3
        self.custList = [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize
    
    def isFull(self, stacknum):
        # Checks if a specific stack is full.
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False
    
    def isEmpty(self, stacknum):
        # Checks if a specific stack is empty.
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False
    
    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize   # Calculate the base index of the stack by multiplying the stack number with the stack size.
        
        return offset + self.sizes[stacknum] - 1
        # Add the base index to the number of elements currently in the stack (sizes[stacknum]),
        # and subtract 1 to get the index of the top element.

    
    def push(self, item, stacknum):
        # Adds an item to a specific stack.
        if self.isFull(stacknum):
            return "The stack is full"
        else:
            self.sizes[stacknum] += 1
            self.custList[self.indexOfTop(stacknum)] = item
    
    def pop(self, stacknum):
        # Removes and returns the top item from a specific stack.
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value
    
    def peek(self, stacknum):
        # Returns the value of the top item in a specific stack without removing it.
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            return value


customStack = MultiStack(6)
# Creates an instance of the MultiStack with a specified stack size of 6.

print(customStack.isFull(0))
# Checks if the first stack is full (prints False).

print(customStack.isEmpty(1))
# Checks if the second stack is empty (prints True).

customStack.push(1, 0)
# Pushes the value 1 onto the first stack.

customStack.push(2, 0)
# Pushes the value 2 onto the first stack.

customStack.push(3, 2)
# Pushes the value 3 onto the third stack.

print(customStack.pop(0))
# Pops a value from the first stack (prints 2).
