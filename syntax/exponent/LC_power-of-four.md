# [LC_power-of-four](https://leetcode.com/problems/power-of-four)

* en

  ```en
  Print if power if 4
  ```

* tc

  ```tc
  Input: 16
  Output: True
  ```

## Solution

* cpp

  ```cpp
  // (4^n - 1) % 3 == 0
  // 4^n - 1 = (2^n + 1) * (2^n - 1) one  must be a multiple of 3
  bool isPowerOfFour(int num) {
    return num > 0 && (num & (num - 1)) == 0 && (num - 1) % 3 == 0;
  }
  ```

* py

  ```py
  def isPowerOfFour(self, num: int) -> bool:
    return num > 0 and num & (num - 1) == 0 and (num - 1) % 3 == 0
  ```
