# Find the first common ancestor of two nodes in a tree, starting from down going up

def findNodeInTree(target,rootNode):
  if not rootNode:
    return False
  if target == rootNode:
    return True
  else:
    return (findNodeInTree(target,rootNode.leftChild) or findNodeInTree(target,rootNode.rightChild))
  
def findFirstCommonAncestor(n1,n2,root):
  n1Left = findNodeInTree(n1,root.leftChild)
  n2Left = findNodeInTree(n2,root.leftChild)

  if n1Left ^ n2Left: # either true or false but not both!
    return root
  else:
    if n1Left:
      return findFirstCommonAncestor(n1,n2,root.leftChild)
    else:
      return findFirstCommonAncestor(n1,n2,root.rightChild)
  
class Node:
  def __init__(self,value,leftChild = None,rightChild = None) -> None:
    self.value = value
    self.leftChild = leftChild
    self.rightChild = rightChild

node54 = Node(54)
node88 = Node(88,node54)
node35 = Node(35)
node22 = Node(22,node35,node88)
node33 = Node(33)
node90 = Node(90,None,node33)
node95 = Node(95)
node99 = Node(99,node90,node95)
node44 = Node(44,node22,node99)
node77 = Node(77)

rootNode = Node(55,node44,node77)

commonAncestor = findFirstCommonAncestor(node54,node95,rootNode)
print(commonAncestor.value)