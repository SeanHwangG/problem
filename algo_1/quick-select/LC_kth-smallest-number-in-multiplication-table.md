# [LC_kth-smallest-number-in-multiplication-table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table)

```en
Multiplication table of size m x n is integer matrix mat where mat[i][j] == i * j (1-indexed)
Given three integers m, n, and k, return kth smallest element in the m x n multiplication table
```

```txt
Input: m = 3, n = 3, k = 5
Output: 3  # 1, 2, 2, 3, 3
```

## Solution

* py

  ```py
  def findKthNumber(self, m, n, k):
    def enough(x):
      return sum(min(x // i, n) for i in range(1, m + 1)) >= k

    lo, hi = 1, m * n
    while lo < hi:
      mi = (lo + hi) // 2
      if not enough(mi):
        lo = mi + 1
      else:
        hi = mi
    return lo
  ```
