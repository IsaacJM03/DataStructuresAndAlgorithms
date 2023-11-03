import math 

def power(base,exponent):
  assert exponent>=0 and int(exponent)==exponent, "exponent must be a positive integer only"
  if exponent==0:
    return 1
  elif exponent==1:
    return base
  else:
    return math.ceil(base*power(base,exponent-1))
  
print(power(3.6,2)) # base can be decimal, output can't