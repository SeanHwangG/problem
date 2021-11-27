{% tabs %}{% tab title='LC_459.cpp' %}

```cpp
bool repeatedSubstringPattern(string s) {
  return (s + s).find(s, 1) < s.size();
}
```

{% endtab %}{% tab title='LC_459.py' %}

```py
def repeatedSubstringPattern(self, s: str) -> bool:
  return s in (2 * s)[1:-1]
```

{% endtab %}{% endtabs %}
