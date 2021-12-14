{% tabs %}{% tab title='LC_242.cpp' %}

```cpp
bool isAnagram(string s, string t) {
  return unordered_multiset<char>(begin(s), end(s)) == unordered_multiset<char>(begin(t), end(t));
}
```

{% endtab %}{% endtabs %}
