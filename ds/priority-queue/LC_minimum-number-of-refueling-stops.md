# [LC_minimum-number-of-refueling-stops](https://leetcode.com/problems/minimum-number-of-refueling-stops)

* en

  ```en
  Gas stations[i] = [positioni, fueli] indicates ith station is i miles east with fueli gas
  Car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it
  Return minimum number of refueling stops the car must make in order to reach its destination
  ```

* tc

  ```tc
  Input: target = 1, startFuel = 1, stations = []
  Output: 0

  Input: target = 100, startFuel = 1, stations = [[10,100]]
  Output: -1
  ```

## Solution

* py

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
