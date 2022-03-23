```py
def makeArrayIncreasing(self, li1: List[int], li2: List[int]) -> int:
  dp = {-1:0}
  li2.sort()
  for i in li1:
    tmp = defaultdict(lambda: float('inf'))
    for key in dp:
      if i > key:
        tmp[i] = min(tmp[i], dp[key])
      loc = bisect_right(li2, key)
      if loc < len(li2):
        tmp[li2[loc]] = min(tmp[li2[loc]], dp[key]+1)
    dp = tmp
  return min(dp.values()) if dp else -1
```
