{% tabs %}{% tab title='HR_matching-zero-or-more-repetitions.py' %}

```py
import re
pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}{% endtabs %}
