# Convert one string to another with minimum number of operations


def findMinOperation(s1,s2,index1,index2,tempDict):
  if index1 == len(s1): # if we have reached the end of the string
    return len(s2) - index2 # we need to insert the remaining characters
  if index2 == len(s2): # if we have reached the end of the string
    return len(s1) - index1 # we need to insert the remaining characters
  if s1[index1] == s2[index2]: # if we have reached the same character
    return findMinOperation(s1,s2,index1+1,index2+1,tempDict) # we can keep moving
  else:
    dictKey = str(index1) + str(index2)
    if dictKey not in tempDict:
      deleteOperation = 1 + findMinOperation(s1,s2,index1,index2+1,tempDict) 
      insertOperation = 1 + findMinOperation(s1,s2,index1+1,index2,tempDict)
      replaceOperation = 1 + findMinOperation(s1,s2,index1+1,index2+1,tempDict)
      tempDict[dictKey] = min(deleteOperation,insertOperation,replaceOperation)
    return tempDict[dictKey]
  

def findMinOperationBU(s1, s2, tempDict):
    for i1 in range(len(s1)+1):
        dictKey = str(i1)+'0'
        tempDict[dictKey] = i1
    for i2 in range(len(s2)+1):
        dictKey = '0'+str(i2)
        tempDict[dictKey] = i2
    
    for i1 in range(1,len(s1)+1):
        for i2 in range(1,len(s2)+1):
            if s1[i1-1] == s2[i2-1]:
                dictKey = str(i1)+str(i2)
                dictKey1 = str(i1-1)+str(i2-1)
                tempDict[dictKey] = tempDict[dictKey1]
            else:
                dictKey = str(i1)+str(i2)
                dictKeyD = str(i1-1)+str(i2)
                dictKeyI = str(i1)+str(i2-1)
                dictKeyR = str(i1-1)+str(i2-1)
                tempDict[dictKey] = 1 + min(tempDict[dictKeyD], min(tempDict[dictKeyI],tempDict[dictKeyR]))
    dictKey = str(len(s1))+str(len(s2))
    return tempDict[dictKey]

print(findMinOperation("table", "tbrltt", 0, 0,{}))
print(findMinOperationBU("table", "tbrltt", {}))