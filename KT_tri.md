{% tabs %}{% tab title='KT_tri.py' %}

```py
a, b, c = input().split()
for op in ['+', '-', '*', '/']:
  if eval(a + op + b) == int(c):
    print(a + op + b + '=' + c)
    break
  if int(a) == eval(b + op + c):
    print(a + '=' + b + op + c)
    break
```

{% endtab %}{% endtabs %}
