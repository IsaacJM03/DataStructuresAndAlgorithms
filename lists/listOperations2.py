myList = list()

while (True):
  inp = input("Enter a number(input 'done' when finished): ")
  if inp == 'done' or inp == 'Done': break
  value = float(inp)
  myList.append(value)

average = sum(myList) / len(myList)

print('Average: ',average)