```cpp
int hammingWeight(uint32_t n) {
  return __builtin_popcount(n);
}
```

```py
def hammingWeight(self, n: int) -> int:
  return bin(n).count('1')
```
