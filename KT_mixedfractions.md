```py
while True:
  dem, num = map(int, input().split())
  if dem == num == 0:
    break
  print(dem // num, dem % num, '/', num)
```
