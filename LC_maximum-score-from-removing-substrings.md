```py
def maximumGain(self, s: str, x: int, y: int) -> int:
  if x < y:
    s = s.replace("a", "-").replace("b", "a").replace("-", "b")
    x, y = y, x
  seen = Counter()
  ans = 0
  for c in s + "x":
    if c in 'ab':
      if c == "b" and 0 < seen["a"]:
        ans += x
        seen["a"], seen["b"] = seen["a"] - 1, seen["b"] - 1
      seen[c] += 1
    else:
      ans += y * min(seen["a"], seen["b"])
      seen = Counter()

  return ans
```
