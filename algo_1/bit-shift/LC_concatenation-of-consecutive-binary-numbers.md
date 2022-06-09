# [LC_concatenation-of-consecutive-binary-numbers](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers)

* en

  ```en
  Given n, return decimal value of binary string formed by concatenating binary of 1 to n in order, modulo 10**9 + 7
  ```

* tc

  ```tc
  Input: n = 3
  Output: 27   # 11011
  ```

## Solution

* cpp

  ```cpp
  int concatenatedBinary(int n) {
    long ans = 0, mod = 1e9+7, len = 0;
    for (int i = 1; i <= n; ++i) {
      if ((i & (i - 1)) == 0) ++len;
      ans = ((ans << len) % mod + i) % mod;
    }
    return ans;
  }
  ```

* py

  ```py
  def concatenatedBinary(self, n: int) -> int:
    ans, l, MOD = 0, 0, 10 ** 9 + 7
    for x in range(1, n + 1):
      if x & (-x) == x: l += 1
      ans = (ans * (1 << l) + x) % MOD
    return ans
  ```
