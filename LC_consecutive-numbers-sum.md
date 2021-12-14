{% tabs %}{% tab title='LC_829.cpp' %}

* $$ Σ_{i=2}^{N+1} = Σ_{i=1}^{N} + N $$
* Log(N)

```cpp
int consecutiveNumbersSum(int N, int res = 0) {
  for (auto n = 2; n * (n + 1) / 2 <= N; ++n)
    res += (N - n * (n + 1) / 2) % n == 0? 1 : 0;
  return res + 1;
}
```

{% endtab %}{% tab title='LC_829.py' %}

* Log(N)

```py
def consecutiveNumbersSum(self, n):
  res = 1
  for i in range(2, math.ceil((1 + (1 + 8 * n) ** 0.5) / 2)):
    if ((n / i) - (i - 1)/2).is_integer():
      res += 1
  return res
```

{% endtab %}{% endtabs %}
