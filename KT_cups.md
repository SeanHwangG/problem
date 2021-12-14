{% tabs %}{% tab title='KT_cups.py' %}

```py
n_line = int(input())
li = []
for _ in range(n_line):
  a, b = input().split()
  if a.isdigit():
    li.append((int(a), b))
  else:
    li.append((int(b) * 2, a))
for _, color in sorted(li):
  print(color)
```

{% endtab %}{% endtabs %}
