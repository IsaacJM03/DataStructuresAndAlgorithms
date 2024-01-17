#include<stdio.h>

// n is the number of elements in the array calculated in the main using size of the array divided by size of the first element in the array

void bubbleSort(int arr[], int n)
{
  for (int i = 0; i < n-1; i++)
  {
    for (int j = 0; j < n-i-1; j++)
    {
      if (arr[j] > arr[j+1])
      {
        int temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
      }
    }
    
  }
  printf("Sorted array: ");
  for (int i = 0; i < n; i++)
  {
    printf("%d ", arr[i]);
  }
}

void selectionSort(int arr[], int n)
{
  for (int i = 0; i < n; i++)
  {
    int minIndex = i;
    for (int j = i+1; j < n; j++)
    {
      if (arr[minIndex] > arr[j])
      {
        minIndex = j;
      }
    }
    int temp = arr[minIndex];
    arr[minIndex] = arr[i];
    arr[i] = temp;
  }
  printf("Sorted array: ");
  for (int i = 0; i < n; i++)
  {
    printf("%d ", arr[i]);
  }
}


void insertionSort(int arr[],int n)
{
  for (int i = 1; i < n; i++)
  {
    int key = arr[i];
    int j = i-1;
    while (j>=0 && key < arr[j])
    {
      arr[j+1] = arr[j];
      j -= 1;
    }
    arr[j+1] = key;
  }
  printf("Sorted array: ");
  for (int i = 0; i < n; i++)
  {
    printf("%d ", arr[i]);
  }
}



int main()
{
  int arr[] = {64, 34, 25, 12, 22, 11, 90};
  int n = sizeof(arr)/sizeof(arr[0]);
  insertionSort(arr, n);
  return 0;
}
