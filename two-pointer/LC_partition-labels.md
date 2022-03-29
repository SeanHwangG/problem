```py
def partitionLabels(self, s: str) -> List[int]:
  rightmost = {c : i for i, c in enumerate(s)}
  l, r = 0, 0
  result = []
  for i, letter in enumerate(s):
    r = max(r, rightmost[letter])
    if i == r:
      result += [r-l + 1]
      l = i + 1
  return result
```
