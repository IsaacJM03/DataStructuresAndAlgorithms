'''
Here's a simple explanation and visualization:

    You have a knapsack with a maximum weight capacity, let's say W.
    You are given a set of items, each with its own weight (wi) and value (vi).
    The task is to select a combination of items to maximize the total value, but the sum of their weights cannot exceed the knapsack's capacity.
'''

class Item:
  def __init__(self,profit,weight) -> None:
    self.profit = profit
    self.weight = weight

def zeroOneKnapsack(items,capacity,currentIndex):
  if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items): # if we reach the end of the array
    return 0
  elif items[currentIndex].weight <= capacity:
    profit1 = items[currentIndex].profit + zeroOneKnapsack(items,capacity-items[currentIndex].weight,currentIndex+1)
    profit2 = zeroOneKnapsack(items,capacity,currentIndex+1)
    return max(profit1,profit2)
  else:
    return 0
  
mango = Item(31,3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]

print(zeroOneKnapsack(items, 7, 0))