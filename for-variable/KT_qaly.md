# [KT_qaly](https://open.kattis.com/problems/qaly)



```txt
Input:
2
1 2
3 -2

Output:
2
-6
```

## Solution

```py
n_line = int(input())
ret = 0
for _ in range(n_line):
  a, b = map(float, input().split())
  ret += a * b
print(ret)
```
