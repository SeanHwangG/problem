```py
count = 0
for _ in range(int(input())):
  st = input().lower()
  if 'pink' in st or 'rose' in st:
    count += 1

print(count if count != 0 else "I must watch Star Wars with my daughter")
```