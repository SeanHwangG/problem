# [LC_word-break](https://leetcode.com/problems/word-break)

Given a string s and a dictionary of strings wordDict
return if s can be segmented into a space-separated sequence of one or more dictionary words

```txt
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
```

## Solution

```py
def wordBreak(self, s: str, words: List[str]) -> bool:
  dp, words_set, max_len = [True], set(words), len(max(words, key=len)) if words else 0
  for i in range(1, len(s) + 1):
    dp += any(dp[j] and s[j:i] in words_set for j in range(max(0, i - max_len), i)),
  return dp[-1]
```
