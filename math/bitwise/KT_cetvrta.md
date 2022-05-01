# [KT_cetvrta](https://open.kattis.com/problems/cetvrta)

Given coordinate of three corners of rectangle, find the last corner

```txt
Input:
1 3
2 3
2 5

Output: 1 5
```

## Solution

* py

  ```py
  x1, y1 = map(int, input().split())
  x2, y2 = map(int, input().split())
  x3, y3 = map(int, input().split())
  print(x1 ^ x2 ^ x3, y1 ^ y2 ^ y3)
  ```
