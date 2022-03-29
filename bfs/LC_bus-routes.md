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
