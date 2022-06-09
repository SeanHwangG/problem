# [LC_k-th-smallest-prime-fraction](https://leetcode.com/problems/k-th-smallest-prime-fraction)

* en

  ```en
  Given sorted int array arr containing 1 and prime numbers, where all the integers of arr are unique, and int k
  For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j]
  Return kth smallest fraction considered. Return array of ints of size 2, where answer[0] == arr[i], answer[1] == arr[j]

  ```

* tc

  ```tc
  Input: arr = [1,2,3,5], k = 3
  Output: [2,5]

  ```

## Solution

* py

  ```py
  def kthSmallestPrimeFraction(self, A, K):
    def kthSmallest(matrix, k):
      # Can be improved from LC_378
      return sorted(itertools.chain(*matrix))[k - 1]
    class Row(int):
      def __getitem__(self, j):
        return float(self) / A[~j], [int(self), A[~j]]
    return kthSmallest(map(Row, A), K)[1]
  ```
