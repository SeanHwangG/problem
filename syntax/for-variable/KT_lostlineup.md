# [KT_lostlineup](https://open.kattis.com/problems/lostlineup)



```txt
Input: 4
1 2 0

Output: 1 4 2 3
```

## Solution

```py
n = int(input())
ret = [1] * n
li = list(map(int, input().split()))
for i, n in enumerate(li):
  ret[n + 1] = i + 2
print(*ret)
```
