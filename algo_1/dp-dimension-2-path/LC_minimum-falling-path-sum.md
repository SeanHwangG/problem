# [LC_minimum-falling-path-sum](https://leetcode.com/problems/minimum-falling-path-sum)

* en

  ```en
  Given 2D grid, find minium path sum
  (row, col) can go to (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1)
  ```

* tc

  ```tc
  Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
  Output: 13
  ```

## Solution

* py

  ```py
  def minFallingPathSum(self, A):
    dp = A[0]
    for row in A[1:]:
      dp = [value + min(dp[max(0, c - 1) : c + 2]) for c, value in enumerate(row)]
    return min(dp)
  ```
