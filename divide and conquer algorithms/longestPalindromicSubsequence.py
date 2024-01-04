# elements of given string form a palindrome(when written backwards)
def findLPS(s,startIndex,endIndex):
  if startIndex > endIndex: # if we have reached the end
    return 0
  elif startIndex == endIndex: # if we have reached the middle
    return 1
  elif s[startIndex] == s[endIndex]: # if we have reached the same character
    return 2 + findLPS(s,startIndex+1,endIndex-1) # we add 2 because we have two characters(beginning and end) and we recursively call from 2nd element up to element before last
  else:
    operation1 = findLPS(s,startIndex,endIndex-1)
    operation2 = findLPS(s,startIndex+1,endIndex)
    return max(operation1,operation2)

print(findLPS("elrmenmet",0,len("elrmenmet")-1)) 