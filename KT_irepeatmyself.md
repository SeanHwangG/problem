{% tabs %}{% tab title='KT_irepeatmyself.py' %}

```py
def shortest_pattern(sentence):
  n = len(sentence)
  for i in range(1, n + 1):
    if (sentence[:i] * (n // i + 1))[:n] == sentence:
      return i
  return n

N = int(input())
for i in range(N):
  sent = input()
  print(shortest_pattern(sent))
```

{% endtab %}{% endtabs %}
