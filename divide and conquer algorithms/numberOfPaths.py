# Number of paths to reach the last cell with given cost in 2D array

def numberOfPaths(twoDArray, row, col, cost):
  if cost < 0:
    return 0  # If cost becomes negative, no valid path.
  elif row == 0 and col == 0:
    if twoDArray[0][0] - cost == 0:  # If we are at the top-left cell and the cost matches the value, return 1.
      return 1
    else:
      return 0  # If cost doesn't match the value at the top-left cell, no valid path.
  elif row == 0:
    return numberOfPaths(twoDArray, row, col - 1, cost - twoDArray[row][col])  # Move only left.
  elif col == 0:
    return numberOfPaths(twoDArray, row - 1, col, cost - twoDArray[row][col])  # Move only up.
  else:
    # Move up and move left, count the number of paths for both scenarios.
    operation1 = numberOfPaths(twoDArray, row - 1, col, cost - twoDArray[row][col])
    operation2 = numberOfPaths(twoDArray, row, col - 1, cost - twoDArray[row][col])
    return operation1 + operation2  # Total number of paths is the sum of paths from both operations.

TwoDList = [[4, 7, 1, 6],
            [5, 7, 3, 9],
            [3, 2, 1, 2],
            [7, 1, 6, 3]
           ]

print(numberOfPaths(TwoDList, 3, 3, 28))

'''
Visualization: # top part and first two sub tress are correct, the rest arent

                           (3,3,28)
                          /        \
                (2,3,26)           (3,2,22)
                /    \              /     \
         (1,3,15)  (2,2,20)     (2,2,21)   (3,1,21)
         /    \     /    \     /    \      /    \
    (0,3,19) (1,2,17)(1,2,20) (1,2,22)(2,1,15)(2,1,19)
    /   \     /  \   /   \    /  \   /  \    /   \
(0,2,15)(1,1,13)(1,1,17)(1,1,20)(1,1,22)(2,0,12)(2,0,15)
   |       |       |       |       |        |      |
(0,1,10)(0,1,13)(0,1,15)(0,1,17)(0,1,20) (1,0,10) (1,0,13)
   |       |       |       |       |        |      |
(0,0,6)  (0,0,10) (0,0,13) (0,0,15) (0,0,17) (0,0,10) 

(0,0,6) <- Path Found


'''