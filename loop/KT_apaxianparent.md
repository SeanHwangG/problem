# [KT_apaxianparent](https://open.kattis.com/problems/apaxianparent)



```txt
Input: menolaxios mox
Output: menolaxiosexmox
```

## Solution

```py
a, b = input().split()
if a[-1] == 'e':
  print(a, 'x', b, sep='')
elif a[-2:] == 'ex':
  print(a, b, sep='')
elif a[-1] in 'aiou':
  print(a[:-1], 'ex', b, sep='')
else:
  print(a, 'ex', b, sep='')
```
