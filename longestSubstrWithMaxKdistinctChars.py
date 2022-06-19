#Given a string, find the length of the longest substring in it with no more than K distinct characters.

def longest_substring_with_k_distinct(str1, k):
  # TODO: Write your code here
  max_length = 0
  winStart = 0 
  charFreq = {}

  for winEnd in range(len(str1)):
    rightChar = str1[winEnd]
    if rightChar not in charFreq:
      charFreq[rightChar] = 0
    charFreq[rightChar] += 1

    while len(charFreq) > k:
      leftChar = str1[winStart]
      charFreq[leftChar] -= 1
      if charFreq[leftChar] == 0:
        del charFreq[leftChar]
      winStart += 1
    max_length = max(max_length, winEnd - winStart + 1)
  return max_length
