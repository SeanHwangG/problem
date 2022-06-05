# [LC_maximum-size-subarray-sum-equals-k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k)

```en
Given int array nums and an integer k, return the maximum length of a subarray that sums to k
If there isn't one, return 0 instead.
```

```txt
Input: nums = [1,-1,5,-2,3], k = 3
Output: 4

Input: nums = [-2,-1,2,1], k = 1
Output: 2
```

## Solution

* py

  ```py
  def maxSubArrayLen(self, nums: List[int], k: int) -> int:
    res, s, d = 0, 0, {0: -1}
    for i, v in enumerate(nums):
      s += v
      res = max(res, i - d.get(s - k, i))
      d.setdefault(s, i)
    return res
  ```
