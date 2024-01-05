'''
Here's a simple explanation and visualization:

    You have a knapsack with a maximum weight capacity, let's say W.
    You are given a set of profits, each with its own weight (wi) and value (vi).
    The task is to select a combination of profits to maximize the total value, but the sum of their weights cannot exceed the knapsack's capacity.
'''

def zeroOneKnapsackBU(profits,weights,capacity):
  if capacity <= 0 or len(profits) == 0 or len(weights) != len(profits):  
    return 0
  numberOfRows = len(profits) + 1
  dp = [[0 for i in range(capacity+2)] for j in range(numberOfRows)] # 2d array for dynamic programming
  for row in range(numberOfRows-2,-1,-1): # looping from last row to first
    for column in range(1,capacity+1):
      profit1 = 0
      profit2 = 0
      if weights[row] <= column:
        profit1 = profits[row] + dp[row+1][column - weights[row]]
      profit2 = dp[row+1][column]
      dp[row][column] = max(profit1,profit2)
  return dp[0][capacity]
  
class Item:
  def __init__(self,profit,weight) -> None:
    self.profit = profit
    self.weight = weight

def zeroOneKnapsackTD(items,capacity,currentIndex,tempDict):
  dictKey = str(currentIndex) + str(capacity)
  if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items): # if we reach the end of the array
    return 0
  elif dictKey in tempDict:
    return tempDict[currentIndex]
  elif items[currentIndex].weight <= capacity:
    profit1 = items[currentIndex].profit + zeroOneKnapsackTD(items,capacity-items[currentIndex].weight,currentIndex+1,tempDict)
    profit2 = zeroOneKnapsackTD(items,capacity,currentIndex+1,tempDict)
    # return max(profit1,profit2)
    tempDict[dictKey] = max(profit1,profit2)
    return tempDict[dictKey]
  else:
    return 0

profits = [31,26,72,17]
weights = [3,1,5,2]
capacity = 7

print(zeroOneKnapsackBU(profits, weights,capacity))



mango = Item(31,3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]
tempDict={}
print(zeroOneKnapsackTD(items, 7,0,tempDict))
