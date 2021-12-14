{% tabs %}{% tab title='LC_699.py' %}

```py
def fallingSquares(self, positions: List[List[int]]) -> List[int]:
  height, pos, res = [0], [0], [0]
  for left, side in positions:
    i, j = bisect_right(pos, left), bisect_left(pos, left + side)
    high = max(height[i - 1: j] or [0]) + side
    pos[i:j] = [left, left + side]
    height[i:j] = [high, height[j - 1]]
    res.append(max(res[-1], high))
  return res[1:]
```

{% endtab %}{% endtabs %}
