{% tabs %}{% tab title='LC_887.cpp' %}

* Time; O(KlogN)
* Space; O(K)

```cpp
int superEggDrop(int K, int N) {
  vector<int> dp(K + 1, 0);
  int m;
  for (m = 0; dp[K] < N; m++)
    for (int k = K; k > 0; --k)
      dp[k] += dp[k - 1] + 1;
  return m;
}
```

{% endtab %}{% tab title='LC_887.py' %}

```py
def superEggDrop(self, K: int, N: int) -> int:
  dp = [[0] * (K + 1) for i in range(N + 1)]
  for m in range(1, N + 1):
    for k in range(1, K + 1):
      dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
    if dp[m][K] >= N: return m
```

{% endtab %}{% endtabs %}
