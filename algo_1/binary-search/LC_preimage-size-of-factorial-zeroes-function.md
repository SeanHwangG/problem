# [LC_preimage-size-of-factorial-zeroes-function](https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function)

```en
Let f(x) be the number of zeroes at the end of x!
Given an integer k, return the number of non-negative integers x have the property that f(x) = k.
```

```txt
Input: k = 0
Output: 5 # 0!, 1!, 2!, 3!, and 4! end with k = 0 zeroes.

Input: k = 5
Output: 0
```

## Solution

* py

  ```py
  def preimageSizeFZF(self, K):
    def f(x):
      return 0 if x < 5 else f(x // 5) + x // 5
    l, r = 0, 5 * (K + 1)
    while l < r:
      m = (r - l) // 2 + l
      if f(m) < K:
        l = m + 1
      else:
        r = m
    return 5 if f(l) == K else 0
  ```
