# [LC_maximum-gap](https://leetcode.com/problems/maximum-gap)

* en

  ```en
  Given an integer array nums, return maximum difference between two successive elements in its sorted form
  If the array contains less than two elements, return 0
  ```

* tc

  ```tc
  Input: nums = [3,6,9,1]
  Output: 3
  ```

## Solution

* py

  ```py
  def maximumGap(self, num):
    if len(num) < 2 or min(num) == max(num):
      return 0
    mn, mx = min(num), max(num)
    size = (mx - mn) // (len(num)-1) or 1
    bucket = [[math.inf, -math.inf] for _ in range((mx - mn) // size + 1)]
    for n in num:
      mx = bucket[(n - mn) // size]
      mx[0] = min(mx[0], n)
      mx[1] = max(mx[1], n)
    bucket = [mx for mx in bucket if mx[0] != math.inf]
    return max(bucket[i][0] - bucket[i - 1][1] for i in range(1, len(bucket)))
  ```
