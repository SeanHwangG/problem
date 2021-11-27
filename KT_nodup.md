{% tabs %}{% tab title='KT_nodup.py' %}

```py
li = input().split()
print("yes" if len(set(li)) == len(li) else "no")
```

{% endtab %}{% endtabs %}
