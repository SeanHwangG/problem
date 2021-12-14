{% tabs %}{% tab title='KT_simonsays.py' %}

```py
N = int(input())
for _ in range(N):
  s = input()
  if s[:10] == "Simon says":
    print(s[10:])
```

{% endtab %}{% endtabs %}
