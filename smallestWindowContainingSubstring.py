# Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

def find_substring(str1, pattern):
  # TODO: Write your code here
  winStart = 0
  minLen = len(str1)+1
  charFreq = {}
  matching = 0
  strr = ""

  for chhr in pattern:
    if chhr not in charFreq:
      charFreq[chhr] = 0
    charFreq[chhr] += 1

  for winEnd in range(len(str1)):
    rightChar = str1[winEnd]
    if rightChar in charFreq:
      charFreq[rightChar] -= 1
      if charFreq[rightChar] >= 0:
        matching += 1
    
    while matching == len(pattern):
      if minLen > winEnd-winStart+1:
        minLen = winEnd-winStart+1
        subStrStart = winStart
    
      leftChar = str1[winStart]
      winStart += 1

      if leftChar in charFreq:
        if charFreq[leftChar] == 0:
          matching -= 1
        charFreq[leftChar] += 1
  if minLen > len(str1):
    return ""

  return str1[subStrStart:subStrStart+minLen]
