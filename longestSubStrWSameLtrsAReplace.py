# Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter,
# find the length of the longest substring having the same letters after replacement.

def length_of_longest_substring(str1, k):
  # TODO: Write your code here
  winStart = 0
  maxLen = 0
  maxRepeat = 0
  
  frequencyMap = {}

  for winEnd in range(len(str1)):
    rightChar = str1[winEnd]
    if rightChar not in frequencyMap:
      frequencyMap[rightChar] = 0
    frequencyMap[rightChar] += 1

    maxRepeat = max(maxRepeat, frequencyMap[rightChar])

    if (winEnd-winStart+1-maxRepeat) > k:
      leftChar = str1[winStart]
      frequencyMap[leftChar] -= 1
      winStart += 1

    maxLen = max(maxLen, winEnd-winStart+1)
  return maxLen
