# [LC_n-queens-ii](https://leetcode.com/problems/n-queens-ii)

Given integer n, return the number of distinct solutions to the n-queens puzzle

```txt
Input: n = 4
Output: 2
```

## Solution

* py

  ```py
  def totalNQueens(self, n: int, queens=[], d1=[], d2=[]) -> int:
    i = len(queens)
    return (i == n) + sum(self.totalNQueens(n, queens+[j], d1+[j-i], d2+[j+i]) for j in range(n) \
                if j not in queens and j - i not in d1 and j + i not in d2)
  ```
