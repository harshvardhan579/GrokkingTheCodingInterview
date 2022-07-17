# Given an array with positive numbers and a positive target number, 
# find all of its contiguous subarrays whose product is less than the target number.

from collections import deque

def find_subarrays(arr, target):
  result = []
  # TODO: Write your code here
  prod = 1
  left = 0
  for right in range(len(arr)):
    prod *= arr[right]
    while (prod >= target and left <= right):
      prod /= arr[left]
      left += 1
    tempList = deque()
    for i in range(right, left-1, -1):
      tempList.appendleft(arr[i])
      result.append(list(tempList))
  return result
