```py
def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
  @lru_cache
  def fn(i, k):  # Return min waste from i with k ops
    if len(nums) - i <= k + 1:
      return 0
    if k == 0: return max(nums[i:]) * (len(nums) - i) - sum(nums[i:])
    ans, mx, sm = inf, -inf, 0
    for j in range(i, len(nums)):
      mx = max(mx, nums[j])
      sm += nums[j]
      ans = min(ans, mx * (j - i + 1) - sm + fn(j + 1, k - 1))
    return ans
  return fn(0, k)
```
