# Recursion
from os import preadv


class Node:
  def __init__(self,value =0,next =None):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

# normal recursion
  def reverseLinkedListRecursive(self,head):
      if not head or not head.next:
        return head
      
      reversedTail = self.reverseLinkedListRecursive(head.next)
      head.next.next = head
      head.next = None

      return reversedTail
  
  # Tail recursion
  def tailReverseLinkedListRecursive(self,currentNode,prevNode):
     if currentNode.next is None: # for the last node, make it the head
        self.head = currentNode
        currentNode.next = prevNode
        return
     nextNode = currentNode.next
     currentNode.next = prevNode
     self.tailReverseLinkedListRecursive(nextNode,currentNode)

# Iteration

  def iterativeReverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


  def reverse(self):
        if self.head is None:
            return
        self.tailReverseLinkedListRecursive(self.head, None)

  def __str__(self):
          linkedListStr = ""
          temp = self.head
          while temp:
              linkedListStr = (linkedListStr +
                              str(temp.value) + " ")
              temp = temp.next
          return linkedListStr
  
  # Pushes new value to the head of the list
  def push(self, value):
      temp = Node(value)
      temp.next = self.head
      self.head = temp

 
linkedList = LinkedList()
linkedList.push(20)
linkedList.push(4)
linkedList.push(15)
linkedList.push(85)

print("Given linked list")
print(linkedList)
 
linkedList.head = linkedList.reverseLinkedListRecursive(linkedList.head)

linkedList.tailReverseLinkedListRecursive(linkedList.head, None)

linkedList.iterativeReverse()
# linkedList.reverse()
print("Reversed linked list")
print(linkedList)


