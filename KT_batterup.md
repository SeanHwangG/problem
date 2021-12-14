{% tabs %}{% tab title='KT_batterup.py' %}

```py
n_hit = int(input())
li = list(map(int, input().split()))
miss = li.count(-1)
print((sum(li) + miss) / (n_hit - miss))
```

{% endtab %}{% endtabs %}
