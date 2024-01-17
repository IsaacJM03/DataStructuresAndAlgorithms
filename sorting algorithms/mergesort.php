<?php

// Merges two subarrays of arr[].
// First subarray is arr[left..middle]
// Second subarray is arr[middle+1..right]

function merge(&$arr, $left, $middle, $right)
{
  $n1 = $middle - $left + 1;
  $n2 = $right - $middle;

  // temporary arrays
  $Left = array();
  $Right = array();

  // copy data to temp arrays Left[] and Right[]
  for ($i = 0; $i < $n1; $i++)
    $Left[$i] = $arr[$left + $i];
  for ($j = 0; $j < $n2; $j++)
    $Right[$j] = $arr[$middle + 1 + $j];

  // merge the temp arrays bak into arr[left...right]
  $i = 0;
  $j = 0;
  $k = $left;
  while ($i < $n1 && $j < $n2) {
    if ($Left[$i] <= $Right[$j]) {
      $arr[$k] = $Left[$i];
      $i++;
    } else {
      $arr[$k] = $Right[$j];
      $j++;
    }
    $k++;
  }

  // copy the remaining elements of Left[], if there are any
  while ($i < $n1) {
    $arr[$k] = $Left[$i];
    $i++;
    $k++;
  }

  // copy the remaining elements of Right[], if there are any
  while ($j < $n2) {
    $arr[$k] = $Right[$j];
    $j++;
    $k++;
  }
}

// left is for left index and right is right index of the sub-array of arr to be sorted

function mergeSort(&$arr, $left, $right)
{
  if ($left < $right) {
    $middle = $left + (int)(($right - $left) / 2);

    // sort first and second halves
    mergeSort($arr, $left, $middle);
    mergeSort($arr, $middle + 1, $right);
    merge($arr, $left, $middle, $right);
  }
}

// Function to print an array
function printArray($A, $size)
{
    for ($i = 0; $i < $size; $i++)
        echo $A[$i]." ";
    echo "\n";
}

$arr = array(10, 7, 8, 9, 1, 5);
$arr_size = sizeof($arr);

echo "Given array is \n";
printArray($arr, $arr_size);

mergeSort($arr,0,$arr_size-1);

echo "\nSorted array is \n";
printArray($arr, $arr_size);

?>