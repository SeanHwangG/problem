{% tabs %}{% tab title='KT_exam.py' %}

```py
correct = int(input())
my = input()
fr = input()
total = len(my)
same = 0
for m, f in zip(my, fr):
  if m == f:
    same += 1

if same > correct:
  print(correct + (total - same))
else:
  print(same + (total - correct))
```

{% endtab %}{% endtabs %}
