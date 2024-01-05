# store values in a dictionary so that we dont need to recalculate already-calculated values at each step
# top-down approach

def fibMemo(n,memo):
  if n == 1:
    return 0
  if n == 2:
    return 1
  if not n in memo:
    memo[n] = fibMemo(n-1,memo) + fibMemo(n-2,memo)
  return memo[n]

myDict = {}
print(fibMemo(9,myDict))