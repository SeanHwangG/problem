```java
public int singleNumber(int[] A) {
  int ones = 0, twos = 0;
  for (int i = 0; i < A.length; i++) {
    ones = (ones ^ A[i]) & ~twos;
    twos = (twos ^ A[i]) & ~ones;
  }
  return ones;
}
```

* O(32N)

```py
def singleNumber(self, nums):
  single = 0
  for i in range(32):
    count = 0
    for num in nums:
      if num & (1 << i) == (1 << i):
        count += 1
    single |= (count % 3) << i

  return single if single < (1 << 31) else single - (1 << 32)
```
