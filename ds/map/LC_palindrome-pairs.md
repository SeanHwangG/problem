# [LC_palindrome-pairs](https://leetcode.com/problems/palindrome-pairs)

Given list of unique words, return all pairs of distinct indices (i, j) in given list
So that concatenation of the two words words[i] + words[j] is a palindrome

```txt
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]  # ["dcbaabcd","abcddcba","slls","llssssll"]

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]  # ["battab","tabbat"]
```

## Solution

* py

  ```py
  def palindromePairs(self, words: List[str]) -> List[List[int]]:
    lookup, res = {w: i for i, w in enumerate(words)}, []
    for i, w in enumerate(words):
      for j in range(len(w) + 1):
        pre, pos = w[:j], w[j:]
        if pre == pre[::-1] and pos[::-1] != w and pos[::-1] in lookup:
          res.append([lookup[pos[::-1]], i])
        if j != len(w) and pos == pos[::-1] and pre[::-1] != w and pre[::-1] in lookup:
          res.append([i, lookup[pre[::-1]]])
    return res
  ```
