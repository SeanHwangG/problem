# [LC_most-stones-removed-with-same-row-or-column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column)

Stone can be removed if it shares either the same row or the same column
Return largest possible number of stones that can be removed

```txt
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
```

## Solution

```cpp
int removeStones(vector<vector<int>>& stones) {
  for (int i = 0; i < stones.size(); ++i)
    uni(stones[i][0], ~stones[i][1]);
  return stones.size() - islands;
}

unordered_map<int, int> f;
int islands = 0;

int find(int x) {
  if (!f.count(x)) f[x] = x, islands++;
  if (x != f[x]) f[x] = find(f[x]);
  return f[x];
}

void uni(int x, int y) {
  x = find(x), y = find(y);
  if (x != y) f[x] = y, islands--;
}
```

```py
def removeStones(self, points):
  UF = {}
  def find(x):
    if x != UF[x]:
      UF[x] = find(UF[x])
    return UF[x]
  def union(x, y):
    UF.setdefault(x, x)
    UF.setdefault(y, y)
    UF[find(x)] = find(y)

  for i, j in points:
    union(i, ~j)
  return len(points) - len({find(x) for x in UF})
```
