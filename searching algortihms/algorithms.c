#include<stdio.h>
#include<math.h>

int binarySearch(int arr[],int n,int value)
{
  int start = 0;
  int end = n-1;
  int middle = floor((start+end)/2);
  while (!(arr[middle] == value) && start <= end)
  {
    if(value < arr[middle])
    {
      end = middle - 1;
    } else {
      start = middle + 1;
    }
    middle = floor((start+end)/2);
  }
  if(arr[middle] == value)
  {
    return middle;
  } else {
    return -1;
  }
  
}

int main()
{
  int arr[] = {1,2,3,4,5,6,7,8,9,10};
  int n = sizeof(arr)/sizeof(arr[0]);
  int value = 5;
  int result = binarySearch(arr, n, value);

  if (result != -1)
  {
      printf("Value found at index: %d\n", result);
  }
  else
  {
      printf("Value not found\n");
  }

  return 0;
}