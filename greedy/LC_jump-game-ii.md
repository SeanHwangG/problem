* Time, Space; O(N), O(1)

```py
def jump(self, nums):
  l, r = 0, nums[0]
  time = 1
  while r < len(nums) - 1:
    time += 1
    nxt = max(i + nums[i] for i in range(l, r + 1))
    l, r = r, nxt # nxt : farthest point that all points in [l, r] can reach
  return time
```
