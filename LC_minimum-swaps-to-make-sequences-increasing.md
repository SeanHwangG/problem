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
