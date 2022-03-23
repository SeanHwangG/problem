```py
def maxSubArrayLen(self, nums: List[int], k: int) -> int:
  res, s, d = 0, 0, {0: -1}
  for i, v in enumerate(nums):
    s += v
    res = max(res, i - d.get(s - k, i))
    d.setdefault(s, i)
  return res
```
