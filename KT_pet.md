{% tabs %}{% tab title='KT_pet.py' %}

```py
num = mx = 0
for i in range(5):
  temp = sum(map(int, input().split()))
  if mx < temp:
    mx = temp
    num = i + 1

print(num, mx)
```

{% endtab %}{% endtabs %}
