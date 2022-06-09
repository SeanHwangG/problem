# [LC_toeplitz-matrix](https://leetcode.com/problems/toeplitz-matrix)

* en

  ```en
  Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false
  Matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements
  ```

* tc

  ```tc
  Input:
  matrix =
  [[1,2,3,4],
   [5,1,2,3],
   [9,5,1,2]]

  Output: true
  ```

## Solution

* py

  ```py
  def isToeplitzMatrix(self, m):
    return all(r1[:-1] == r2[1:] for r1, r2 in zip(m, m[1:]))
  ```
