{% tabs %}{% tab title='LC_1525.md' %}

* Given string s, a split is called good if can split s into 2 non-empty strings p and q
  * Where its concatenation is equal to s and the number of distinct letters in p and q are the same
* Return # good splits you can make in s.

```txt
Input: s = "aacaba"
Output: 2

Input: s = "abcd"  # ("ab", "cd")
Output: 1

Input: s = "aaaaa"
Output: 4
```

{% endtab %}{% tab title='LC_1525.py' %}

```py
def numSplits(self, s: str) -> int:
  lc, rc = Counter(), Counter(s)
  res = 0
  for c in s:
    lc[c] += 1
    rc[c] -= 1
    if rc[c] == 0:
      del rc[c]

    if len(lc) == len(rc):
      res += 1

  return res
```

{% endtab %}{% endtabs %}
