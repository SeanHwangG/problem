# [LC_longest-consecutive-sequence](https://leetcode.com/problems/longest-consecutive-sequence)

Given unsorted array of int nums, return the length of the longest consecutive elements sequence

```txt
Input: nums = [100,4,200,1,3,2]
Output: 4
```

## Solution

```py
def longestConsecutive(self, nums: List[int]) -> int:
  nums = set(nums)
  best = 0
  for x in nums:
    if x - 1 not in nums:
      y = x + 1
      while y in nums:
        y += 1
      best = max(best, y - x)
  return best
```
