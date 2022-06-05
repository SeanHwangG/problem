# [LC_available-captures-for-rook](https://leetcode.com/problems/available-captures-for-rook)

```en
Print a + b
```

```txt
Input: 1 2
Output: 3
```

## Solution

* py

  ```py
  def numRookCaptures(self, A):
    return sum(''.join(r).replace('.', '').count('Rp') for r in A + zip(*A) for r in [r, r[::-1]])
  ```
