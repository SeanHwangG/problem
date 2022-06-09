# [LC_count-square-submatrices-with-all-ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones)

* en

  ```en
  Given m * n matrix of ones and zeros, return how many square submatrices have all ones
  ```

* tc

  ```tc
  Input: matrix =
  [
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
  ]
  Output: 15

  Input: matrix =
  [
    [1,0,1],
    [1,1,0],
    [1,1,0]
  ]
  Output: 7
  ```

## Solution

* py

  ```py
  def countSquares(self, A):
    for i in xrange(1, len(A)):
      for j in xrange(1, len(A[0])):
        A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1
    return sum(map(sum, A))
  ```
