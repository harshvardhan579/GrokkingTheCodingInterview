# Given an array of positive integers and a number ‘S,’ 
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
# Return 0 if no such subarray exists.

import math

def smallest_subarray_sum(s, arr):
  # TODO: Write your code here
  minLen = math.inf
  winSum = 0
  winStart = 0

  for winEnd in range(0, len(arr)):
    winSum += arr[winEnd]

    while winSum >= s:
      minLen = min(minLen, winEnd - winStart + 1)
      winSum -= arr[winStart]
      winStart += 1
  
  if minLen == math.inf:
    return 0
  return minLen
