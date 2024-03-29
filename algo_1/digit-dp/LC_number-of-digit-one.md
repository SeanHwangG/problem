# [LC_number-of-digit-one](https://leetcode.com/problems/number-of-digit-one)

* en

  ```en
  Given int n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n
  ```

* tc

  ```tc
  Input: n = 13
  Output: 6         # 1, 10, 11, 12, 13
  ```

## Solution

* cpp

  ```cpp
  int countDigitOne(int n) {
    int ones = 0;
    for (long long m = 1; m <= n; m *= 10)
      ones += (n / m + 8) / 10 * m + (n / m % 10 == 1) * (n % m + 1); // current digit/position being 0, 1
    return ones;
  }
  ```

* Sum out how often a "1" appears at each position
* Given 3141592, when m=1000. Then a=3141 and b=592

* py

  ```py
  def countDigitOne(self, n):
    ones, m = 0, 1
    while m <= n:
      # split 31013
      # 2102 0
      # 2100 4
      # 2100 0
      # 2000 14
      # 10000 0
      ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
      m *= 10
    return ones
  ```
