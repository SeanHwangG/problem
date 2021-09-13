{% tabs %}{% tab title='LC_871.md' %}

* Gas stations[i] = [positioni, fueli] indicates ith station is i miles east with fueli gas
* The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it
* Return minimum number of refueling stops the car must make in order to reach its destination

```txt
Input: target = 1, startFuel = 1, stations = []
Output: 0

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
```

{% endtab %}{% tab title='LC_871.py' %}

```py
def minRefuelStops(self, target: int, cur: int, s: List[List[int]]) -> int:
  pq, res, i = [], 0, 0
  while cur < target:
    while i < len(s) and s[i][0] <= cur:
      heapq.heappush(pq, -s[i][1])
      i += 1
    if not pq: return -1
    cur -= heapq.heappop(pq)
    res += 1
  return res
```

{% endtab %}{% endtabs %}
