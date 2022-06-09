# [LC_reverse-integer](https://leetcode.com/problems/reverse-integer)

* en

  ```en
  Reverse integer
  ```

* tc

  ```tc
  Input: 421
  Output:
  124
  ```

## Solution

* cpp

  ```cpp
  int reverse(int x) {
    long r = 0;
    while (x) r = r * 10 + x % 10, x /= 10;
    return (int(r) == r) * r;
  }
  ```
