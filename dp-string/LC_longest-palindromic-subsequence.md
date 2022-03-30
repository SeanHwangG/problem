# [LC_longest-palindromic-subsequence](https://leetcode.com/problems/longest-palindromic-subsequence)

Given a string s, find the longest palindromic subsequence's length in s

```txt
Input: s = "(()"
Output: 2

```

## Solution

* Time, Space; O(N^2), O(N)

```cpp
int longestPalindromeSubseq(string s) {
  vector<int> dp(s.size(), 1);
  for (int j = 0; j < s.size(); ++j) {
    int prev = 0;
    for (int i = j - 1; i >= 0; --i) {
      int tmp = dp[i];
      if (s[i] == s[j]) dp[i] = 2 + prev;
      else              dp[i] = max(dp[i + 1], dp[i]);
      prev = tmp;
    }
  }
  return dp[0];
}
```

```py
# Time, Space O(N^2), O(N^2)
@lru_cache(None)
def longestPalindromeSubseq(self, s):
  recurse = lambda i, j: 1 if i == j else 2 + self.longestPalindromeSubseq(s[i+1:j])
  return max((recurse(s.find(ch), s.rfind(ch)) for ch in set(s)), default=0)
```
