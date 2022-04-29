# [LC_minimum-operations-to-reduce-x-to-zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero)

Can either pop from left or right element and subtract from x
Print minimum number of operations to make x to be 0

```txt
Input: nums = [1,1,4,2,3], x = 5
Output: 2
```

## Solution

* Equivalent of finding largest contiguous subarrays with sum(nums) - x

* py

```py
def minOperations(self, nums, x) :
  cumsum = [0] + list(accumulate(nums))
  dic = {c : i for i, c in enumerate(cumsum)}
  goal = cumsum[-1] - x
  ans = -float("inf")

  if goal < 0: return -1
  for num in dic:
    if num + goal in dic:
      ans = max(ans, dic[num + goal] - dic[num])

  return len(nums) - ans if ans != -float("inf") else -1
```
