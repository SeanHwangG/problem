# [LC_length-of-longest-fibonacci-subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence)

* en

  ```en
  Find longest fibonacci subsequence
  ```

* tc

  ```tc
  Input: arr = [1, 3, 7, 11, 12, 14, 18]
  Output: 3
  ```

## Solution

* py

  ```py
  def lenLongestFibSubseq(self, A: List[int]) -> int:
    dp = collections.defaultdict(lambda: 2)
    s = set(A)
    for j in range(len(A)):
      for i in range(j):
        if A[j] - A[i] < A[i] and A[j] - A[i] in s:
          dp[A[i], A[j]] = dp[(A[j] - A[i], A[i])] + 1
    return max(dp.values() or [0])
  ```
