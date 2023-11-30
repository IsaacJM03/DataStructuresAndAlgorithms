# lastUsedIndex is used to keep track of the last index in the customList where a node has been inserted. It is incremented every time a new node is added to the binary tree. This variable helps in determining the position to insert a new node in the next available slot in the customList.

class BinaryTree:
  def __init__(self,size) -> None:
    self.customList = size * [None]
    self.lastUsedIndex = 0 # keeps track of the last index in the customList
    self.maxSize = size

  def insertNode(self,value):
    if self.lastUsedIndex + 1 == self.maxSize:
      return "The Binary Tree is full"
    self.customList[self.lastUsedIndex+1] = value # inserting the new value at the end
    self.lastUsedIndex += 1 # adding another index at the end
    return "Successfully inserted"
  
  def searchNode(self,nodeValue):
    for i in range(len(self.customList)):
      if self.customList[i] == nodeValue:
        return "Success"
    return "Not found"
  
  # root -> left -> right
  def preOrderTraversal(self,index):
    if index > self.lastUsedIndex:
      return
    print(self.customList[index]) #root
    self.preOrderTraversal(index*2) # left
    self.preOrderTraversal(index*2+1) # right

  # left -> root -> right
  def inOrderTraversal(self,index):
    if index > self.lastUsedIndex:
      return
    self.inOrderTraversal(index*2) # left
    print(self.customList[index]) #root
    self.inOrderTraversal(index*2+1) # right
  
  # left -> right -> root
  def postOrderTraversal(self,index):
    if index > self.lastUsedIndex:
      return
    self.postOrderTraversal(index*2) # left
    self.postOrderTraversal(index*2+1) # right
    print(self.customList[index])

  # level by level. left -> right
  def levelOrderTraversal(self,index):
    for i in range(index, self.lastUsedIndex+1): # looping till the last index
      print(self.customList[i])

  def deleteNode(self,value):
    if self.lastUsedIndex == 0:
      return "There is no node available to delete"
    for i in range(1,self.lastUsedIndex+1): # looping till the last index
      if self.customList[i] == value: # finding the value
        self.customList[i] = self.customList[self.lastUsedIndex] # replacing the deepest node with the value
        self.customList[self.lastUsedIndex] = None # deleting the deepest node
        self.lastUsedIndex -= 1 # decrementing the last used index for each iteration
        return "Successfully deleted"
  
  def deleteBinaryTree(self):
    self.customList = None
    return "Successfully deleted"


newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")

# print(newBT.deleteBT())

newBT.postOrderTraversal(1)
