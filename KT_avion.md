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
