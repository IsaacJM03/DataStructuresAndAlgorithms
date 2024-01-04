# starting from down(destination) to up(source)

def findMinCost(twoDArray,row,col):
  if row == -1 or col == -1: # if we are out of bounds
    return float('inf')
  elif row == 0 and col == 0: # if we are at source
    return twoDArray[0][0]
  else:
    operation1 = findMinCost(twoDArray,row-1,col)
    operation2 = findMinCost(twoDArray,row,col-1)
    return twoDArray[row][col] + min(operation1,operation2)
  

TwoDList = [
  [4,7,8,6,4],
  [6,7,3,9,2],
  [3,8,1,2,4],
  [7,1,7,3,7],
  [2,9,8,9,3]
]

print(findMinCost(TwoDList, 4,4)) # 4,4 because we start from the bottom right corner
