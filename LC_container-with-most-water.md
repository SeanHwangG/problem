{% tabs %}{% tab title='LC_11.py' %}

```py
def maxArea(self, height):
  i, j = 0, len(height) - 1
  water = 0
  while i < j:
    water = max(water, (j - i) * min(height[i], height[j]))
    if height[i] < height[j]:
      i += 1
    else:
      j -= 1
  return water
```

{% endtab %}{% endtabs %}