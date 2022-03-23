```py
def maxAscendingSum(self, nums: List[int]) -> int:
  mx = 0
  for i, x in enumerate(nums):
    if i == 0 or nums[i-1] >= nums[i]: cur = 0
    cur += nums[i]
    mx = max(mx, cur)
  return mx
```
