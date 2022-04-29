# [KT_zamka](https://open.kattis.com/problems/zamka)

Determine minimal integer N such that L≤N≤D and sum of its digits is X
Determine maximal integer M such that L≤M≤D and sum of its digits is X

```txt
Input: 1
100
4
Output:
4
40
```

## Solution

* py

```py
mn = int(input())
mx = int(input())
sm = int(input())
def match(n, sm):
  while n != 0:
    sm -= n % 10
    n //= 10
  return sm == 0
for i in range(mn, mx + 1):
  if match(i, sm):
    print(i)
    break
for i in range(mx, mn - 1, -1):
  if match(i, sm):
    print(i)
    break
```
