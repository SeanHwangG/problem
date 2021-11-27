{% tabs %}{% tab title='KT_ostgotska.py' %}

```py
li = input().split()
n = len(li) * 0.4
count = 0
for st in li:
  if "ae" in st:
    count += 1
if n <= count:
  print("dae ae ju traeligt va")
else:
  print("haer talar vi rikssvenska")
```

{% endtab %}{% endtabs %}
