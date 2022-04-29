# [KT_reverserot](https://open.kattis.com/problems/reverserot)



```txt
Input: 1 ABCD
3 YO_THERE.
1 .DOT
14 ROAD
9 SHIFTING_AND_ROTATING_IS_NOT_ENCRYPTING
2 STRING_TO_BE_CONVERTED
1 SNQZDRQDUDQ
0
Output:
EDCB
CHUHKWBR.
UPEA
ROAD
PWRAYF_LWNHAXWH.RHPWRAJAX_HMWJHPWRAORQ.
FGVTGXPQEAGDAQVAIPKTVU
REVERSE_ROT
```

## Solution

* py

```py
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
  raw = input()
  if raw == '0':
    break
  shift, st = raw.split()
  shift = int(shift)
  for ch in reversed(st):
    print(alp[(alp.find(ch) + shift) % len(alp)], end='')
  print()
```
