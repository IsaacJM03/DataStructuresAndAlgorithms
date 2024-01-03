# maximum value must be in knapsack

class Item:
  def __init__(self,weight,value) -> None:
    self.weight = weight
    self.value = value
    self.ratio = value / weight
  
def knapsackMethod(items,capacity):
  items.sort(key=lambda x: x.ratio,reverse = True)
  usedCapacity = 0
  totalValue = 0
  for i in items:
    if usedCapacity + i.weight <= capacity: # we are still filling
      usedCapacity += i.weight # storing the values in knapsack
      totalValue += i.value
    else: # if it is empty
      unusedWeight = capacity - usedCapacity
      value = i.ratio * unusedWeight
      usedCapacity += unusedWeight
      totalValue += value

    if usedCapacity == capacity:
      break
  print("Total value obtained: "+str(totalValue))


item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)
cList = [item1,item2,item3]

knapsackMethod(cList,50)