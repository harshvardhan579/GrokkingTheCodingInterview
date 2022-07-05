# Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each element appears only once.

def remove_duplicates(arr):
  # TODO: Write your code here
  nextNonDup = 1
  i = 0
  while (i < len(arr)):
    if arr[nextNonDup-1] != arr[i]:
      arr[nextNonDup] = arr[i]
      nextNonDup += 1
    i += 1
    
  return nextNonDup
