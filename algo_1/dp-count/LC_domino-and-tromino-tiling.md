# [LC_domino-and-tromino-tiling](https://leetcode.com/problems/domino-and-tromino-tiling)

Given two types of domino (I and L), find the number of ways to tile 2 * N board

```txt
Input: n = 3
Output: 5
```

## Solution

* cpp

  ```cpp
  int numTilings(int N) {
    int p3 = -1, p2 = 0, p1 = 1;
    for (int n = 1; n <= N; n++) {
      int cur = (p1 * 2L + p3) % int(1e9 + 7);
      p3 = p2;
      p2 = p1;
      p1 = cur;
    }
    return p1;
  }
  ```
