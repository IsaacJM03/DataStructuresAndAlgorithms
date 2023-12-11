def bubbleSort(customList):   # ---------> O(n^2)
  for i in range(len(customList)-1): # keep decreasing the number of adjacent pairs(pairs close to each other)
    for j in range(len(customList)-i-1): # need to decrease number of loops as the last is always regarded as "fully sorted"
      if customList[j] > customList[j+1]: # j+1 is next(2nd) element in adajcent pair
        customList[j],customList[j+1] = customList[j+1], customList[j]
  print(customList)


def selectionSort(customList):  #----> O(n^2)
  for i in range(len(customList)): # since we are traversing entire unsorted array for each iteration
    min_index = i 
    for j in range(i+1, len(customList)):
      if customList[min_index] > customList[j]:
        min_index = j #swapping smallest element in unsorted to beginning
    customList[i],customList[min_index] = customList[min_index], customList[i]
  print(customList)


sampleList = [3,8,26,78,3,4,9,32]
# bubbleSort(sampleList)
selectionSort(sampleList)