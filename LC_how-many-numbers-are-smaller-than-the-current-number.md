```py
def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
  return [sum(m < n for m in nums) for n in nums]
```
