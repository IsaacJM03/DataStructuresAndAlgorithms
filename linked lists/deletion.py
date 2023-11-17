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

    # delete node from singly linked list
    def deleteNode(self,location):
      if self.head is None:
          print("The Singly Linked List does not exist")
      else:
         if location == 0:
            if self.head == self.tail:
               self.head = None
               self.tail = None
            else:
               self.head = self.head.next
         elif location == -1:
            if self.head == self.tail:
               self.head = None
               self.tail = None
            else:
               node = self.head
               while node is not None:
                  if node.next == self.tail:
                     break
                  node = node.next
               node.next = None
               self.tail = node 
         else:
            tempNode = self.head
            index = 0
            while index < location -1:
               tempNode = tempNode.next
               index+=1
            nextNode = tempNode.next
            tempNode.next = nextNode.next

      # Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None

    
singlyLinkedList = SLinkedList()

singlyLinkedList.insertSLL(0,0)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(20,2)
singlyLinkedList.insertSLL(21,3)
singlyLinkedList.insertSLL(23,4)
singlyLinkedList.insertSLL(1,-1)

print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteNode(1)
singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])

'''
Further explanation:

Certainly, let's go through the `deleteNode` method line by line with visualizations:

```python
# delete node from singly linked list
def deleteNode(self, location):
    if self.head is None:
        print("The Singly Linked List does not exist")
    else:
        # Deleting at the Beginning (location == 0)
        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

        # Deleting at the End (location == -1)
        elif location == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = None
                self.tail = node

        # Deleting in the Middle (location other than 0 or -1)
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next
```

Let's visualize the changes at each step:

1. **Checking if the List Exists:**
   ```python
   if self.head is None:
       print("The Singly Linked List does not exist")
   ```
   - This check ensures that the linked list exists. If it doesn't, a message is printed.

   **Visualization (Empty List):**
   ```
   The Singly Linked List does not exist
   ```

2. **Deleting at the Beginning (`location == 0`):**
   ```python
   elif location == 0:
       if self.head == self.tail:
           self.head = None
           self.tail = None
       else:
           self.head = self.head.next
   ```
   - If the location is 0, it checks if there's only one node. If so, it removes that node. Otherwise, it updates the `head` to the next node.

   **Visualization (After Deletion at Beginning):**
   ```
   LinkedList: ... -> newHead -> ...
   ```

3. **Deleting at the End (`location == -1`):**
   ```python
   elif location == -1:
       if self.head == self.tail:
           self.head = None
           self.tail = None
       else:
           node = self.head
           while node is not None:
               if node.next == self.tail:
                   break
               node = node.next
           node.next = None
           self.tail = node
   ```
   - If the location is -1, it checks if there's only one node. If so, it removes that node. Otherwise, it traverses the list to find the node just before the tail and updates the `tail`.

   **Visualization (After Deletion at End):**
   ```
   LinkedList: ... -> newTail -> None
   ```

4. **Deleting in the Middle (`location` other than 0 or -1):**
   ```python
   else:
       tempNode = self.head
       index = 0
       while index < location - 1:
           tempNode = tempNode.next
           index += 1
       nextNode = tempNode.next
       tempNode.next = nextNode.next
   ```
   - If the location is neither 0 nor -1, it traverses the list to the node just before the desired index. It then updates the `next` reference to skip the node at the desired index.

   **Visualization (After Deletion in the Middle):**
   ```
   LinkedList: ... -> tempNode -> ... -> nextNode.next -> ...
   ```

This process ensures proper deletion of nodes at different locations in the linked list, maintaining the structure of the list.
'''