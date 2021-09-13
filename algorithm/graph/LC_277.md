{% tabs %}{% tab title='LC_277.md' %}

* Definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them
* Given a helper function bool knows(a, b) which tells you whether A knows B
* Return celebrity's label if there is a celebrity in the party. If none, return -1.

```txt
Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1

Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
```

{% endtab %}{% tab title='LC_277.py' %}

* Time: O(N)
* Space: O(1)

```py
# def knows(a: int, b: int) -> bool:
def findCelebrity(self, n: int) -> int:
  x = 0
  for i in range(n):
    if knows(x, i):
      x = i
  if any(knows(x, i) for i in range(x)):
    return -1
  if any(not knows(i, x) for i in range(n)):
    return -1
  return x
```

{% endtab %}{% endtabs %}
