```py
st = input()
for i, c in enumerate(st):
  if i == 0 or st[i - 1] != c:
    print(c, end='')
```
