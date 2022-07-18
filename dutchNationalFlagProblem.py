# Given an array containing 0s, 1s and 2s, sort the array in-place. 
# You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

def dutch_flag_sort(arr):
  # TODO: Write your code here
  low = 0
  high = len(arr)-1
  i = 0 
  temp = 0
  while (i <= high):
    if arr[i] == 0:
      temp = arr[i]
      arr[i] = arr[low]
      arr[low] = temp
      i += 1
      low += 1
    elif arr[i] == 1:
      i += 1
    else:
      temp = arr[i]
      arr[i] = arr[high]
      arr[high] = temp
      high -= 1
  return arr
