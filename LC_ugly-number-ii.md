{% tabs %}{% tab title='LC_264.cpp' %}

```cpp
int nthUglyNumber(int n) {
  vector<int> ugly(n, 1);
  int c2 = 2, c3 = 3, c5 = 5;
  int i2 = 0, i3 = 0, i5 = 0;
  for (int i=1; i<n; ++i) {
    int last = ugly[i] = min(c2, min(c3, c5));
    while (c2 <= last) c2 = 2 * ugly[++i2];
    while (c3 <= last) c3 = 3 * ugly[++i3];
    while (c5 <= last) c5 = 5 * ugly[++i5];
  }
  return ugly[n-1];
}
```

{% endtab %}{% tab title='LC_264.py' %}

```py
def nthUglyNumber(self, n):
  ugly = [1]
  i2 = i3 = i5 = 0
  while len(ugly) < n:
    while ugly[i2] * 2 <= ugly[-1]: i2 += 1
    while ugly[i3] * 3 <= ugly[-1]: i3 += 1
    while ugly[i5] * 5 <= ugly[-1]: i5 += 1
    ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
  return ugly[-1]
```

{% endtab %}{% endtabs %}