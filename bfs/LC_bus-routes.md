# [LC_bus-routes](https://leetcode.com/problems/bus-routes)

Start at bus stop source (not on any bus initially), and you want to go to bus stop target
Return least number of buses you must take to travel from source to target. Return -1 if it's impossible

```txt
Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
```

## Solution

```py
def numBusesToDestination(self, routes, S, T):
  G = collections.defaultdict(set)
  for i, route in enumerate(routes):
    for j in route:
      G[j].add(i)
  bfs = [(S, 0)]
  seen = set([S])
  for stop, bus in bfs:
    if stop == T: return bus
    for i in G[stop]:
      for j in routes[i]:
        if j not in seen:
          bfs.append((j, bus + 1))
          seen.add(j)
      routes[i] = []  # seen route
  return -1
```
