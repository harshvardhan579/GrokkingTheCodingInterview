# Given a string and a list of words, find all the starting indices of substrings in the given string 
# that are a concatenation of all the given words exactly once without any overlapping of words. 
# It is given that all words are of the same length.

def find_word_concatenation(str1, words):
  result_indices = []
  # TODO: Write your code here
  if len(words) == 0 or len(words[0]) == 0:
    return []
  
  wordFreq = {}

  for word in words:
    if word not in wordFreq:
      wordFreq[word] = 0
    wordFreq[word] += 1

  wordCount = len(words)
  wordLength = len(words[0])

  for i in range((len(str1) - wordCount * wordLength)+1):
    wordSeen = {}
    for j in range(0, wordCount):
      nextWordIndex = i + j * wordLength
      word = str1[nextWordIndex: nextWordIndex + wordLength]
      if word not in wordFreq:
        break

      if word not in wordSeen:
        wordSeen[word] = 0
      wordSeen[word] += 1

      if wordSeen[word] > wordFreq.get(word, 0):
        break
      
      if j + 1 == wordCount:
        result_indices.append(i)


  return result_indices
