```py
n_test = int(input())
def SSD(b, n):
  ret = 0
  while n != 0:
    ret += (n % b) ** 2
    n //= b
  return ret
for _ in range(1, n_test + 1):
  K, b, n = map(int, input().split())
  print(f'{K} {SSD(b, n)}')
```
