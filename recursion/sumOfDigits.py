def sumOfDigits(n):
  assert n>=0 and int(n)==n, "n must be a positive integer only"
  if n==0:
    return 0
  else:
    return (n%10) + sumOfDigits(n//10)
  
print(sumOfDigits(1234))