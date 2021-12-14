{% tabs %}{% tab title='KT_dicegame.py' %}

```py
a = sum(map(int, input().split()))
b = sum(map(int, input().split()))
if a < b:
  print('Emma')
elif b < a:
  print('Gunnar')
else:
  print('Tie')
```

{% endtab %}{% endtabs %}
