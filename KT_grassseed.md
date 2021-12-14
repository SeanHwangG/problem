{% tabs %}{% tab title='KT_grassseed.py' %}

```py
c = float(input())
l = int(input())
ret = 0
for _ in range(l):
  w, l = map(float, input().split())
  ret += w * l * c
print(ret)
```

{% endtab %}{% endtabs %}
