```cpp
int maxLengthBetweenEqualCharacters(string s, unordered_map<char, int> m = {}, vector<int> cand = {}) {
  for_each(s.begin(), s.end(), [i = -1, &m](auto c) mutable { m[c] = ++i; });
  transform(s.begin(), s.end(), back_inserter(cand), [i = -1, &m](auto c) mutable { return m[c] - ++i - 1; });
  return *max_element(cand.begin(), cand.end());
}
```

```py
def maxLengthBetweenEqualCharacters(self, s: str) -> int:
  return max(s.rfind(ch) - s.find(ch) - 1 for ch in set(s))
```
