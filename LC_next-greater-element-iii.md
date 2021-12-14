{% tabs %}{% tab title='LC_556.cpp' %}

```cpp
int nextGreaterElement(int n) {
  auto digits = to_string(n);
  next_permutation(begin(digits), end(digits));
  auto res = stoll(digits);
  return (res > INT_MAX || res <= n) ? -1 : res;
}
```

{% endtab %}{% endtabs %}
