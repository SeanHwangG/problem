# [LC_max-sum-of-rectangle-no-larger-than-k](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k)

Given m x n matrix matrix and integer k, return max sum of a rectangle in matrix ST its sum is no larger than k
It is guaranteed that there will be a rectangle with a sum no larger than k

```txt
Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2

Input: matrix = [[2,2,-1]], k = 3
Output: 3
```

## Solution

* py

  ```py
  from sortedcontainers import SortedList

  def maxSumSubmatrix(self, M, k):
    def countRangeSum(nums, U):
      SList, ans = [0], -float("inf")
      for s in accumulate(nums):
        idx = bisect_left(SList, s - U)
        if idx < len(SList): ans = max(ans, s - SList[idx])
        bisect.insort(SList, s)
      return ans

    m, n, ans = len(M), len(M[0]), -float("inf")

    for i, j in product(range(1, m), range(n)):
      M[i][j] += M[i-1][j]

    M = [[0] * n] + M
    for r1, r2 in combinations(range(m + 1), 2):
      row = [j - i for i, j in zip(M[r1], M[r2])]
      ans = max(ans, countRangeSum(row, k))

    return ans
  ```
