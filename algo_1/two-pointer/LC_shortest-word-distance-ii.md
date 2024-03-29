# [LC_shortest-word-distance-ii](https://leetcode.com/problems/shortest-word-distance-ii)

* en

  ```en
  Design data structure with string array, and then answer queries of shortest distance between two strings from array
    WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict
    int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict
  ```

* tc

  ```tc
  Input
  ["WordDistance", "shortest", "shortest"]
  [[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]

  Output
  [null, 3, 1]
  ```

## Solution

* Time; O(m + n)

* py

  ```py
  class WordDistance:
    def __init__(self, words):
      self.dic, self.l = defaultdict(list), len(words)
      for i, x in enumerate(words):
        self.dic[x].append(i)

    def shortest(self, word1, word2):
      l1, l2, res = self.dic[word1], self.dic[word2], self.l
      i = j = 0
      while i < len(l1) and j < len(l2):
        res = min(res, abs(l1[i] - l2[j]))
        if l1[i] < l2[j]:
          i += 1
        else:
          j += 1
      return res
  ```
