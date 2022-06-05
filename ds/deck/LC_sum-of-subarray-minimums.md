# [LC_sum-of-subarray-minimums](https://leetcode.com/problems/sum-of-subarray-minimums)

```en
Given array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr
```

```txt
Input: arr = [3,1,2,4]
Output: 17
```

## Solution

* py

  ```py
  def sumSubarrayMins(self, A):
    res, s = 0, []
    A = [0] + A + [0]
    for i, x in enumerate(A):
      while s and A[s[-1]] > x:
        j = s.pop()
        k = s[-1]
        res += A[j] * (i - j) * (j - k)
      s.append(i)
    return res % (10**9 + 7)
  ```
