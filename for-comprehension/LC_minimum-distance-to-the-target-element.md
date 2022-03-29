* Time; O(n)
* Space; O(1)

```py
def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
  return min(abs(start - i) for i, n in enumerate(nums) if n == target)
```
