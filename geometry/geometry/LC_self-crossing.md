# [LC_self-crossing](https://leetcode.com/problems/self-crossing)

```en
Check if line is self crossing
```

```txt
Input: distance = [2,1,1,2]
Output: true
```

## Solution

* py

  ```py
  def isSelfCrossing(self, x):
    """ Two cases
                      b                              b
    +----------------+             +----------------+
    |                |             |                |
    |                |             |                | a
  c |                |           c |                |
    |                | a           |                |    f
    +----------->    |             |                | <----+
              d       |             |                |      | e
                      |             |                       |
                                    +-----------------------+
                                                d
    """
    b = c = d = e = 0
    for a in x:
      if d >= b > 0 and (a >= c or a >= c - e >= 0 and b + f >= d):
        return True
      b, c, d, e, f = a, b, c, d, e
    return False
  ```
