{% tabs %}{% tab title='LC_983.cpp' %}

```cpp
int numPermsDISequence(string S) {
  int n = S.length(), mod = 1e9 + 7;
  vector<int> dp(n + 1, 1), dp2(n);
  for (int i = 0; i < n; dp = dp2, i++) {
    if (S[i] == 'I')
      for (int j = 0, cur = 0; j < n - i; j++)
        dp2[j] = cur = (cur + dp[j]) % mod;
    else
      for (int j = n - i - 1, cur = 0; j >= 0; j--)
        dp2[j] = cur = (cur + dp[j + 1]) % mod;
  }
  return dp[0];
}
```

{% endtab %}{% tab title='LC_903.py' %}

* ![LC_903](images/20210727_010921.png)

```py
def numPermsDISequence(self, S):
  dp = [1] * (len(S) + 1)
  for c in S:
    if c == "I":
      dp = dp[:-1]
      for i in range(1, len(dp)):
        dp[i] += dp[i - 1]
    else:
      dp = dp[1:]
      for i in range(len(dp) - 1)[::-1]:
        dp[i] += dp[i + 1]
  return dp[0] % (10**9 + 7)
```

{% endtab %}{% endtabs %}
