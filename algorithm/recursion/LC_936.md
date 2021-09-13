{% tabs %}{% tab title='LC_936.md' %}

* Convert s to target using at most 10 x target.length turns
* In one turn, place stamp over s and replace every letter in the s with the corresponding letter from stamp
* Return array of index of left-most letter being stamped at each turn, if cannot obtain target, return empty array

```txt
Input: stamp = "abc", target = "ababc"
Output: [0,2]  # abc?? -> ababc

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
```

{% endtab %}{% tab title='LC_936.py' %}

```py
def movesToStamp(self, s: str, t: str) -> List[int]:
  n, m, t, s, res = len(t), len(s), list(t), list(s), []

  def check(i):
    changed = False
    for j in range(m):
      if t[i + j] == '?': continue
      if t[i + j] != s[j]: return False
      changed = True
    if changed:
      t[i:i + m] = ['?'] * m
      res.append(i)
    return changed

  changed = True
  while changed:
    changed = False
    for i in range(n - m + 1):
      changed |= check(i)
  return res[::-1] if t == ['?'] * n else []
```

{% endtab %}{% endtabs %}
