# [LC_construct-k-palindrome-strings](https://leetcode.com/problems/construct-k-palindrome-strings)

```en
Given string s and int k. You should construct k non-empty palindrome strings using all the characters in s
Return if you can use all the characters in s to construct k palindrome strings
```

```txt
Input: s = "annabelle", k = 2
Output: true
```

## Solution

* py

  ```py
  def canConstruct(self, s, k):
    return sum(i & 1 for i in collections.Counter(s).values()) <= k <= len(s)
  ```
