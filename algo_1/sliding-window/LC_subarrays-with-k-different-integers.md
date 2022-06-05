# [LC_subarrays-with-k-different-integers](https://leetcode.com/problems/subarrays-with-k-different-integers)

```en
Given array nums ints, call subarray of nums good if number of different integers in that subarray is exactly k
Return the number of good subarrays of nums.
```

```txt
Input: nums = [1,2,1,2,3], k = 2
Output: 7  # [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Input: nums = [1,2,1,3,4], k = 3
Output: 3  # [1,2,1,3], [2,1,3], [1,3,4].
```

## Solution

* py

  ```py
  def subarraysWithKDistinct(self, A, K):
    return self.atMostK(A, K) - self.atMostK(A, K - 1)

  def atMostK(self, A, K):
    count = collections.Counter()
    res = i = 0
    for j in range(len(A)):
      if count[A[j]] == 0:
        K -= 1
      count[A[j]] += 1
      while K < 0:
        count[A[i]] -= 1
        if count[A[i]] == 0:
          K += 1
        i += 1
      res += j - i + 1
    return res
  ```
