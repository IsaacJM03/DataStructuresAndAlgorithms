# traversing

shoppingList = ['Milk','cheese','mugatti','yoggie','kgoeg','gjengkie','hrrngrek']

# for i in range(len(shoppingList)):
#   shoppingList[i] = "Taep " + shoppingList[i]
#   print(shoppingList[i])

# slicing

# print(shoppingList[0::2])

# #deleting

# # print(shoppingList.pop())

# del shoppingList[2:4]
# print(shoppingList)


#searching 
# # with IN

# if 'Milk'in shoppingList:
#   print(shoppingList.index('Milk'))
# else:
#   print('Value doesn\'t exist')

# linear search 

def linearSearch(list,value):
  for i in list:
    if i == value:
      return "It is at index {}".format(list.index(value))
  return 'Value doesn\'t exist'

print(linearSearch(shoppingList,'Milk'))