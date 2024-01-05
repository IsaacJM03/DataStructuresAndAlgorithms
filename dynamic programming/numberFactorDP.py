# number factor problem which checks the number of ways 1,3 and 4 can be summed to get a given number n
# general formula ; numberFactor(n) = numberFactor(n-1) + numberFactor(n-3) + numberFactor(n-4)

def numberFactorTD(n,dp): # dp stores the results
  if n in (0,1,2):
    return 1
  elif n == 3:
    return 2
  elif n in dp:
    return dp[n]
  else:
    subProblem1 = numberFactorTD(n-1,dp)
    subProblem2 = numberFactorTD(n-3,dp)
    subProblem3 = numberFactorTD(n-4,dp)
    dp[n] = sum([subProblem1,subProblem2,subProblem3])
    return dp[n]
    # return subProblem1 + subProblem2 + subProblem3

print(numberFactorTD(10,{}))


def numberFactorBU(n):
  tb = [1,1,1,2]
  for i in range(4,n+1):
    tb.append(tb[i-1] + tb[i-3] + tb[i-4])
  return tb[n]

print(numberFactorBU(10))