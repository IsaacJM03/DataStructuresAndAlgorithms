import QueuewithLinkedList as queue

class BSTNode:
  def __init__(self,data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

# if bigger, insert right. if smaller, insert left
def insertNode(rootNode,nodeValue):  #----> O(log n) because input size keeps reducing since we consider either the left or the right
  if rootNode.data == None:
    rootNode.data = nodeValue # create new node as the root
  elif nodeValue <= rootNode.data: # insert left,if value is smaller than root/parent
    if rootNode.leftChild is None:
      rootNode.leftChild = BSTNode(nodeValue) 
    else:
      insertNode(rootNode.leftChild,nodeValue) # recursive call in case we have to keep moving down
  else:
    if rootNode.rightChild is None:
      rootNode.rightChild = BSTNode(nodeValue)
    else: # if value is bigger than root/parent
      insertNode(rootNode.rightChild,nodeValue) # keep on moving down, to the right if value is bigger
  return "Successfully Inserted"

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
  if not rootNode:
    return
  else:
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not (customQueue.isEmpty()):
      root = customQueue.dequeue()
      print(root.value.data)
      if root.value.leftChild is not None:
        customQueue.enqueue(root.value.leftChild)
      if root.value.rightChild is not None:
        customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue) # If not found on the left, recursively call searchNode on the left child until the value is found.
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue) # If not found on the right, recursively call searchNode on the right child until the value is found.

#  getting the minimum value in a subtree
def minNode(node):
  current = node # storing the value 
  while (current.leftChild is not None):
    current = current.leftChild # keep moving down until we reach the last 
  return current

def deleteNode(rootNode,nodeValue):
  if rootNode is None:
    return rootNode #base case for recursion
  if nodeValue < rootNode.data:  # smaller than parent
    rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue) # recursive call to delete going left
  elif nodeValue > rootNode.data: # bigger than parent
    rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue) # recursive call to delete going right
  else: # Handling the case when the target value is equal to the current node's data
    if rootNode.leftChild is None:
      temp = rootNode.rightChild
      rootNode = None
      return temp # replacing the parent node with it's right child
    
    if rootNode.rightChild is None:
      temp = rootNode.leftChild
      rootNode = None
      return temp # replacing the parent node with it's left child
    
    temp = minNode(rootNode.rightChild) #if 2 children, check for smallest
    rootNode.data = temp.data # replace with smallest
    rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data) # recusrively delete the smallest node from the right
    return rootNode #return modified root/ new parent
  
def deleteBST(rootNode):
  rootNode.data = None
  rootNode.leftChild = None
  rootNode.rightChild = None
  return "Successfully Deleted"


# newBST = BSTNode(None)
# insertNode(newBST, 70)
# insertNode(newBST,50)
# insertNode(newBST,90)
# insertNode(newBST, 30)
# insertNode(newBST,60)
# insertNode(newBST,80)
# insertNode(newBST,100)
# insertNode(newBST,20)

# print(newBST.leftChild.data)
# print('-----------------')
# print(deleteBST(newBST))
# print('-----------------')
# levelOrderTraversal(newBST)