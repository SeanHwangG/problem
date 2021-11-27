{% tabs %}{% tab title='LC_1967.cpp' %}

```cpp
int numOfStrings(vector<string>& ps, string word) {
  return count_if(begin(ps), end(ps), [&](const auto &p) { return word.find(p) != string::npos; });
}
```

{% endtab %}{% tab title='LC_1967.py' %}

```py
def numOfStrings(self, patterns: List[str], word: str) -> int:
  return sum(x in word for x in patterns)
```

{% endtab %}{% endtabs %}
