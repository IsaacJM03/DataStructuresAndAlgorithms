#include <stdio.h>

int main()
{
  int arr[2][3] = {
                  {1,2,3},
                  {4,5,6}
                };
  int rows = sizeof(arr)/sizeof(arr[0]);
  int columns = sizeof(arr[0])/sizeof(arr[0][0]);

  for(int i=0;i<rows;i++) // we divide the size of the array in bytes by the size of an element(8bytes) in order to get the number of elements
  {
    for (int j=0;j<columns;j++)
    {
      printf("%.1d", arr[i][j]);
    }
    printf("\n");
  }
  return 0;
}