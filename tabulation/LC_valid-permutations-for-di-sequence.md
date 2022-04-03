# [LC_valid-permutations-for-di-sequence](https://leetcode.com/problems/valid-permutations-for-di-sequence)

Given s, a length n string of characters from the set {'D', 'I'}. (stand for "decreasing" and "increasing".)
Count permutation p[0], p[1], ..., p[n] of integers {0, 1, ..., n}, such that for all i:
  If s[i] == 'D', then p[i] > p[i+1], and;
  If s[i] == 'I', then p[i] < p[i+1

```txt
Input: s = "DID"
Output: 5   # (1, 0, 3 2) ...
```

## Solution

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
