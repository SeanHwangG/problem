```py
s = input()
A = B = 0
for i in range(1, len(s), 2):
  if s[i - 1] == 'A':
    A += int(s[i])
  else:
    B += int(s[i])
if A > B:
  print('A')
else:
  print('B')
```
