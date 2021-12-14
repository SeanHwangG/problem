{% tabs %}{% tab title='LC_735.py' %}

```py
def asteroidCollision(self, asteroids):
  res = []
  for asteroid in asteroids:
    while len(res) and asteroid < 0 and res[-1] > 0:
      if res[-1] == -asteroid:
        res.pop()
        break
      elif res[-1] < -asteroid:
        res.pop()
        continue
      elif res[-1] > -asteroid:
        break
    else:
      res.append(asteroid)
  return res
```

{% endtab %}{% endtabs %}
