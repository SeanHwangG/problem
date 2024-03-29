# [LC_ugly-number-ii](https://leetcode.com/problems/ugly-number-ii)

* en

  ```en
  Given an integer n, return the nth ugly number
  Ugly number is a positive number whose prime factors only include 2, 3, and/or 5
  ```

* tc

  ```tc
  Input: n = 10
  Output: 12 # [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
  ```

## Solution

* cpp

  ```cpp
  int nthUglyNumber(int n) {
    vector<int> ugly(n, 1);
    int c2 = 2, c3 = 3, c5 = 5;
    int i2 = 0, i3 = 0, i5 = 0;
    for (int i=1; i<n; ++i) {
      int last = ugly[i] = min(c2, min(c3, c5));
      while (c2 <= last) c2 = 2 * ugly[++i2];
      while (c3 <= last) c3 = 3 * ugly[++i3];
      while (c5 <= last) c5 = 5 * ugly[++i5];
    }
    return ugly[n-1];
  }
  ```

* py

  ```py
  def nthUglyNumber(self, n):
    ugly = [1]
    i2 = i3 = i5 = 0
    while len(ugly) < n:
      while ugly[i2] * 2 <= ugly[-1]: i2 += 1
      while ugly[i3] * 3 <= ugly[-1]: i3 += 1
      while ugly[i5] * 5 <= ugly[-1]: i5 += 1
      ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]
  ```
