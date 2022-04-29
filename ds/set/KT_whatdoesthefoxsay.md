# [KT_whatdoesthefoxsay](https://open.kattis.com/problems/whatdoesthefoxsay)



```txt
Input: 1
toot woof wa ow ow ow pa blub blub pa toot pa blub pa pa ow pow toot
dog goes woof
fish goes blub
elephant goes toot
seal goes ow
what does the fox say?

Output: wa pa pa pa pa pa pow
```

## Solution

* py

```py
n_test = int(input())
for _ in range(n_test):
  li = input().split()
  s = input()
  ignore = set()
  while s != 'what does the fox say?':
    ignore.add(s.split()[-1])
    s = input()
  for e in li:
    if e not in ignore:
      print(e, end=' ')
```
