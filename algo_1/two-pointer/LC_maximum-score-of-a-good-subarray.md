# [LC_maximum-score-of-a-good-subarray](https://leetcode.com/problems/maximum-score-of-a-good-subarray)

Given array of integers nums (0-indexed) and an integer k
Score of a subarray (i, j) is min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). good subarray if i <= k <= j
Return maximum possible score of good subarray

```txt
Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
```

## Solution

* py

```py
def maximumScore(self, nums: List[int], k: int) -> int:
  res = mini = nums[k]
  i, j, n = k, k, len(nums)
  while i > 0 or j < n - 1:
    if (nums[i - 1] if i else 0) < (nums[j + 1] if j < n - 1 else 0):
      j += 1
    else:
      i -= 1
    mini = min(mini, nums[i], nums[j])
    res = max(res, mini * (j - i + 1))
  return res
```
