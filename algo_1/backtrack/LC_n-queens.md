# [LC_n-queens](https://leetcode.com/problems/n-queens)

* en

  ```en
  Return all answer for NQueen
  ```

* tc

  ```tc
  Input: n = 4
  Output:
  [[".Q..","...Q","Q...","..Q."],
   ["..Q.","Q...","...Q",".Q.."]]
  ```

## Solution

* py

  ```py
  def solveNQueens(self, n):
    def DFS(queens, xy_dif, xy_sum):
      p = len(queens)
      if p==n:
        result.append(queens)
        return
      for q in range(n):
        if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
          DFS(queens+[q], xy_dif+[p - q], xy_sum+[p+q])
    result = []
    DFS([], [], [])
    return [["." * i + "Q" + "." * (n-i-1) for i in sol] for sol in result]
  ```
