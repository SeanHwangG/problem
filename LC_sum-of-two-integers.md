{% tabs %}{% tab title='LC_371.cpp' %}

```cpp
int getSum(int a, int b) {
  return b == 0? a: getSum(a ^ b, (a & b) << 1); // Be careful about the terminating condition;
}
```

{% endtab %}{% endtabs %}