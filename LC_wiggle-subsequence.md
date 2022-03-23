```py
def wiggleMaxLength(self, nums: List[int]) -> int:
  len_dec, len_inc = 1, 1
  for i in range(1, len(nums)):
    len_dec = len_inc + 1 if nums[i] < nums[i-1] else len_dec
    len_inc = len_dec + 1 if nums[i] > nums[i-1] else len_inc
  return max(len_inc, len_dec)
```
