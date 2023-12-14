import math


def linearSearch(array,value):  #----> O(n) -time, O(1) -space
  for i in range(len(array)):
    if array[i] == value:
      return "Value is at index {}".format(i)
      # return "Value is the {}th element".format(i+1)
  return "Value not found"

def binarySearch(array,value):
  start = 0
  end = len(array) - 1
  middle = math.floor((start+end)/2)
  while not(array[middle]==value) and start<=end:
    if value < array[middle]:
      end = middle - 1
    else:
      start = middle + 1
    middle = math.floor((start+end)/2)
  if array[middle] == value:
    return "Value is at index {}".format(middle)
  else:
    return "Value not found"

print(linearSearch([1,2,3,4,35,6,7,8,9,10],10))
print(binarySearch([1,2,3,4,35,6,7,8,9,10],35))