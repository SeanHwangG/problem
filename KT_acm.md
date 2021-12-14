{% tabs %}{% tab title='KT_acm.py' %}

```py
from collections import Counter
total_score = total_time = 0
penalty = Counter()
while True:
  st = input()
  if st == '-1':
    break
  t, prob, result = st.split()
  t = int(t)

  if result == 'wrong':
    penalty[prob] += 20
  elif result == 'right':
    total_time += t + penalty[prob]
    total_score += 1

print(total_score, total_time)
```

{% endtab %}{% endtabs %}
