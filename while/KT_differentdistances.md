```py
while True:
  raw = input()
  if raw == '0':
    break
  a, b, c, d, e = map(float, raw.split())
  print((abs(a - c) ** e + abs(b - d) ** e) ** (1/e))
```
