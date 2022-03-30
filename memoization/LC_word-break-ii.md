# [LC_word-break-ii](https://leetcode.com/problems/word-break-ii)

Given a string s and a dictionary of strings wordDict
Add spaces in s to construct a sentence where each word is a valid dictionary word
Return all such possible sentences in any order

```txt
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
```

## Solution

```py
def wordBreak(self, s: str, words: List[str]) -> List[str]:
  words, dp = set(words), dict()

  @lru_cache
  def helper(r):
    if r == 0:
      return ['']
    rst = []
    for l in range(r - 1, -1, -1):
      if s[l: r] in words:
        for prevStr in helper(l):
          rst.append(' '.join([prevStr, s[l: r]]).strip())
    return rst

  return helper(len(s))
```
