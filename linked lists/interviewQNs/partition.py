# sorting around a value x but without necessarily sorting either side in ascending or descending

from LinkedList import LinkedList

def partition(ll,x):
  currentNode = ll.head
  ll.tail = ll.head
  while currentNode:
    nextNode = currentNode.next
    currentNode.next = None # disconnecting it from list to prepare it to move
    if currentNode.value < x:
      currentNode.next = ll.head # moving it to the beginning
      ll.head = currentNode
    else:
      ll.tail.next = currentNode #moving it to the end
      ll.tail = currentNode
    currentNode = nextNode #continuing the loop
  
  if ll.tail.next is not None:
    ll.tail.next = None # the last node was placed at the end of the linked list. In this case, it disconnects the last node from any subsequent nodes

customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
partition(customLL, 30)
print(customLL)