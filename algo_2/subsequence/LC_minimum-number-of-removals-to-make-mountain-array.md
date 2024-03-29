# [LC_minimum-number-of-removals-to-make-mountain-array](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array)

* en

  ```en
  You may recall that an array arr is a mountain array if and only if:
  arr.length >= 3
  There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
  arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
  arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
  Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array
  ```

* tc

  ```tc
  Input: nums = [2,1,1,5,6,2,3,1]
  Output: 3  # 0, 1, 5
  ```

## Solution

* py

  ```py
  def minimumMountainRemovals(self, A: List[int]) -> int:
    n = len(A)
    dp, mono = [0] * n, [10**9] * n
    for i in range(n):
      j = bisect_left(mono, A[i])
      mono[j] = A[i]
      dp[i] += j + 1 if j else -n
    mono = [10**9] * n
    for i in range(n - 1, -1, -1):
      j = bisect_left(mono, A[i])
      mono[j] = A[i]
      dp[i] += j if j else -n
    return n - max(dp[1:-1])
  ```
