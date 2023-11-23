from LinkedList import LinkedList, Node

def intersection(llA, llB):
    if llA.tail is not llB.tail: #checking if they intersect
        return False
    
    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next # Moving the longer linked list's pointer to a position where both linked lists have the same number of nodes remaining.

    
    while shorterNode is not longerNode: #Move both pointers in tandem until they meet at the intersection point which is the longer node
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    
    return longerNode


# Helper addition method, adding the same node for tests
def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode

llA = LinkedList()
llA.generate(3,0, 10)

llB = LinkedList()
llB.generate(4,0, 10)

addSameNode(llA, llB, 1)
addSameNode(llA, llB, 4)

print(llA)
print(llB)

print(intersection(llA, llB))