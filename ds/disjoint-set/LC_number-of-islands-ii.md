# [LC_number-of-islands-ii](https://leetcode.com/problems/number-of-islands-ii)

```en
Return an array of integers answer where answer[i] is # islands after turning cell (ri, ci) into a land
Island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically
```

```txt
Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]

Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]
```

## Solution

* py

  ```py
  def numIslands2(self, m, n, positions):
    counts, main, land = [], {}, {}
    for i, j in positions:
      p = i, j
      main[p], land[p] = p, [p]
      for q in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
        p, q = main[p], main.get(q)
        if not q or p == q:
          continue
        if len(land[p]) < len(land[q]):
          p, q = q, p
        land[p] += land[q]
        for l in land.pop(q):
          main[l] = p
      counts += len(land),
    return counts
  ```
