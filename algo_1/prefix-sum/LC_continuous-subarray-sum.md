# [LC_continuous-subarray-sum](https://leetcode.com/problems/continuous-subarray-sum)

* en

  ```en
  Given int array nums and an integer k
  Return if nums has a continuous subarray of size at least two whose elements sum up to multiple of k
  ```

* tc

  ```tc
  Input: nums = [23,2,4,6,7], k = 6
  Output: true
  ```

## Solution

* Time, Space; O(N), O(N)

* py

  ```py
  def checkSubarraySum(self, A, k):
    seen, cur = {0: -1}, 0
    for i, a in enumerate(A):
      cur = (cur + a) % abs(k) if k else cur + a
      if i - seen.setdefault(cur, i) > 1:
        return True
    return False
  ```
