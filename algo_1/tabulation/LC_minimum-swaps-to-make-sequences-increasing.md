# [LC_minimum-swaps-to-make-sequences-increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing)

* en

  ```en
  We can swap elements A[i] and B[i]
  Find the minimum number of swaps so that A and B are both strictly increasing
  ```

* tc

  ```tc
  Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
  Output: 1
  ```

## Solution

* py

  ```py
  def minSwap(self, A, B):
    N = len(A)
    not_swap, swap = [N] * N, [N] * N
    not_swap[0], swap[0] = 0, 1
    for i in range(1, N):
      if A[i - 1] < A[i] and B[i - 1] < B[i]:
        swap[i] = swap[i - 1] + 1      # Swap at i - 1 and Swap at i
        not_swap[i] = not_swap[i - 1]  # Stay at (i-1) and Stay at i,
      if A[i - 1] < B[i] and B[i - 1] < A[i]:
        swap[i] = min(swap[i], not_swap[i - 1] + 1)  # Swap at i - 1 and stay at i
        not_swap[i] = min(not_swap[i], swap[i - 1])  # Stay at i - 1 and swap at i
    return min(swap[-1], not_swap[-1])
  ```
