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
