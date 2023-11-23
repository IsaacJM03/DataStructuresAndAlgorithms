from LinkedList import LinkedList

def nthToLast(ll,n):
  # setting pointers to help us keep track of where we are and where we want to be i.e. distance from last

  pointer1 = ll.head
  pointer2 = ll.head

  for i in range(n):
    if pointer2 is None:
      return None
    pointer2 = pointer2.next #move to the next in the list
  while pointer2:
    pointer1 = pointer1.next
    pointer2 = pointer2.next
  return pointer1 # index/value of what we're looking for 

customLL = LinkedList()
customLL.generate(10,0,50)
print(customLL)
print(nthToLast(customLL,8))
