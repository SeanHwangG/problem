{% tabs %}{% tab title='LC_70.md' %}

* You are climbing staircase which takes n steps to reach top
* Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

```txt
Input: n = 2
Output: 2
```

{% endtab %}{% tab title='LC_70.go' %}

```go
func climbStairs(n int) int {
  a := 1
  b := 1
  for ; n > 0; n-- {
    a, b = b, a+b
  }
  return a
}
```

{% endtab %}{% tab title='LC_70.py' %}

```py
def climbStairs(self, n):
  return int((5 ** .5 / 5) * (((1 + 5 ** .5) / 2) ** (n + 1) - ((1 - 5 ** .5) / 2) ** (n + 1)))
```

{% endtab %}{% endtabs %}
