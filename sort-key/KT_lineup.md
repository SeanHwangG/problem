# [KT_lineup](https://open.kattis.com/problems/lineup)



```txt
Input:
5
JOE
BOB
ANDY
AL
ADAM

Output: DECREASING
```

## Solution

```py
n = int(input())
li = []
for _ in range(n):
  li.append(input())
if li == sorted(li):
  print("INCREASING")
elif li == sorted(li, reverse=True):
  print('DECREASING')
else:
  print('NEITHER')
```
