# [KT_avion](https://open.kattis.com/problems/avion)



```txt
Input:
N-FBI1
9A-USKOK
I-NTERPOL
G-MI6
RF-KGB1

Output: 1
```

## Solution

```py
seen = False
for i in range(1, 6):
  st = input()
  if 'FBI' in st:
    print(i, end=' ')
    seen = True

if not seen:
  print("HE GOT AWAY!")
```
