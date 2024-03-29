# [LC_shortest-word-distance](https://leetcode.com/problems/shortest-word-distance)

* en

  ```en
  Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2
  Return shortest distance between these two words in the list
  ```

* tc

  ```tc
  Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
  Output: 3

  Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
  Output: 1
  ```

## Solution

* py

  ```py
  def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
    ans, cur_word, cur_idx = len(words), None, 0
    for index, word in enumerate(words):
      if word != word1 and word != word2:
        continue
      if cur_word and word != cur_word:
        ans = min(ans, index - cur_idx)
      cur_word, cur_idx = word, index
    return ans
  ```
