#  coin change problem which is a problem of finding the minimum number of coins that make up a given value when added together

def coinChange(totalNumber, coins):
  N = totalNumber
  coins.sort() 
  index = len(coins)-1
  coinNumber = []
  while True:
    coinValue = coins[index]
    if N >= coinValue: # for checking if the value is greater than the coin
      print(coinValue)
      coinNumber.append(coinValue)
      N = N - coinValue # subtracting the coin value from the total number
    if N < coinValue: # for checking if the value is less than the coin
      index -= 1 # decrementing the index

    if N == 0: 
      print(f"Total number of coins: {len(coinNumber)}")
      break
      

coins = [1,2,5,20,50,100]
coinChange(1000,coins)