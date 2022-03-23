```py
def countBits(self, num) -> List[int]:
  ret = [0] * (num + 1)
  for i in range(num + 1):
    ret[i] = ret[i // 2] + i % 2
  return ret
```
