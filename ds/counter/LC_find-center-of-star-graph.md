# [LC_find-center-of-star-graph](https://leetcode.com/problems/find-center-of-star-graph)

```en
Find most common item in 2d list
```

```txt
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
```

## Solution

* py

  ```py
  def findCenter(self, edges: List[List[int]]) -> int:
    return collections.Counter([v for edge in edges for v in edge]).most_common()[0][0]
  ```
