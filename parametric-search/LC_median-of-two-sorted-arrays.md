# [LC_median-of-two-sorted-arrays](https://leetcode.com/problems/median-of-two-sorted-arrays)

Return median of two sorted array

```txt
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000  # merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5
```

## Solution

```py
def findMedianSortedArrays(self, nums1, nums2):
  a, b = sorted((nums1, nums2), key=len)
  after = (len(a) + len(b) - 1) // 2
  lo, hi = 0, len(a)
  while lo < hi:
    mi = (lo + hi) // 2
    if after-mi-1 < 0 or a[mi] >= b[after-mi-1]:
      hi = mi
    else:
      lo = mi + 1
  nextfew = sorted(a[lo:lo+2] + b[after-lo:after-lo+2])
  return (nextfew[0] + nextfew[1 - (len(a) + len(b)) % 2]) / 2.0
```
