# [KT_chanukah](https://open.kattis.com/problems/chanukah)

```en
For each day n light is needed
Determines how many candles would be necessary for a Chanukah holiday lasting for a given number of days
```

```txt
Input:
3
1 8
2 1
3 10

Output:
1 44
2 2
3 65
```

## Solution

* py

  ```py
  n_test = int(input())
  for i in range(n_test):
    t, n = map(int, input().split())
    print(t, n + (n * (n + 1)) // 2)
  ```
