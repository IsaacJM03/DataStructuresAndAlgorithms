# Convert one string to another with minimum number of operations


def findMinOperation(s1,s2,index1,index2):
  if index1 == len(s1): # if we have reached the end of the string
    return len(s2) - index2 # we need to insert the remaining characters
  if index2 == len(s2): # if we have reached the end of the string
    return len(s1) - index1 # we need to insert the remaining characters
  if s1[index1] == s2[index2]: # if we have reached the same character
    return findMinOperation(s1,s2,index1+1,index2+1) # we can keep moving
  else:
    deleteOperation = 1 + findMinOperation(s1,s2,index1,index2+1) 
    insertOperation = 1 + findMinOperation(s1,s2,index1+1,index2)
    replaceOperation = 1 + findMinOperation(s1,s2,index1+1,index2+1)
    return min(deleteOperation,insertOperation,replaceOperation)