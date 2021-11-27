{% tabs %}{% tab title='KT_bookingaroom.py' %}

```py
a, b = map(int, input().split())
se = set()
for _ in range(b):
  se.add(int(input()))
for i in range(1, a + 1):
  if i not in se:
    print(i)
    break
else:
  print("too late")
```

{% endtab %}{% endtabs %}
