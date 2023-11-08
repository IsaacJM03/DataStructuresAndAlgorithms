from array import * 

arr1 = array('i',[1,2,3,4,5])

def searchArray(array,value):
  for i in array:
    if i == value:
      return "Value found at index {}".format(array.index(value))
  return "Value not found"

print(searchArray(arr1,9))