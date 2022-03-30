# [LC_maximum-value-at-a-given-index-in-a-bounded-array](https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array)

Given three positive integers n, index and maxSum. construct 0 indexed array nums that satisfies the following conditions
  nums.length == n
  nums[i] is a positive integer where 0 <= i < n
  abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1
  The sum of all the elements of nums does not exceed maxSum
  nums[index] is maximized
Return nums[index] of the constructed array

```txt
Input: n = 4, index = 2,  maxSum = 6
Output: 2
```

## Solution

```py
def maxValue(self, n, index, maxSum):
  def test(mid):
    left = max(mid - index, 0)
    right = max(mid - ((n - 1) - index), 0)
    return (mid + left) * (mid - left + 1) // 2 + (mid + right - 1) * (mid - right) // 2

  maxSum -= n
  left, right = 0, maxSum
  while left < right:
    mid = (left + right + 1) // 2
    if test(mid) <= maxSum:
      left = mid
    else:
      right = mid - 1
  return left + 1
```
