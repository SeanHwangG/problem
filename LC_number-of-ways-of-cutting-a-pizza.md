{% tabs %}{% tab title='LC_1444.py' %}

```py
def ways(self, pizza: List[str], K: int) -> int:
  m, n, MOD = len(pizza), len(pizza[0]), 10 ** 9 + 7
  pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
  for r in range(m - 1, -1, -1):
    for c in range(n - 1, -1, -1):
      pre_sum[r][c] = pre_sum[r][c + 1] + pre_sum[r + 1][c] - pre_sum[r + 1][c + 1] + (pizza[r][c] == 'A')

  @lru_cache(None)
  def dp(k, r, c):
    if pre_sum[r][c] == 0: return 0
    if k == 0: return 1
    ans = 0
    for nr in range(r + 1, m): # cut horizontally
      if pre_sum[r][c] - pre_sum[nr][c] > 0:
        ans = (ans + dp(k - 1, nr, c)) % MOD
    for nc in range(c + 1, n): # cut vertically
      if pre_sum[r][c] - pre_sum[r][nc] > 0:
        ans = (ans + dp(k - 1, r, nc)) % MOD
    return ans

  return dp(K - 1, 0, 0)
```

{% endtab %}{% endtabs %}
