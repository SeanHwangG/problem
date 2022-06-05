# [LC_power-of-two](https://leetcode.com/problems/power-of-two)

```en
Check if power of 2
```

```txt
Input: 8
Output: True
```

## Solution

* py

  ```py
  def isPowerOfTwo(self, n):
    return n > 0 and not (n & n-1)
  ```
