{% tabs %}{% tab title='HR_matching-ending-items.py' %}

```py
import re
pattern = r'^[a-zA-Z]*s$'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}{% endtabs %}
