# [KT_savingforretirement](https://open.kattis.com/problems/savingforretirement)



```txt
Input: 20 25 5 20 10
Output: 23
```

## Solution

* py

```py
a, b, c, d, e = map(int, input().split())
print(d + (b - a) * c // e + 1)
```
