{% tabs %}{% tab title='LC_60.py' %}

```py
class Solution:
  def getPermutation(self, n: int, k: int) -> str:
    elements = list(range(1, n+1))
    NN = reduce(operator.mul, elements) # n!
    k, result = (k - 1) % NN, ''
    while len(elements) > 0:
      NN //= len(elements)
      i, k = k // NN, k % NN
      result += str(elements.pop(i))
    return result
```

{% endtab %}{% endtabs %}
