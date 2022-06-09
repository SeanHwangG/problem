# [LC_number-of-1-bits](https://leetcode.com/problems/number-of-1-bits)

* en

  ```en
  Find number of 1 in binary
  ```

* tc

  ```tc
  Input: n = 00000000000000000000000000001011
  Output: 3
  ```

## Solution

* cpp

  ```cpp
  int hammingWeight(uint32_t n) {
    return __builtin_popcount(n);
  }
  ```

* py

  ```py
  def hammingWeight(self, n: int) -> int:
    return bin(n).count('1')
  ```
