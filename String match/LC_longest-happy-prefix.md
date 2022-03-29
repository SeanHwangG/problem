```py
def longestPrefix(self, s: str) -> str:
  lps = [0] * len(s)
  for i in range(1, len(s)):
    t = lps[i-1]
    while t and s[t] != s[i]:
      t = lps[t-1]
    if s[t] == s[i]:
      t += 1
    lps[i] = t
  return s[:lps[-1]]
```
