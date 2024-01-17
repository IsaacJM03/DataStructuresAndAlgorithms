<?php
// This Function takes place last element as pivot
// Place the pivot as correct position
// In Sorted Array, and places all smaller to left
// of pivot and all greater element to its right of pivot

function partition(&$arr, $low, $high)
{
  // choose the pivot
  $pivot = $arr[$high];

  // index of smaller element and index of greater element
  $i = $low - 1;

  for ($j=$low; $j < $high-1 ; $j++) 
  { 
    if ($arr[$j] < $pivot) 
    {
      // increment index of smaller element
      $i++;
      list($arr[$i], $arr[$j]) = [$arr[$j], $arr[$i]];
    }
  }
  // move pivot element to correct position
  list($arr[$i+1], $arr[$high]) = [$arr[$high], $arr[$i+1]];
  return $i+1;
}

// The main function that implement as QuickSort
// arr[]:- Array to be sorted
// low:- Starting Index
// high:- Ending Index
function quickSort(&$arr, $low, $high)
{
  if ($low<$high) 
  {
    // pi is partition
    $pi = partition($arr, $low, $high);

    // sort the array
    // before partition
    quickSort($arr, $low, $pi-1);
    // after partition
    quickSort($arr, $pi+1, $high);
  }
}

$arr = array(10, 7, 8, 9, 1, 5);
$n = count($arr);

quickSort($arr, 0, $n-1);
echo "Sorted array: \n";

for ($i=0; $i < $n ; $i++) 
{ 
  echo $arr[$i]. " ";
}
?>