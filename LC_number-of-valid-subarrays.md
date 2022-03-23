```py
def validSubarrays(self, nums: List[int]) -> int:
  nums.append(-inf)
  stack, result = [], 0
  for i, num in enumerate(nums):
    while stack and nums[stack[-1]] > num:
      result += i - stack.pop()
    stack.append(i)

  return result
```
