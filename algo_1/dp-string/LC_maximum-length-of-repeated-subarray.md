# [LC_maximum-length-of-repeated-subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray)

* en

  ```en
  Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays
  ```

* tc

  ```tc
  Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
  Output: 3
  ```

## Solution

* py

  ```py
  def findLength(self, A, B):
    dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
      for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
          dp[i][j] = dp[i - 1][j - 1] + 1
    return max(max(row) for row in dp)
  ```
