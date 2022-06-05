# [LC_best-meeting-point](https://leetcode.com/problems/best-meeting-point)

```en
Given m x n binary grid grid where each 1 marks home of one friend, return min total travel distance
Total travel distance is sum of distances between houses of friends and the meeting point
```

```txt
Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 6

Input: grid = [[1,1]]
Output: 1
```

## Solution

* Median of all ones

* py

  ```py
  def minTotalDistance(self, grid: List[List[int]]) -> int:
    total = 0
    for grid in grid, zip(*grid):
      X = []
      for x, row in enumerate(grid):
        X += [x] * sum(row)
      total += sum(abs(x - X[len(X) // 2]) for x in X)
    return total
  ```
