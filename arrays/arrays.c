#include <stdio.h>

int main()
{
  int arr[] = {1, 2, 3, 4, 5};

  for(int i=0;i<sizeof(arr)/sizeof(arr[0]);i++) // we divide the size of the array in bytes by the size of an element(8bytes) in order to get the number of elements
  {
    printf("%.1d\n", arr[i]);
  }
  return 0;
}