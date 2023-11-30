import QueuewithLinkedList as queue

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

  
newBinaryTree = TreeNode("Drinks")
left = TreeNode("Hot")
right = TreeNode("Cold")

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")


newBinaryTree.leftChild = left
newBinaryTree.rightChild = right

left.leftChild = tea
left.rightChild = coffee


# pre order traversal --> root, left, right
def preOrderTraversal(rootNode):
  if not rootNode:
    return
  print(rootNode.data)
  preOrderTraversal(rootNode.leftChild)
  preOrderTraversal(rootNode.rightChild)

# preOrderTraversal(newBinaryTree)

# in order traversal --> root, left, right
def inOrderTraversal(rootNode):
  if not rootNode:
    return 
  inOrderTraversal(rootNode.leftChild)
  print(rootNode.data)
  inOrderTraversal(rootNode.rightChild)

# inOrderTraversal(newBinaryTree)

# post order traversal --> left, right, root
def postOrderTraversal(rootNode):
  if not rootNode:
    return
  postOrderTraversal(rootNode.leftChild)
  postOrderTraversal(rootNode.rightChild)
  print(rootNode.data)

# postOrderTraversal(newBinaryTree)

# level order traversal
def levelOrderTraversal(rootNode):  
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()  # Create an empty queue
        customQueue.enqueue(rootNode)  # Enqueue the root node

        while not(customQueue.isEmpty()):  # Continue until the queue is empty
            root = customQueue.dequeue()  # Dequeue a node from the front of the queue
            print(root.value.data)  # Print the data of the dequeued node

            # Enqueue the left child if it exists
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            # Enqueue the right child if it exists
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


# levelOrderTraversal(newBinaryTree)

# searching binary tree
def searchBinaryTree(rootNode,nodeValue):
  if not rootNode:
      return "The Binary Tree does not exist"
  else:
      customQueue = queue.Queue()
      customQueue.enqueue(rootNode)
      while not(customQueue.isEmpty()):
          root = customQueue.dequeue()
          if root.value.data == nodeValue:
              return "Success"
          if (root.value.leftChild is not None):
              customQueue.enqueue(root.value.leftChild)
          
          if (root.value.rightChild is not None):
              customQueue.enqueue(root.value.rightChild)
      return "Not found"
  
def insertChild(rootNode,newNode):
  if not rootNode:
      return "The Binary Tree does not exist"
  else:
      customQueue = queue.Queue()
      customQueue.enqueue(rootNode)
      while not(customQueue.isEmpty()):
          root = customQueue.dequeue()
          if root.value.leftChild is not None:
             customQueue.enqueue(root.value.leftChild)
          else:
             root.value.leftChild = newNode
             return "Successfully Inserted {}".format(newNode)
          if root.value.rightChild is not None:
             customQueue.enqueue(root.value.rightChild)
          else:
             root.value.rightChild = newNode
             return "Successfully Inserted {}".format(newNode)

def getDeepestNode(rootNode):
    if not rootNode:
      return
    else:
      customQueue = queue.Queue()
      customQueue.enqueue(rootNode)
      while not(customQueue.isEmpty()):
          root = customQueue.dequeue() #temporary node for us to store the deepest node
          if root.value.leftChild is not None:
             customQueue.enqueue(root.value.leftChild)
          if root.value.rightChild is not None:
             customQueue.enqueue(root.value.rightChild)
      deepestNode = root.value
      return deepestNode
   
def deleteDeepestNode(rootNode,dNode):
   if not rootNode:
      return
   else:
      customQueue = queue.Queue()
      customQueue.enqueue(rootNode)
      while not(customQueue.isEmpty()):
         root = customQueue.dequeue()
         if root.value is dNode:
            root.value = None
            return 
         if root.value.rightChild:
            if root.value.rightChild is dNode:
               root.value.rightChild = None
               return
            else:
               customQueue.enqueue(root.value.rightChild)
         if root.value.leftChild:
            if root.value.leftChild is dNode:
               root.value.leftChild = None
               return
            else:
               customQueue.enqueue(root.value.leftChild)
def deleteNode(rootNode,node):
   if not rootNode:
      return "The Binary Tree does not exist"
   else:
      customQueue = queue.Queue()
      customQueue.enqueue(rootNode)
      while not(customQueue.isEmpty()):
         root = customQueue.dequeue()
         if root.value.data == node:
            dNode = getDeepestNode(rootNode) #deepest node
            root.value.data = dNode.data #copy the data from old deepest to the desired node
            deleteDeepestNode(rootNode,dNode) # delete the deepest node, since it is replaced by the desired node
            return "Successfully Deleted"
         if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
         if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)
      return "Failed to Delete"

def deleteBinaryTree(rootNode):
  rootNode.data = None
  rootNode.leftChild = None
  rootNode.rightChild = None
  return "Successfully Deleted"


cola = TreeNode("Cola")
water = TreeNode("Water")

insertChild(newBinaryTree,cola)
insertChild(newBinaryTree,water)
levelOrderTraversal(newBinaryTree)
print('--------------------------')
testNode = getDeepestNode(newBinaryTree)
deleteDeepestNode(newBinaryTree,testNode)
deleteNode(newBinaryTree,'Hot')
levelOrderTraversal(newBinaryTree)
print('--------------------------')
deleteBinaryTree(newBinaryTree)
levelOrderTraversal(newBinaryTree)