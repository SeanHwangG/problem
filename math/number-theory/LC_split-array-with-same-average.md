# [LC_split-array-with-same-average](https://leetcode.com/problems/split-array-with-same-average)

In a given integer array A, we must move every element of A to either list B or list C
Return if is it possible that average of B is equal to average of C, and B and C are both non-empty

```txt
Input: nums = [1,2,3,4,5,6,7,8]
Output: true  # [1,4,5,8] and [2,3,6,7]
```

## Solution

* py

```py
from statistics import mean
def splitArraySameAverage(self, A):
  @functools.lru_cache()
  def find(target, k, i):
    if k == 0: return target == 0
    if target < 0 or k + i > n: return False
    return find(target - A[i], k - 1, i + 1) or find(target, k, i + 1)
  n, s = len(A), sum(A)
  return any(find(s * k // n, k, 0) for k in range(1, n // 2 + 1) if s * k % n == 0)
```
