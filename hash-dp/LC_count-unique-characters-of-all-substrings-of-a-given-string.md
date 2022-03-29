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
