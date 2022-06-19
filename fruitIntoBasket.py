# Write a function to return the maximum number of fruits in both baskets.

def fruits_into_baskets(fruits):
  # TODO: Write your code here
  maxLen = 0 
  winStart = 0
  fruitNo = {}

  for winEnd in range(len(fruits)):
    rightFruit = fruits[winEnd]
    if rightFruit not in fruitNo:
      fruitNo[rightFruit] = 0
    fruitNo[rightFruit] += 1

    while len(fruitNo) > 2:
      leftFruit = fruits[winStart]
      fruitNo[leftFruit] -= 1
      if fruitNo[leftFruit] == 0:
        del fruitNo[leftFruit]
      winStart += 1
    maxLen = max(maxLen, winEnd-winStart+1)

  return maxLen
  
