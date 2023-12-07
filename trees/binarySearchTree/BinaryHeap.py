class Heap:
  def __init__(self,size) -> None:
    self.customList = (size + 1) * [None] # we can ignore the index 0 and perform calculations more easily using 1-based indexing. Custom List help stores the elements of the binary heap
    self.heapSize = 0
    self.maxSize = size + 1

def peekHeap(rootNode):
  if not rootNode:
    return
  else:
    return rootNode.customList[1] # first element, not 0 since we start from 1
  
def sizeOfHeap(rootNode):
  if not rootNode:
    return
  else:
    return rootNode.heapSize #maximum size of the heap
  

def levelOrderTraversal(rootNode):
  if not rootNode:
    return
  else:
    for i in range(1,rootNode.heapSize + 1):
      print(rootNode.customList[i])

def heapTreeInsert(rootNode,index,heapType):
  parentIndex = int(index/2) # since original formula for getting child is 2x 
  if index <= 1:
    return
  if heapType.lower() == "min":
    if rootNode.customList[index] < rootNode.customList[parentIndex]: # if required value is less than parent
      temp = rootNode.customList[index]
      rootNode.customList[index] = rootNode.customList[parentIndex] # performs a swap. This swap ensures that the smaller value moves up the heap, maintaining the heap property.
      rootNode.customList[parentIndex] = temp
      heapTreeInsert(rootNode,parentIndex,heapType) # until all obey the heap property
    elif heapType.lower() == "max":
      if rootNode.customList[index] > rootNode.customList[parentIndex]: # if required value is greater than parent
        temp = rootNode.customList[index]
        rootNode.customList[index] = rootNode.customList[parentIndex] # performs a swap. This swap ensures that the larger value moves up the heap, maintaining the heap property.
        rootNode.customList[parentIndex] = temp
        heapTreeInsert(rootNode,parentIndex,heapType) # until all obey the heap property
    
def insertNode(rootNode,nodeValue,heapType):
  if rootNode.heapSize + 1 == rootNode.maxSize:
    return "The Binary Heap is Full"
  rootNode.customList[rootNode.heapSize + 1] = nodeValue # adding it to the very end of the list
  rootNode.heapSize += 1 # increasing the list size
  heapTreeInsert(rootNode,rootNode.heapSize,heapType)
  return "The value has been successfully inserted"

def heapTreeExtract(rootNode,index,heapType):
  # basing of the formula, right = 2x and left = 2x + 1 where x is parent node index
  leftIndex = index * 2
  rightIndex = index * 2 + 1
  swapChild = 0 # used to keep track of the index of the child node that needs to be swapped with the current node

  if rootNode.heapSize < leftIndex: # the current node has no child nodes, so it is a leaf node
    return
  elif rootNode.heapSize == leftIndex: # has exactly one child
    if heapType.lower() == "min": 
      if rootNode.customList[index] > rootNode.customList[leftIndex]: # if child is greater than parent
        temp = rootNode.customList[index] > rootNode.customList[leftIndex]
        rootNode.customList[index] = rootNode.customList[leftIndex]
        rootNode.customList[leftIndex] = temp
      return
    else:
      if rootNode.customList[index] < rootNode.customList[leftIndex]: # if child is less than parent
        temp = rootNode.customList[index] < rootNode.customList[leftIndex]
        rootNode.customList[index] = rootNode.customList[leftIndex]
        rootNode.customList[leftIndex] = temp
      return
  else: # if the current node has 2 child nodes
    if heapType.lower() == "min":
      if rootNode.customList[index] > rootNode.customList[leftIndex]:
        swapChild = leftIndex # if left is smaller, it is the child to be swapped
      else:
        swapChild = rightIndex ## otherwise, the right child is the child to be swapped
      if rootNode.customList[index] > rootNode.customList[swapChild]:
        temp = rootNode.customList[index]
        rootNode.customList[index] = rootNode.customList[swapChild] # performs a swap. This swap ensures that the smaller value moves up the heap, maintaining the heap property.
        rootNode.customList[swapChild] = temp
      else:
        if rootNode.customList[index] > rootNode.customList[rightIndex]:
          swapChild = leftIndex # if the right child is smaller, it is the child to be swapped
        else:
          swapChild = leftIndex # otherwise, the left child is the child to be swapped
        if rootNode.customList[index] < rootNode.customList[swapChild]:
          temp = rootNode.customList[index]
          rootNode.customList[index] = rootNode.customList[swapChild] # performs a swap. This swap ensures that the smaller value moves up the heap, maintaining the heap property.
          rootNode.customList[swapChild] = temp
  heapTreeExtract(rootNode,swapChild,heapType)

def extractNode(rootNode,heapType):
  if rootNode.heapSize == 0:
    return
  rootNode.customList[1] = rootNode.customList[rootNode.heapSize] # moves the last node to the root position.
  rootNode.customList[rootNode.heapSize] = None # remove last node from the heap.
  rootNode.heapSize -= 1 # reduce the heap size to reflect removal of node
  heapTreeExtract(rootNode,1,heapType) # helps adjust the heap
  return rootNode.customList[rootNode.heapSize + 1] # returns extracted node which was previously the root node


def deleteEntireHeap(rootNode):
  rootNode.customList = None


newHeap = Heap(5)
insertNode(newHeap, 4, "min")
insertNode(newHeap, 5, "min")
insertNode(newHeap, 2, "min")
insertNode(newHeap, 1, "min")
deleteEntireHeap(newHeap)
levelOrderTraversal(newHeap)
