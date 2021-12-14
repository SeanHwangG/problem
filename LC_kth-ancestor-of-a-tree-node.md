{% tabs %}{% tab title='LC_1483.py' %}

* A is the parent in 1 step
* Based on this, we can find the parent in 2 steps, ... parent in 4 steps

```py
step = 15
def __init__(self, n, A):
  A = dict(enumerate(A))
  jump = [A]
  for s in range(self.step):
    B = {}
    for i, a in A.items():
      if a in A:
        B[i] = A[a]
    jump.append(B)
    A = B
  self.jump = jump

def getKthAncestor(self, x, k):
  step = self.step
  while k > 0 and x > -1:
    if k >= 1 << step:
      x = self.jump[step].get(x, -1)
      k -= 1 << step
    else:
      step -= 1
  return x
```

{% endtab %}{% endtabs %}
