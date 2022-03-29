```py
s = input()
chunk = len(s) // 3
a = s[:chunk]
b = s[chunk:chunk * 2]
c = s[chunk * 2:]
if b == c:
  print(b)
else:
  print(a)
```
