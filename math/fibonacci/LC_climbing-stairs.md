# [LC_climbing-stairs](https://leetcode.com/problems/climbing-stairs)

```en
Climbing staircase which takes n steps to reach top
Each time either climb 1 or 2 steps. In how many distinct ways can climb to top?
```

```txt
Input: n = 2
Output: 2
```

## Solution

* go

  ```go
  func climbStairs(n int) int {
    a := 1
    b := 1
    for ; n > 0; n-- {
      a, b = b, a+b
    }
    return a
  }
  ```

* java

  ```java
  public int climbStairs(int n) {
    int a = 1, b = 1;
    while (n-- > 0)
        a = (b += a) - a;
    return a;
  }
  ```

* py

  ```py
  def climbStairs(self, n):
    return int((5 ** .5 / 5) * (((1 + 5 ** .5) / 2) ** (n + 1) - ((1 - 5 ** .5) / 2) ** (n + 1)))
  ```
