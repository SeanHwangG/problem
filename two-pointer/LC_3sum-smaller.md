```py
def threeSumSmaller(self, nums, target):
  count = 0
  nums.sort()
  for i in range(len(nums)):
    j, k = i + 1, len(nums)-1
    while j < k:
      s = nums[i] + nums[j] + nums[k]
      if s < target:
        count += k-j # if (i,j,k) works, then (i,j,k), (i,j,k-1) ... (i, j, j + 1)
        j += 1
      else:
        k -= 1
  return count
```
