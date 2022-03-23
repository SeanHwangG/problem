```py
def findDifferentBinaryString(self, nums: List[str]) -> str:
  return ''.join([str(1 ^ int(num[i])) for i, num in enumerate(nums)])
```
