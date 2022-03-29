```py
add = int(input())
n_line = int(input())
cur = 0
for n in range(n_line):
  cur += add
  cur = max(0, cur - int(input()))
print(cur + add)
```
