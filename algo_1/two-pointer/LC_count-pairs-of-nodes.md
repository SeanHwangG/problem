# [LC_count-pairs-of-nodes](https://leetcode.com/problems/count-pairs-of-nodes)

* en

  ```en
  Undirected graph with n # nodes, and an integer array queries are given
  Answer to jth query is # pairs of nodes (a, b) that satisfy following conditions:
    a < b
    cnt is strictly greater than queries[j], where cnt is # edges incident to a or b
  Return array answers where answers[j] is answer of jth query
  ```

* tc

  ```tc
  Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
  Output: [6,5]
  ```

## Solution

* py

  ```py
  def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
    v2count, res = Counter(v for edge in edges for v in edge), [0] * len(queries)
    shared = Counter((min(n1, n2), max(n1, n2)) for n1, n2 in edges)
    sorted_cnt = sorted(list(v2count.values()) + [0] * (n + 1 - len(v2count)))
    for k, q in enumerate(queries):
      i, j = 1, n
      while i < j:
        if q < sorted_cnt[i] + sorted_cnt[j]:   # for each j add all ignoring intersection
          res[k] += j - i
          j -= 1
        else:
          i += 1
      for (i, j), sh_cnt in shared.items():
        if q < v2count[i] + v2count[j] <= q + sh_cnt:
          res[k] -= 1
    return res
  ```
