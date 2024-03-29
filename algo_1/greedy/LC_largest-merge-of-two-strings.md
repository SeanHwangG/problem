# [LC_largest-merge-of-two-strings](https://leetcode.com/problems/largest-merge-of-two-strings)

* en

  ```en
  Given two strings word1 and word2, construct a string merge in the following way
  While either word1 or word2 are non-empty, choose one of the following options:
    If word1 is non-empty, append the first character in word1 to merge and delete it from word1
    If word2 is non-empty, append the first character in word2 to merge and delete it from word2
  Return the lexicographically largest merge you can construct
  ```

* tc

  ```tc
  Input: word1 = "abcabc", word2 = "abdcaba"
  Output: "abdcabcabcaba"
  ```

## Solution

* py

  ```py
  def largestMerge(self, s1, s2):
    if s1 >= s2 > '':
      return s1[0] + self.largestMerge(s1[1:], s2)
    if s2 >= s1 > '':
      return s2[0] + self.largestMerge(s1, s2[1:])
    return s1 + s2
  ```
