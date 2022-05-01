# [LC_remove-9](https://leetcode.com/problems/remove-9)

Start from integer 1, remove any integer that contains 9 such as 9, 19, 29...
So now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...
Given a positive integer n, you need to return the n-th integer after removing

```txt
Input: 9
Output: 10
```

## Solution

* py

  ```py
  import numpy
  def newInteger(self, n):
    return int(numpy.base_repr(n, 9))
  ```
