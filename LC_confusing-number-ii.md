```py
res = 0
rotate = {'0' : '0', '1' : '1', '6' : '9', '8' : '8', '9' : '6'}
def helper(self, num, rot, N):
  if int(num) > N:
    return

  if num != rot:
    self.res += 1

  for d in self.rotate:
    self.helper(num + d, self.rotate[d] + rot, N)

def confusingNumberII(self, N: int) -> int:
  self.helper('1', '1', N)
  self.helper('6', '9', N)
  self.helper('8', '8', N)
  self.helper('9', '6', N)

  return self.res
```
