# [LC_minimum-non-zero-product-of-the-array-elements](https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements)

Consider 1-indexed array num that consist of int in inclusive range [1, 2p - 1] in their binary representation
Find Minimum product when you can switch any same position bits of two number, returns in modulo 1e9 + 7

```txt
Input: p = 2
Output: 6  # [01, 10, 11]

Input: p = 3
Output: 1512  # [001, 010, 011, 100, 101, 110, 111]
```

## Solution

* py

  ```py
  def minNonZeroProduct(self, p: int) -> int:
    MOD, mx = int(1e9 + 7), 2 ** p - 1
    return (pow(mx - 1, (mx - 1) // 2, MOD) * (mx)) % MOD
  ```
