# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s,
# find the length of the longest contiguous subarray having all 1s.

def length_of_longest_substring(arr, k):
  # TODO: Write your code here
  winStart = 0
  maxLen = 0
  maxOneCount = 0

  for winEnd in range(len(arr)):
    if arr[winEnd] == 1:
      maxOneCount += 1

    if (winEnd - winStart + 1 - maxOneCount) > k:
      if arr[winStart] == 1:
        maxOneCount -= 1
      winStart += 1
    maxLen = max(maxLen, winEnd - winStart + 1)
  return maxLen
