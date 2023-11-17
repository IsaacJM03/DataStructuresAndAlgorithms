class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

singlyLinked = SinglyLinkedList()
node1 = Node(1)
node2 = Node(2)

singlyLinked.head = node1
singlyLinked.head.next = node2
singlyLinked.tail = node2

'''
additional explanation

Certainly! Let's visualize the steps of the `insertSLL` method:

1. **Initialization:**
   - `newNode = Node(value)`: A new node (`newNode`) is created with the given value.

2. **Checking if the List is Empty:**
   ```python
   if self.head is None:
       self.head = newNode
       self.tail = newNode
   ```
   - If the linked list is empty (i.e., `head` is `None`), the new node becomes both the head and the tail of the list.

   **Visualization:**
   ```
   LinkedList: newNode -> None
   ```

3. **Inserting at the Beginning:**
   ```python
   elif location == 0:
       newNode.next = self.head
       self.head = newNode
   ```
   - If the `location` is 0, the new node is inserted at the beginning. Its `next` reference points to the current head, and the head is updated to the new node.

   **Visualization:**
   ```
   LinkedList: newNode -> oldHead -> ...
   ```

4. **Inserting at the End:**
   ```python
   elif location == -1:
       newNode.next = None
       self.tail.next = newNode
       self.tail = newNode
   ```
   - If the `location` is -1, the new node is inserted at the end. Its `next` reference is set to `None`, the current tail's `next` points to the new node, and the tail is updated to the new node.

   **Visualization:**
   ```
   LinkedList: ... -> oldTail -> newNode -> None
   ```

5. **Inserting in the Middle:**
   Certainly! Let's go more in-depth with the visualization for the case where the new node is inserted in the middle of the linked list:

```python
else:
    tempNode = self.head
    index = 0
    while index < location - 1:
        tempNode = tempNode.next
        index += 1
    nextNode = tempNode.next
    tempNode.next = newNode
    newNode.next = nextNode
    if tempNode == self.tail:
        self.tail = newNode
```

Assuming `location` is a valid index within the linked list (not at the beginning or end):

1. **Initialization:**
   ```python
   tempNode = self.head
   index = 0
   ```
   - `tempNode` is initialized to the head of the linked list.
   - `index` is initialized to 0.

   **Visualization:**
   ```
   LinkedList: ... -> tempNode -> ...
   ```

2. **Looping to the Desired Index:**
   ```python
   while index < location - 1:
       tempNode = tempNode.next
       index += 1
   ```
   - The `while` loop iterates until `index` is one less than the desired `location`. It moves `tempNode` to the node just before the desired index.

   **Visualization (Assuming `location = 2`):**
   ```
   LinkedList: ... -> tempNode -> ... -> DesiredNode -> ...
   ```

3. **Saving the Next Node:**
   ```python
   nextNode = tempNode.next
   ```
   - `nextNode` is a reference to the node that comes after `tempNode`.

   **Visualization:**
   ```
   LinkedList: ... -> tempNode -> ... -> DesiredNode -> nextNode -> ...
   ```

4. **Inserting the New Node:**
   ```python
   tempNode.next = newNode
   newNode.next = nextNode
   ```
   - The `next` reference of `tempNode` is updated to point to the new node (`newNode`).
   - The `next` reference of `newNode` is updated to point to the node that was originally after `tempNode`.

   **Visualization (After Insertion):**
   ```
   LinkedList: ... -> tempNode -> ... -> DesiredNode -> newNode -> nextNode -> ...
   ```

5. **Updating the Tail (if needed):**
   ```python
   if tempNode == self.tail:
       self.tail = newNode
   ```
   - If `tempNode` was the current tail of the linked list, the tail is updated to the new node (`newNode`).

   **Visualization (After Tail Update):**
   ```
   LinkedList: ... -> tempNode -> ... -> DesiredNode -> newNode -> nextNode -> ... -> self.tail -> ...
   ```

This process ensures the proper insertion of the new node at the specified location in the middle of the linked list.

In each case, the visualization represents the state of the linked list after the insertion operation. The arrows indicate the `next` references between nodes.
'''