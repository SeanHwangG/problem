# [LC_count-unique-characters-of-all-substrings-of-a-given-string](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string)

Let's define a function countUniqueChars(s) that returns the number of unique characters on s.
(ex: if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, 5.)
Given a string s, return the sum of countUniqueChars(t) where t is a substring of s.
Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

```txt
Input: s = "ABC"
Output: 10  # "A","B","C","AB","BC" and "ABC".

Input: s = "ABA"
Output: 8
```

## Solution

* py

  ```py
  def uniqueLetterString(self, S: str) -> int:
    dp = {c: [-1, -1] for c in string.ascii_uppercase} # last two occurrence index for every upper characters
    res = 0
    for i, c in enumerate(S):
      k, j = dp[c]
      res += (i - j) * (j - k)
      dp[c] = [j, i]
    for c in dp:
      k, j = dp[c]
      res += (len(S) - j) * (j - k)
    return res % (10**9 + 7)
  ```
