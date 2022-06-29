# Given a string and a pattern, find out if the string contains any permutation of the pattern.

def find_permutation(str1, pattern):
  # TODO: Write your code here
  winStart = 0
  charFreq = {}
  matching = 0
  k = len(pattern)

  for chrr in pattern:
    if chrr not in charFreq:
      charFreq[chrr] = 0
    charFreq[chrr] += 1
  
  for winEnd in range(len(str1)):
    rightChar = str1[winEnd]
    if rightChar in charFreq:
      charFreq[rightChar] -= 1
      if charFreq[rightChar] == 0:
        matching += 1
    
    if matching == len(charFreq):
      return True
    
    if (winEnd-winStart+1) >= k:
      leftChar = str1[winStart]
      winStart += 1
      if leftChar in charFreq:
        if charFreq[leftChar] == 0:
          matching -= 1
        charFreq[leftChar] += 1
    
  return False
