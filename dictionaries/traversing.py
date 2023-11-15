# traversing and searching a dictionary

firstDict = {
  'a': 1,
  'b': 'Isaac',
  'c': 90
}

def searchDict(dict,value):
  for key in dict: #---------> Time: O(n), Space: O(1)
    if dict[key] == value:
      return key,value
    
  return "Value does not exist"

print(searchDict(firstDict,'Isaac'))
