# [KT_cold](https://open.kattis.com/problems/cold)

Print number of negative numbers

```txt
Input: 3
5 -10 15
Output: 1
```

## Solution

* py

  ```py
  input()
  print(len(n for n in map(int, input().split()) if n < 0))
  ```
