{% tabs %}{% tab title='HR_matching-same-text-again-again.py' %}

```py
import re

pattern = r'^([a-z]\w\s\W\d\D[A-Z][a-z,A-Z][aieouAEIOU]\S)\1$'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}{% endtabs %}
