myTuple = ('a','bro','c',4,'e','f')

# searching tuple

def searchTuple(tuple,value):
  for i in tuple:
    if i == value:
      return "Value found at index {}".format(tuple.index(value))
  return "Value not found"

print(searchTuple(myTuple,4))

# list to tuple

print(tuple(['hello','bros']))

# nesting both lists and tuples
listTuple = [(1,2,3),(4,5,6),(7,8,9)]
tupleList = ([1,2,3],[4,5,6],[7,8,9])

print(listTuple,"\n",tupleList)