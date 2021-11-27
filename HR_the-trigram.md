{% tabs %}{% tab title='HR_the-trigram.py' %}

```py
import sys
from collections import Counter
from functools import reduce
from operator import iconcat

def getTrigrams(sentence):
  words = sentence.split()
  return [" ".join(words[i:i+3]) for i in range(len(words)-2)]

txt = sys.stdin.read()
trigrams = Counter(reduce(iconcat, map(getTrigrams, txt.lower().split('.')), []))
print(max(trigrams, key=trigrams.get))
```

{% endtab %}{% endtabs %}
