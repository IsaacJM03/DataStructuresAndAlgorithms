'''
Algorithm:

currentNode = node1
tempSet = {1} -> {1,2} -> ...

while currentNode.next is not None:
  if next node's value is in tempSet:
    delete next node
  otherwise add it to tempSet
'''
from LinkedList import LinkedList

def removeDups(ll):
  if ll.head is None:
    return 
  else:
    currentNode = ll.head
    visited = set([currentNode.value]) # temporary set where will store and compare
    while currentNode.next:
      if currentNode.next.value in visited:
        currentNode.next = currentNode.next.next
      else:
        visited.add(currentNode.next.value)
        currentNode = currentNode.next
    return ll
  
def removeWithoutBuffer(ll):
  if ll.head is None:
    return
  
  currentNode = ll.head
  while currentNode:
    runner = currentNode
    while runner.next:
      if runner.next.value == currentNode.value:
        runner.next = runner.next.next
      else:
        runner = runner.next
    currentNode = currentNode.next
  return ll.head
  
customLL = LinkedList()
customLL.generate(10,0,5)
print(customLL)
removeDups(customLL)
removeWithoutBuffer(customLL)
print(customLL)