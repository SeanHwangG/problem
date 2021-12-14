{% tabs %}{% tab title='LC_191.cpp' %}

```cpp
int hammingWeight(uint32_t n) {
  return __builtin_popcount(n);
}
```

{% endtab %}{% tab title='LC_191.py' %}

```py
def hammingWeight(self, n: int) -> int:
  return bin(n).count('1')
```

{% endtab %}{% endtabs %}
