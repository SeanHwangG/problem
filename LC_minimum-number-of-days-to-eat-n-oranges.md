```cpp
unordered_map<int, int> dp;
int minDays(int n) {
  if (n <= 1)
    return n;
  if (dp.count(n) == 0)
    dp[n] = 1 + min(n % 2 + minDays(n / 2), n % 3 + minDays(n / 3));
  return dp[n];
}
```

```py
@lru_cache()
def minDays(self, n: int) -> int:
  if n <= 1:
    return n
  return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))
```
