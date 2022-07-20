# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

def shortest_window_sort(arr):
  # TODO: Write your code here
  firstP, lastP = 0, len(arr)-1
  arr2 = sorted(arr)
  while (firstP <= lastP):
    if arr[firstP] == arr2[firstP]:
      firstP += 1
    elif arr[lastP] == arr2[lastP]:
      lastP -= 1
    else:
      return len(arr[firstP:lastP])+1
  return 0
