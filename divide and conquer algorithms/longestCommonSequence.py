# basically subsets or taking the longest word that can be formed from the intersesction of 2 strings

def findLCS(s1,s2,index1,index2):
  if index1 == len(s1) or index2 == len(s2): # if we have reached the end of the string
    return 0
  if s1[index1] == s2[index2]: # if we have reached the same character
    return 1 + findLCS(s1,s2,index1+1,index2+1) # recursive call in order to check the next character in the string
  else:
    operation1 = findLCS(s1,s2,index1,index2+1)
    operation2 = findLCS(s1,s2,index1+1,index2)
    return max(operation1,operation2)
  
print(findLCS("xyzabcd","absnoejscd",0,0)) # 0,0 because we start from the first character of each string
