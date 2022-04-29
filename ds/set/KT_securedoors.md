# [KT_securedoors](https://open.kattis.com/problems/securedoors)



```txt
Input:
8
entry Abbey
entry Abbey
exit Abbey
entry Tyrone
exit Mason
entry Demetra
exit Latonya
entry Idella

Output:
Abbey entered
Abbey entered (ANOMALY)
Abbey exited
Tyrone entered
Mason exited (ANOMALY)
Demetra entered
Latonya exited (ANOMALY)
Idella entered
```

## Solution

* py

```py
N = int(input())
se = set()
for _ in range(N):
  typ, name = input().split()
  if typ == 'entry':
    if name in se:
      print(name, 'entered', '(ANOMALY)')
    else:
      print(name, 'entered')
      se.add(name)
  else:
    if name in se:
      print(name, 'exited')
      se.remove(name)
    else:
      print(name, 'exited', ('(ANOMALY)' if name not in se else ''))
```
