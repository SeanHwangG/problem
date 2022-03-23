```py
st = input()
for i, ch in enumerate(st):
  if i == 0 or st[i - 1] == '-':
    print(st[i], end='')
```
