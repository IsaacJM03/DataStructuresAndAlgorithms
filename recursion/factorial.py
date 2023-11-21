def factorial(n):
  assert n>=0 and int(n)==n, "n must be a positive integer only"
  if n in [0,1]:
    return 1
  else:
    return n*factorial(n-1)
  
print(factorial(100))

# tail recursion version
def factorial_tail(n, acc=1):
    assert n >= 0 and int(n) == n, "n must be a positive integer only"
    if n in [0, 1]:
        return acc
    else:
        return factorial_tail(n - 1, n * acc)

print(factorial_tail(5))
