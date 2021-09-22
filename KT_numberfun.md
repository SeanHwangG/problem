{% tabs %}{% tab title='KT_numberfun.py' %}

```py
n_test = int(input())
for _ in range(n_test):
  a, b, c = map(int, input().split())
  if a + b == c or a - b == c or b - a == c or a * b == c or a / b == c or b / a == c:
    print("Possible")
  else:
    print("Impossible")
```

{% endtab %}{% endtabs %}
