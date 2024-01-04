# house robber problem where we must rob the maximum amount of money from houses but we cannot rob adjacent houses
# general formula; houseRobber(houses, currentIndex) = houseRobber(houses, currentIndex + 1) + houseRobber(houses, currentIndex + 2) 



def houseRobber(houses, currentIndex):
  if currentIndex >= len(houses):
    return 0
  else:
    stealFirstHouse = houses[currentIndex] + houseRobber(houses,currentIndex + 2) 
    skipFirstHouse = houseRobber(houses,currentIndex + 1) # we skip the first house because we can't rob adjacent houses
    return max(stealFirstHouse, skipFirstHouse)
  
houses = [6,7,10,30,8,2,4]
print(houseRobber(houses,0))