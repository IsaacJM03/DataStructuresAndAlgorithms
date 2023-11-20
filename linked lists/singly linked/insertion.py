class Node:
    def __init__(self, value=None):
        # defining the next reference on each node
        self.value = value
        self.next = None

class SLinkedList:
    # defining the head and tail of list
    def __init__(self):
        self.head = None
        self.tail = None

  # helps us to iterate over the linked list
    def __iter__(self):
      node = self.head
      while node:
        yield node
        node = node.next

    def insertSLL(self,value,location):
      newNode = Node(value)
      # if we're creating the first node
      if self.head is None:
        self.head = newNode
        self.tail = newNode
      else:
        # inserting at beginning
        if location==0:
          newNode.next = self.head
          self.head = newNode
        elif location == -1:
          newNode.next = None
          self.tail.next = newNode
          self.tail = newNode
        else:
          # inserting in the middle
          tempNode = self.head
          index = 0
          # looping till we find required index
          while index < location -1:
            tempNode = tempNode.next
            index+=1
          nextNode = tempNode.next
          tempNode.next = newNode
          newNode.next = nextNode
          if tempNode == self.tail:
            self.tail=newNode

singlyLinkedList = SLinkedList()

singlyLinkedList.insertSLL(0,0)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(1,-1)

print([node.value for node in singlyLinkedList])