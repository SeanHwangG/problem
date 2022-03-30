# [KT_shatteredcake](https://open.kattis.com/problems/shatteredcake)



```txt
Input:
4
7
2 3
1 4
1 2
1 2
2 2
2 2
2 1
Output: 6
```

## Solution

```py
w = int(input())
total = 0
for _ in range(int(input())):
  a, b = map(int, input().split())
  total += a * b
print(total // w)
```
