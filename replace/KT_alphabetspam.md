```py
st = input()
white = 0
lower = 0
upper = 0
symbol = 0
for ch in st:
  if ch == '_':
    white += 1
  elif ch.islower():
    lower += 1
  elif ch.isupper():
    upper += 1
  else:
    symbol += 1

total = white + lower + upper + symbol
print(white / total)
print(lower / total)
print(upper / total)
print(symbol / total)
```
