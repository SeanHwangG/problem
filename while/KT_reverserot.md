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
