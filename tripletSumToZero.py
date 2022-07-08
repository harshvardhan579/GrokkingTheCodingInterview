# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

def search_triplets(arr):
  triplets = []
  # TODO: Write your code here
  arr.sort()
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:
      continue
    search_pair(arr, -arr[i], i+1, triplets)
  return triplets

def search_pair(arr, targetSum, left, triplets):
  right = len(arr)-1
  while(left < right):
    currentSum = arr[left] + arr[right]
    if currentSum == targetSum:
      triplets.append([-targetSum, arr[left], arr[right]])
      left += 1
      right -= 1
      while left < right and arr[left] == arr[left-1]:
        left += 1
      while left < right and arr[right] == arr[right+1]:
        right -= 1
    elif targetSum > currentSum:
      left += 1
    else:
      right -= 1
