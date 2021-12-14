{% tabs %}{% tab title='LC_818.py' %}

1. Go pass our target, stop and turn back
    * We take n instructions of A.
    * 1 + 2 + 4 + ... + 2 ^ (n-1) = 2 ^ n - 1
    * Then we turn back by one R instruction.
    * In the end, we get closer by n + 1 instructions.

2. Go as far as possible before pass target, stop and turn back
    * We take n - 1 instruction of A and one R.
    * Then we take m instructions of A, where m < n

* Time; O(TlogT)
* Space; O(T)

```py
@lru_cache(None)
def racecar(self, t: int) -> int:
  if t == 0:
    return 0
  n = t.bit_length()
  if 2 ** n - 1 == t:
    return n
  else:
    mn = self.racecar(2 ** n - 1 - t) + n + 1
    for m in range(n - 1):
      mn = min(mn, self.racecar(t - 2 ** (n - 1) + 2 ** m) + n + m + 1)
  return mn
```

{% endtab %}{% endtabs %}
