{% tabs %}{% tab title='KT_pokerhand.py' %}

```py
from collections import Counter
cnter = Counter()
for card in input().split():
  cnter[card[0]]+=1
print(cnter.most_common(1)[0][1])
```

{% endtab %}{% endtabs %}
