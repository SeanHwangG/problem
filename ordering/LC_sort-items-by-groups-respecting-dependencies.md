# [LC_sort-items-by-groups-respecting-dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies)

There are n items each belonging to zero or one of m groups where group[i] is group that i-th item belongs
It's equal to -1 if i-th item belongs to no group. items and groups are zero indexed (Group can have no item)
Return sorted list of the items such that:
Items that belong to same group are next to each other in the sorted list
beforeItems[i] is list containing all items that should come before i-th item in sorted array (to left of i-th item)
Return any solution if there is more than one solution and return an empty list if there is no solution

```txt
Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
```

## Solution

* Time; O(V + E)

```py
def sortItems(self, n: int, m: int, group: List[int], prereqs: List[List[int]]) -> List[int]:
  def topo_sort(points, pre, suc):
    order, sources = [], [p for p in points if not pre[p]]
    while sources:
      s = sources.pop()
      order.append(s)
      for u in suc[s]:
        pre[u].remove(s)
        if not pre[u]:
          sources.append(u)
    return order if len(order) == len(points) else []

  group2item = defaultdict(set)
  for i in range(n):
    if group[i] == -1:  # Assign random group
      group[i] = m
      m += 1
    group2item[group[i]].add(i)
  # find relationships between the groups and each items in same group
  t_pre, t_suc = defaultdict(set), defaultdict(set)
  g_pre, g_suc = defaultdict(set), defaultdict(set)
  for i in range(n):
    for j in beforeItems[i]:
      if group[i] == group[j]:
        t_pre[i].add(j)
        t_suc[j].add(i)
      else:
        g_pre[group[i]].add(group[j])
        g_suc[group[j]].add(group[i])
  groups_order = topo_sort([i for i in group2item], g_pre, g_suc) # Topo Sort Group
  t_order = []
  for i in groups_order:
    items = group2item[i]
    i_order = topo_sort(items, t_pre, t_suc)  # Topo Sort items in each group
    if len(i_order) != len(items):
      return []
    t_order += i_order
  return t_order if len(t_order) == n else []
```
