{% tabs %}{% tab title='LC_1763.py' %}

```py
def longestNiceSubstring(self, s: str) -> str:
  if not s: return ""
  ss = set(s)
  for i, c in enumerate(s):
    if c.swapcase() not in ss:
      s0 = self.longestNiceSubstring(s[:i])
      s1 = self.longestNiceSubstring(s[i+1:])
      return max(s0, s1, key=len)
  return s
```

{% endtab %}{% endtabs %}