{% tabs %}{% tab title='HR_find-a-word.py' %}

```py
import re

sentence = ' '.join(input() for _ in range(int(input())))
for _ in range(int(input())):
  print(len(re.findall(fr'\b{input()}\b', sentence)))
```

{% endtab %}{% endtabs %}
