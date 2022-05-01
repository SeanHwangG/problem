# [LC_minimum-interval-to-include-each-query](https://leetcode.com/problems/minimum-interval-to-include-each-query)

Given a 2D integer array intervals, where intervals[i] = [lefti, righti] (inclusive)
You are also given an integer array queries
Answer to jth query is size of the smallest interval i st lefti <= queries[j] <= righti, -1 if no such interval exists
Return an array containing the answers to the queries

```txt
Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
```

## Solution

* Time; O(N log N)

* py

  ```py
  def minInterval(self, li: List[List[int]], queries: List[int]) -> List[int]:
    li = sorted(li)[::-1]
    pq, res = [], {}
    for q in sorted(queries):
      while li and li[-1][0] <= q:
        i, j = li.pop()
        if j >= q:
          heapq.heappush(pq, [j - i + 1, j])
      while pq and pq[0][1] < q:
        heapq.heappop(pq)
      res[q] = pq[0][0] if pq else -1
    return [res[q] for q in queries]
  ```
