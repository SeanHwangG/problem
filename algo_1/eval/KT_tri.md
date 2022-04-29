# [KT_tri](https://open.kattis.com/problems/tri)



```txt
Input: 5 3 8
Output: 5+3=8

Input: 2 2 4
Output: 2*2=4  # can be 2+2=4
```

## Solution

* py

```py
a, b, c = input().split()
for op in ['+', '-', '*', '/']:
  if eval(a + op + b) == int(c):
    print(a + op + b + '=' + c)
    break
  if int(a) == eval(b + op + c):
    print(a + '=' + b + op + c)
    break
```
