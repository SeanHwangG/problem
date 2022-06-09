# [LC_permutation-sequence](https://leetcode.com/problems/permutation-sequence)

* en

  ```en
  Find kth permutation from the set [1, 2, ...]
  ```

* tc

  ```tc
  Input: n = 3, k = 3
  Output: "213"
  ```

## Solution

* py

  ```py
  class Solution:
    def getPermutation(self, n: int, k: int) -> str:
      elements = list(range(1, n+1))
      NN = reduce(operator.mul, elements) # n!
      k, result = (k - 1) % NN, ''
      while len(elements) > 0:
        NN //= len(elements)
        i, k = k // NN, k % NN
        result += str(elements.pop(i))
      return result
  ```
