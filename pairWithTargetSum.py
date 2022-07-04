# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
  firstP = 0
  lastP = len(arr)-1

  while(firstP < lastP):
    curSum = arr[firstP] + arr[lastP]
    if curSum == target_sum:
      return [firstP, lastP]

    if curSum > target_sum:
      lastP -= 1
    else:
      firstP += 1
  return [-1, -1]
