# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

def make_squares(arr):
  squares = []
  # TODO: Write your code here
  n = len(arr)
  squares = [0 for x in range(n)]
  highestSquareIdx = n-1
  leftPtr, rightPtr = 0, n-1
  while leftPtr <= rightPtr:
    leftSquare = arr[leftPtr]*arr[leftPtr]
    rightSquare = arr[rightPtr]*arr[rightPtr]
    if leftSquare > rightSquare:
      squares[highestSquareIdx] = leftSquare
      leftPtr += 1
    else:
      squares[highestSquareIdx] = rightSquare
      rightPtr -= 1
    highestSquareIdx -= 1
  return squares
