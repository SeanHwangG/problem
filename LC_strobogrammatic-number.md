```py
def isStrobogrammatic(self, num):
  return set(map(operator.add, num, num[::-1])) <= {'69', '96', '00', '11', '88'}
```
