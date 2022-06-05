# [LC_minimum-size-subarray-sum](https://leetcode.com/problems/minimum-size-subarray-sum)

```en
Print minimum length of contiguous subarray sum is greater than target
```

```txt
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
```

## Solution

* py

  ```py
  def minSubArrayLen(self, s, A):
    i, res = 0, len(A) + 1
    for j in xrange(len(A)):
      s -= A[j]
      while s <= 0:
        res = min(res, j - i + 1)
        s += A[i]
        i += 1
    return res % (len(A) + 1)
  ```
