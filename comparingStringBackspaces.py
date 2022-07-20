# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

def backspace_compare(str1, str2):
  # TODO: Write your code here
  ind1 = len(str1)-1
  ind2 = len(str2)-1

  while (ind1 >= 0 and ind2 >= 0):
    i1 = getNextValidChar(str1, ind1)
    i2 = getNextValidChar(str2, ind2)
    if i1<0 and i2<0:
      return True
    if i1<0 or i2<0:
      return False
    if str1[i1] != str2[i2]:
      return False
    ind1 = i1-1
    ind2 = i2-1
  return True

def getNextValidChar(str, index):
  backspaceCount = 0
  while (index >= 0):
    if str[index] == '#':
      backspaceCount += 1
    elif backspaceCount > 0:
      backspaceCount -= 1
    else:
      break
    index -=1
  return index
