# [KT_bookingaroom](https://open.kattis.com/problems/bookingaroom)



```txt
Input:
100 5
42
3
2
99
1

Output: 23
```

## Solution

* py

```py
a, b = map(int, input().split())
se = set()
for _ in range(b):
  se.add(int(input()))
for i in range(1, a + 1):
  if i not in se:
    print(i)
    break
else:
  print("too late")
```
