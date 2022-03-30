# [KT_lastfactorialdigit](https://open.kattis.com/problems/lastfactorialdigit)

Print last digit of factorial

```txt
Input: 3
1
2
3

Output: 1
2
6
```

## Solution

```py
n_test = int(input())
for _ in range(n_test):
  n = int(input())
  ret = 1
  for i in range(1, n + 1):
    ret *= i
  print(ret % 10)
```
