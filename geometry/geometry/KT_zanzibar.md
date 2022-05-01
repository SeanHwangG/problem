# [KT_zanzibar](https://open.kattis.com/problems/zanzibar)

Only double is possible
Print the lower bound for the number of turtles not born on Zanzibar

```txt
Input: 3
1 100 0
1 1 1 2 2 4 8 8 9 0
1 28 72 0

Output: 98
0
42
```

## Solution

* py

  ```py
  n_test = int(input())
  for i in range(n_test):
    li = list(map(int, input().split()))
    ret = 0
    for i in range(1, len(li) - 1):
      ret += max(0, li[i] - li[i - 1] * 2)
    print(ret)

  a, b, c, d = map(int, input().split())
  s = sum([a, b, c, d]) / 2
  print(((s - a) * (s - b) * (s - c) * (s - d)) ** 0.5)
  ```
