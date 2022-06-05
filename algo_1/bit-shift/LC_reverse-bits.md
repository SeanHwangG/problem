# [LC_reverse-bits](https://leetcode.com/problems/reverse-bits)

```en
Reverse bits of a given 32 bits unsigned integer
```

```txt
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
```

## Solution

* cpp

  ```cpp
  uint32_t reverseBits(uint32_t n) {
    n = (n >> 16) | (n << 16);
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
    n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
    n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
    n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
    return n;
  }
  ```

* py

  ```py
  class Solution:
    def reverseBits(self, n):
      return int(bin(n)[:1:-1].ljust(32, '0'), 2)
  ```
