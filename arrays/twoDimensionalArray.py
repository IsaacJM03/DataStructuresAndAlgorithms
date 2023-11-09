import numpy as np

twoDArray = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(twoDArray)
print(" ")

# can use similar implementations to traverse an array
def search2DArray(array,value):
  for i in range(len(array)):
    for j in range(len(array[0])):
      if array[i][j] == value:
        return "The value is at column {}, row {}".format(i,j)
  return "Element not found"

print(search2DArray(twoDArray,9))