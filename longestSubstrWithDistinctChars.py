# Given a string, find the length of the longest substring, which has all distinct characters.

def non_repeat_substring(str):
  # TODO: Write your code here
  maxLen = 0
  winStart = 0
  charIndexMap = {}

  for winEnd in range(len(str)):
    rightChar = str[winEnd]
    if rightChar in charIndexMap:
      winStart = max(winStart, charIndexMap[rightChar]+1)
    charIndexMap[rightChar] = winEnd
    maxLen = max(maxLen, winEnd - winStart + 1)
  return maxLen
