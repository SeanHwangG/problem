# [LC_find-k-th-smallest-pair-distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance)

Distance of a pair of integers a and b is defined as absolute difference between a and b.
Given an integer array nums and an integer k, return kth smallest distance among all the pairs nums[i] and nums[j]
where 0 <= i < j < nums.length.

```txt
Input: nums = [1,3,1], k = 1
Output: 0

Input: nums = [1,1,1], k = 2
Output: 0
```

## Solution

```py
def smallestDistancePair(self, li: List[int], k: int) -> int:
  def enough(distance) -> bool:  # two pointers
    count, l, r = 0, 0, 0
    while l < len(li) or r < len(li):
      while r < len(li) and li[r] - li[l] <= distance:
        r += 1
      count += r - l - 1
      l += 1
    return count >= k

  li.sort()
  l, r = 0, li[-1] - li[0]
  while l < r:
    m = l + (r - l) // 2
    if not enough(m):
      l = m + 1
    else:
      r = m
  return l
```
