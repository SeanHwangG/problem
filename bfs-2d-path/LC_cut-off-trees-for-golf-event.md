# [LC_cut-off-trees-for-golf-event](https://leetcode.com/problems/cut-off-trees-for-golf-event)

0 means cell cannot be walked through, 1 represents an empty cell that can be walked through
Number greater than 1 represents a tree in a cell that can be walked through, and this number is tree's height
Starting from point (0, 0), return min steps you need to walk to cut off all trees. If you cannot, return -1

```txt
Input: forest =
[[1,2,3],
 [0,0,4],
 [7,6,5]]
Output: 6
```

## Solution

* Hadlock's algorithm

```py
def cutOffTree(self, forest: List[List[int]]) -> int:
  # Add sentinels (a border of zeros) so we don't need index-checks later on.
  forest.append([0] * len(forest[0]))
  for row in forest:
    row.append(0)

  trees = [(height, i, j) for i, row in enumerate(forest) for j, height in enumerate(row) if height > 1]

  # Can we reach every tree? If not, return -1 right away.
  queue, reached = [(0, 0)], set()
  for i, j in queue:
    if (i, j) not in reached and forest[i][j]:
      reached.add((i, j))
      queue += (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
  if not all((i, j) in reached for (_, i, j) in trees):
    return -1

  def distance(i, j, I, J):
    now, soon, expanded = [(i, j)], [], set()
    manhattan, detours = abs(i - I) + abs(j - J), 0
    while True:
      if not now:
        now, soon = soon, []
        detours += 1
      i, j = now.pop()
      if (i, j) == (I, J):
        return manhattan + 2 * detours
      if (i, j) in expanded:
        continue
      expanded.add((i, j))
      for i, j, closer in (i + 1, j, i < I), (i - 1, j, i > I), (i, j + 1, j < J), (i, j - 1, j > J):
        if forest[i][j]:
          (now if closer else soon).append((i, j))

  trees.sort()
  return sum(distance(i, j, I, J) for (_, i, j), (_, I, J) in zip([(0, 0, 0)] + trees, trees))
```
