```py
st = input()
skip = 0
for ch in st:
  if skip > 0:
    skip -=1
  elif ch in 'aeiou':
    skip = 2
    print(ch, end='')
  else:
    print(ch, end='')
```
