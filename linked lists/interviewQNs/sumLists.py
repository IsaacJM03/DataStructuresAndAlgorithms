from LinkedList import LinkedList

def sumList(llA,llB):
  n1,n2 = llA.head, llB.head
  carry = 0
  ll = LinkedList()

  while n1 or n2:
    result = carry # storing the carried digit here and adding it to the result later
    if n1:
      result += n1.value #adding the value to the result which also includes the carried digit
      n1 = n1.next # go to next in list
    if n2:
      result += n2.value #adding the value to the result which also includes the carried digit
      n2 = n2.next # go to next in list

    ll.add(int(result%10)) # adds the result but without the remainder. say 12, keep 2 and the carry 1 in the next step. we are keeping 2 here.
    carry = result/10 #getting remainder or carry

  return ll

llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)


llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)
print(llA)
print(llB)
print(sumList(llA, llB))