# [KT_onechicken](https://open.kattis.com/problems/onechicken)



```txt
Input: 20 100
Output: Dr. Chaz will have 80 pieces of chicken left over!
```

## Solution

```py
a, b = map(int, input().split())
if a < b:
  print(f"Dr. Chaz will have {b - a} piece{'' if b - a == 1 else 's'} of chicken left over!")
else:
  print(f"Dr. Chaz needs {a - b} more piece{'' if a - b == 1 else 's'} of chicken!")
```
