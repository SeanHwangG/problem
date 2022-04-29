# [KT_quickestimate](https://open.kattis.com/problems/quickestimate)



```txt
Input: 2
ab
a
Output: 2
1
```

## Solution

* py

```py
n_line = int(input())
for _ in range(n_line):
  x = input()
  print(len(x))
```
