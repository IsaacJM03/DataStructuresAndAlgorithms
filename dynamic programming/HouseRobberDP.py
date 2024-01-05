# house robber problem where we must rob the maximum amount of money from houses but we cannot rob adjacent houses
# general formula; houseRobber(houses, currentIndex) = houseRobber(houses, currentIndex + 1) + houseRobber(houses, currentIndex + 2) 



def houseRobberTD(houses, currentIndex,tempDict):
  if currentIndex >= len(houses):
    return 0
  else:
    if currentIndex not in tempDict:
      stealFirstHouse = houses[currentIndex] + houseRobberTD(houses,currentIndex + 2,tempDict) 
      skipFirstHouse = houseRobberTD(houses,currentIndex + 1,tempDict) # we skip the first house because we can't rob adjacent houses
      tempDict[currentIndex] = max(stealFirstHouse, skipFirstHouse)
    return tempDict[currentIndex]
  
houses = [6,7,10,30,8,2,4]
print(houseRobberTD(houses,0,{}))


def houseRobberBU(houses,currentIndex):
  tempArray = [0]*(len(houses)+2)
  for i in range(len(houses)-1,-1,-1):
    tempArray[i] = max(tempArray[i+1], houses[i] + tempArray[i+2])
  return tempArray[0]

print(houseRobberBU(houses,0))