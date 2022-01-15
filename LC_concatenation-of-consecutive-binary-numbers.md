{% tabs %}{% tab title='LC_1680.cpp' %}

```cpp
int concatenatedBinary(int n) {
  long ans = 0, mod = 1e9+7, len = 0;
  for (int i = 1; i <= n; ++i) {
    if ((i & (i - 1)) == 0) ++len;
    ans = ((ans << len) % mod + i) % mod;
  }
  return ans;
}
```

{% tab title='LC_1680.py' %}
{% endtab %}

```py
def concatenatedBinary(self, n: int) -> int:
  ans, l, MOD = 0, 0, 10 ** 9 + 7
  for x in range(1, n + 1):
    if x & (-x) == x: l += 1
    ans = (ans * (1 << l) + x) % MOD
  return ans
```

{% endtab %}{% endtabs %}
