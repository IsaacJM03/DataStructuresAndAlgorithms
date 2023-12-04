# Tried out using Inheritance, tutorial used Normal stuff

''' 
Conditions summary
LL Condition
     z                                      y
    / \                                   /    \
   y   D      Right Rotate (z)          x      z
  / \          - - - - - - - - ->      /  \   / \
 x   C                               A    B C   D
/ \
A   B

RR Condition
  x                                      y
 / \                                   /    \
A   y      Left Rotate (x)            x      z
   / \    - - - - - - - - ->         / \    / \
  B   z                             A   B  C   D
     / \
    C   D

LR Condition

     z                                      z                                   x
    / \                                   /   \                                /    \
   y   D      Left Rotate (y)           x    D       Right Rotate (z)      y      z
  / \          - - - - - - - - ->      /  \        - - - - - - - - ->     / \    / \
 x   C                               y    C                             A   B  C   D
/ \                                 / \
A   B                               A   B

RL Condition

  x                                      x                                   z
 / \                                   /   \                                /    \
A   z      Right Rotate (z)           A    z      Left Rotate (x)        x      y
   / \    - - - - - - - - ->               / \   - - - - - - - - ->      / \    / \
  B   y                                 B   y                        A   B  C   D
     / \                                   / \
    C   D                                 C   D

'''
import binarySearchTree as BST

class AVLNode(BST.BSTNode):
  def __init__(self,data):
    self.data = data
    self.leftChild = None
    self.rightChild = None
    self.height = 1

def getHeight(rootNode):
  if not rootNode: 
    return 0
  return rootNode.height

'''
before rotation here:

    disbalanceNode
    /           \
   A             newRoot
    \           /
     B        C

after rotation here:

       newRoot
      /        \
disbalanceNode  C
  /              \
 A                B

'''
def rightRotate(disbalanceNode):
  # Save the left child of the disbalanced node as the new root
  newRoot = disbalanceNode.leftChild

  # Make the right child of the left child of the disbalanced node the new left child of the disbalanced node
  disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild

  newRoot.rightChild = disbalanceNode    # Make the disbalanced node the right child of the new root

  disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChild))    # Update the height of the disbalanced node based on the heights of its left and right subtrees
 
  newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild)) # Update the height of the new root based on the heights of its left and right subtrees

  return newRoot

'''
before rotation here:

 disbalanceNode
 /           \
A           newRoot
 \         /
  B      C

  
after rotation:

  newRoot
  /    \
 C      disbalanceNode
       /
      A
       \
        B

'''
def leftRotate(disbalanceNode):
  newRoot = disbalanceNode.rightChild     # Save the right child of the disbalanced node as the new root

  disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild  # Make the left child of the right child of the disbalanced node the new right child of the disbalanced node

  newRoot.leftChild = disbalanceNode     # Make the disbalanced node the left child of the new root

  # we add 1 since we consider the parent node **
  disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChild))    # Update the height of the disbalanced node based on the heights of its left and right subtrees

  newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))     # Update the height of the new root based on the heights of its left and right subtrees

  return newRoot

# Function to get the balance factor of a node
def getBalance(rootNode):
  if not rootNode:
    return 0
  # Calculate the balance factor as the difference between the heights of left and right subtrees
  return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, nodeValue):
    if not rootNode:    # If the tree is empty, create a new node with the given value
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:     # If the value is less than the current node's value, insert into the left subtree
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:    # If the value is greater than the current node's value, insert into the right subtree
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    # Update the height of the current node
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))

    # Get the balance factor of the current node
    balance = getBalance(rootNode)

    # Perform rotations to maintain AVL balance if necessary
    # left left condition hence right rotation
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        # Left-Right (LR) Condition: Perform left rotation on left child and then right rotation on the original node
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        # Right-Left (RL) Condition: Perform right rotation on right child and then left rotation on the original node
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    
    # Return the current node
    return rootNode

# Function to find the node with the minimum value in a BST

def getMinValueNode(rootNode):
  if rootNode is None or rootNode.leftChild is None:
    return rootNode
  return getMinValueNode(rootNode.leftChild)


def deleteNode(rootNode,nodeValue):
  #  if the tree is empty
  if not rootNode:
     return rootNode
  
  #  if the value is less than the current node's value,delete from left subtree
  elif nodeValue < rootNode.data:
     rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)

  # if value greater than current node, delete from right subtree
  elif nodeValue > rootNode.data:
     rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)

  # if value found, perform deletion
  else:
    #  if node has one child or no child
    if rootNode.leftChild is None:
       temp = rootNode.rightChild
       rootNode= None
       return temp
    elif rootNode.rightChild is None:
       temp = rootNode.leftChild
       rootNode= None
       return temp
    
    # if the node has 3 children, get the smallest in the right subtree / in order successor
    temp = getMinValueNode(rootNode.rightChild)
    rootNode.data = temp.data
    rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data)

  # update height of current node
  rootNode.height = 1 + max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))

  # get the balance factor of the current node
  balance = getBalance(rootNode)

  if balance > 1 and getBalance(rootNode.leftChild) >= 0: # LL condition
     return rightRotate(rootNode)
  if balance < -1 and getBalance(rootNode.rightChild) <= 0: # RR condition
     return leftRotate(rootNode)
  if balance > 1 and getBalance(rootNode.leftChild) < 0: # LR condition
     rootNode.leftChild = leftRotate(rootNode.leftChild)
     return rightRotate(rootNode)
  if balance < -1 and getBalance(rootNode.rightChild) > 0: # RL condition
     rootNode.rightChild = rightRotate(rootNode.rightChild)
     return leftRotate(rootNode)
  

  return rootNode


newAVL = AVLNode(50)
# print(newAVL.height)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
BST.levelOrderTraversal(newAVL)
print('--------------------')
deleteNode(newAVL,15)
BST.levelOrderTraversal(newAVL)