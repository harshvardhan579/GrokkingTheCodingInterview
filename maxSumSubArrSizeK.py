def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  maxSum, winSum = 0, 0
  winStart = 0

  for winEnd in range(len(arr)):
    winSum += arr[winEnd]
    if winEnd >= k-1:
      maxSum = max(maxSum, winSum)
      winSum -= arr[winStart]
      winStart += 1
  return maxSum 
