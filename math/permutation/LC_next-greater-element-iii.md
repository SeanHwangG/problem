# [LC_next-greater-element-iii](https://leetcode.com/problems/next-greater-element-iii)

```en
Given positive integer n, find smallest int which has same digits existing in integer n, greater in value than n
If no such positive integer exists, return -1
Note that returned integer should fit in 32-bit integer, if valid answer does not fit in 32-bit integer, return -1.
```

```txt
Input: n = 12
Output: 21

Input: n = 21
Output: -1
```

## Solution

* cpp

  ```cpp
  int nextGreaterElement(int n) {
    auto digits = to_string(n);
    next_permutation(begin(digits), end(digits));
    auto res = stoll(digits);
    return (res > INT_MAX || res <= n) ? -1 : res;
  }
  ```
