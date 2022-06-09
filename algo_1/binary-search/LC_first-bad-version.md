# [LC_first-bad-version](https://leetcode.com/problems/first-bad-version)

* en

  ```en
  Find first bad version using isBadVersion function
  ```

* tc

  ```tc
  50
  isBadVersion False
  25
  isBadVersion True
  ...
  ```

## Solution

* py

  ```py
  def firstBadVersion(self, n):
    lo, hi = 1, n
    while lo < hi:
      mi = (lo + hi) // 2
      if not isBadVersion(mi):
        lo = mi + 1
      else:
        hi = mi
    return lo
  ```
