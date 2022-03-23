```cpp
bool repeatedSubstringPattern(string s) {
  return (s + s).find(s, 1) < s.size();
}
```

```py
def repeatedSubstringPattern(self, s: str) -> bool:
  return s in (2 * s)[1:-1]
```
