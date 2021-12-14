{% tabs %}{% tab title='HR_matching-one-or-more-repititions.py' %}

```py
import re
pattern = r'^\d+[A-Z]+[a-z]+$'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}{% endtabs %}
