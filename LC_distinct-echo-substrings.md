{% tabs %}{% tab title='LC_1316.md' %}

* Return number of distinct non-empty substrings of text that can be written as concatenation of some string with itself

```txt
Input: text = "abcabcabc"
Output: 3  # "abcabc", "bcabca" and "cabcab".
```

{% endtab %}{% tab title='LC_1316.cpp' %}

```cpp
int distinctEchoSubstrings(string text) {
  int N = text.size();
  int MOD = 1000000007;
  unordered_set<string> distinct;

  /* rh[i][l] = rolling hash of substring starting at i with length l */
  vector<vector<int>> rh(N, vector<int>(N+1, 0));

  for (int l = 1; l <= N ; ++l) {
    for (int i = 0 ; i + l <= N ; ++i) {
      /* Build rh[i][l] on rh[i][l-1] and current character. */
      rh[i][l] = (rh[i][l-1] + text[i + l - 1]) % MOD;

      /* Check if previous adjacent substring of same length matches */
      if (i >= l && rh[i - l][l] == rh[i][l]) { //rh matches
        string sub = text.substr(i, l);

        /* Check if not found and actual character by character match */
        if (distinct.find(sub) == distinct.end() && sub == text.substr(i - l, l))
          distinct.emplace(sub);
      }
    }
  }
  return distinct.size();
}
```

{% endtab %}{% tab title='LC_1316.py' %}

```py
def distinctEchoSubstrings(self, s):
  s += '.'
  se = set()
  for k in range(1, len(s) // 2 + 1):
    same = sum(c == d for c, d in zip(s, s[k: k + k]))
    for i in range(len(s) - 2 * k + 1):
      if same == k:
        se.add(s[i: i + k])
      same += (s[i + k] == s[i + k + k]) - (s[i] == s[i + k])
  return len(se)
```

{% endtab %}{% endtabs %}
