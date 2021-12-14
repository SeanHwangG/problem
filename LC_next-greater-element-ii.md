{% tabs %}{% tab title='LC_503.py' %}

```py
def nextGreaterElements(self, nums: List[int]) -> List[int]:
  stack, res = [], [-1] * len(A)
  for i in range(len(A)) * 2:
    while stack and (A[stack[-1]] < A[i]):
      res[stack.pop()] = A[i]
    stack.append(i)
  return res
```

{% endtab %}{% endtabs %}
