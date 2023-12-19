import math


def bubbleSort(customList):   # ---------> O(n^2)
  for i in range(len(customList)-1): # keep decreasing the number of adjacent pairs(pairs close to each other)
    for j in range(len(customList)-i-1): # need to decrease number of loops as the last is always regarded as "fully sorted"
      if customList[j] > customList[j+1]: # j+1 is next(2nd) element in adajcent pair
        customList[j],customList[j+1] = customList[j+1], customList[j]
  return customList


def selectionSort(customList):  #----> O(n^2)
  for i in range(len(customList)): # since we are traversing entire unsorted array for each iteration
    min_index = i 
    for j in range(i+1, len(customList)):
      if customList[min_index] > customList[j]:
        min_index = j #swapping smallest element in unsorted to beginning
    customList[i],customList[min_index] = customList[min_index], customList[i]
  return customList



def insertionSort(customList): # -----------> 0(n^2)
  for i in range(1, len(customList)):
    key = customList[i] # current element
    j = i-1 # element just before the current
    while j>=0 and key < customList[j]:
      customList[j+1] = customList[j] #  Move elements greater than the current element to the right.
      j -= 1 # reduce elements in unsorted array
    customList[j+1] = key # Insert the current element at its correct position in the sorted array.
  return customList


def bucketSort(customList):
  numberOfBuckets = round(math.sqrt(len(customList)))
  maxValue = max(customList)
  arr = []
  
  for i in range(numberOfBuckets):
    arr.append([])# creating 2d array for inserting elements later

  for j in customList:
    index_b = math.ceil(j * numberOfBuckets / maxValue)
    arr[index_b-1].append(j) # inserting into appropriate basing on index j starting with the last

  for i in range(numberOfBuckets):
    if arr[i]:
      arr[i] = quickSort(arr[i],0,len(arr[i])-1) # sorting the bucket, not entire list

  k = 0
  for i in range(numberOfBuckets):
    for j in range(len(arr[i])):
      customList[k] = arr[i][j] # populating the 2d array
      k += 1 # incrementing go to nect element
  return customList # merging all buckets inside custom list


def merge(customList,l,m,r): # sub array, left(first), middle, right(end)
  # l, m, and r are indices such that l <= m < r. 
  # The two subarrays are customList[l..m] and customList[m+1..r].
  n1 = m - l + 1# number of elements in first in sub category
  n2 = r - m # number of elements in 2nd sub category

  # creating and populating the temporary sub arrays
  L = [0]*(n1)
  R = [0]*(n1)

  for i in range(0,n1):
    L[i] = customList[l+i] # elements being copied to original array

  for j in range(0,n2):
    R[j] = customList[m+1+j] # elements being copied to original array

  i = 0 # initial index of first sub array
  j = 0 # initial index of second sub array
  k = l # initial index of merged array

  # when merging we need to sort 
  while i < n1 and j < n2:
    if L[i] <= R[j]: #This checks if the current element in the left half (L[i]) is less than or equal to the current element in the right half (R[j])
      customList[k]= L[i] # element from the left half should be placed in the merged array.
      i += 1 # Moves the index i to the next position in the left half since we have used the current element.
    else: # the current element in the right half is smaller, so we place it in the merged array.
      customList[k] = R[j]
      j += 1 # Moves the index j to the next position in the right half since we have used the current element.
    k += 1 # Advances the index k in the merged array to the next position.

  while i < n1: # is for the remaining elements in the left half (L). It iterates through the remaining elements, placing them in the merged array.
    customList[k] = L[i]
    i += 1
    k += 1

  while j < n2: # is for the remaining elements in the right half (R). It iterates through the remaining elements, placing them in the merged array.
    customList[k] = R[j]
    j += 1
    k += 1

def mergeSort(customList,l ,r):
  if l < r :
    m = (l+(r-1))//2 # floor division
    mergeSort(customList,l,m)
    mergeSort(customList,m+1,r)
    merge(customList,l,m,r)
  return customList

def partition(customList, low, high):
  i = low - 1 # index of smaller element
  pivot = customList[high] # pivot
  for j in range(low,high): # traverse all elements from low to high
    if customList[j] <= pivot: # if current element is smaller than or equal to pivot
      i += 1
      customList[i],customList[j] = customList[j],customList[i] # swap elements 
  customList[i+1],customList[high] = customList[high],customList[i+1] # swap new pivot with last element
  return (i+1)

def quickSort(customList,low,high):
  if low < high: # if array has more than 1 element
    pi = partition(customList,low,high) # partition index is pi
    quickSort(customList,low,pi-1) # sort elements before/left of pi
    quickSort(customList,pi+1,high) # sort elements on the right of pi 
  return customList


def heapify(customList,n,i):
  smallest = i
  l = 2 * i + 1 # left child
  r = 2 * i + 2 # right child
  
  if l < n and customList[l] < customList[smallest]:
    smallest = l # left child set to smallest

  if r < n and customList[r] < customList[smallest]:
    smallest = r # right child set to smallest

  if smallest != i:
    customList[i],customList[smallest] = customList[smallest],customList[i]
    heapify(customList,n,smallest) # setting new head as smallest

def heapSort(customList):
  n = len(customList)
  for i in range(int(n/2)-1,-1,-1): # building the heap, looping from last non-leaf node skipping leaf nodes up to root
    heapify(customList,n,i) # setting new head as current element
  
  for i in range(n-1,0,-1):
    customList[i],customList[0] = customList[0],customList[i] # swap root with last element
    heapify(customList,i,0) # setting new head as root
  customList.reverse()


sampleList = [3,1,5,6,7,9,10,2,4,8]
heapSort(sampleList)
print(sampleList)

# low = 0
# high = len(sampleList) - 1
quickSort(sampleList, 0, len(sampleList) - 1)
print(sampleList)
# print(mergeSort(sampleList,0,7))
print(bucketSort(sampleList))
print(insertionSort(sampleList))
# print(bubbleSort(sampleList))
# print(selectionSort(sampleList))