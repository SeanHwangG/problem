{% tabs %}{% tab title='KT_electricaloutlets.py' %}

```py
for _ in range(int(input())):
  li = list(map(int, input().split()))
  count = sum(li) - 2 * li[0] + 1
  print(count)
```

{% endtab %}{% endtabs %}
