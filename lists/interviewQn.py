import numpy as np
# Checking uniqueness

myList = [1,2,3,4,5,6,7,8,9,4,8,6,4,3,2]

def checkUnique(list):
  emptyList = []
  for i in list:
    if  i in emptyList:
      print(i)
      return "Not unique"
    else:
      emptyList.append(i)
  return "Is Unique"
    
print(checkUnique(myList))

# rotating matrix

def rotateMatrix(matrix):
  n = len(matrix)
  for layer in range(n//2):
    first,last = layer, n - layer -1
    for i in range(first,last):
      # save top
      top = matrix[layer][i]
      # left to top
      matrix[layer][i] = matrix[-i-1][layer]
      # bottom to left
      matrix[-i-1][layer] = matrix[-layer-1][-i-1]
      # right to bottom
      matrix[-layer-1][-i-1] = matrix [i][-layer-1]
      # top to right
      matrix[i][-layer-1] = top
  return matrix

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
print(rotateMatrix(matrix))

# OR: 

def rotateMatrix(matrix):
  n = len(matrix)
  # transpose the matrix
  for i in range(n):
    for j in range(i,n):
      matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

  #reverse the matrix

  for i in range(n//2):
    for j in range(n):
      matrix[j][i],matrix[j][n-1-i] = matrix[j][n-1-i],matrix[j][i]

  return matrix

print(rotateMatrix(matrix))