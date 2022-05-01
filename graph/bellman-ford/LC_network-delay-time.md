# [LC_network-delay-time](https://leetcode.com/problems/network-delay-time)

Given a network of n nodes, labeled from 1 to n, and times, directed edges of travel times times[i] = (ui, vi, wi)
Where ui is source node, vi is target node, and wi is time it takes for a signal to travel from source to target
Send signal from given node k. Return time it takes for all n nodes to receive signal, return -1 if impossible


```txt
Input: times =
[[2,1,1],
 [2,3,1],
 [3,4,1]], n = 4, k = 2
Output: 2
```

## Solution

* Time: O(VE)
* Space: O(N)

* py

  ```py
  def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
    dist = [float("inf") for _ in range(N)]
    dist[K - 1] = 0
    for _ in range(N - 1):
      for u, v, w in times:
        if dist[u - 1] + w < dist[v - 1]:
          dist[v - 1] = dist[u - 1] + w
    return max(dist) if max(dist) < float("inf") else -1
  ```
