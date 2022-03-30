# [KT_helpaphd](https://open.kattis.com/problems/helpaphd)



```txt
Input: 4
2+2
1+2
P=NP
0+0
Output: 4
3
skipped
0
```

## Solution

```py
n_test = int(input())
for _ in range(n_test):
  line = input()
  if line == 'P=NP':
    print('skipped')
  else:
    print(eval(line))
```
