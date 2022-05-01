# [LC_find-minimum-in-rotated-sorted-array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)

Perform binary search on rotated sorted array

```txt
Input: nums = [3,4,5,1,2]
Output: 1
```

## Solution

* py

  ```py
  def findMin(self, li):
    lo, hi = 0, len(li) - 1
    while lo < hi:
      mi = (lo + hi) // 2
      if li[mi] > li[hi]:
        lo = mi + 1
      else:
        hi = mi
    return li[lo]
  ```
