# [LC_get-biggest-three-rhombus-sums-in-a-grid](https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid)

* en

  ```en
  Given an m x n integer matrix grid
  A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid
  The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell
  ```

* tc

  ```tc
  Input:
  grid = [
    [3,4,5,1,3],
    [3,3,4,2,3],
    [20,30,200,40,10],
    [1,5,5,4,1],
    [4,3,2,2,5]]

  Output: [228,216,211]
  ```

## Solution

* py

  ```py
  def getBiggestThree(self, grid):
    m, n, heap = len(grid), len(grid[0]), []

    def update(heap, num):
      if num not in heap:
        heappush(heap, num)
        if len(heap) > 3: heappop(heap)
      return heap

    for num in chain(*grid): update(heap, num)

    @lru_cache(None)
    def dp(i, j, dr):
      if not 0 <= i < n or not 0 <= j < m: return 0
      return dp(i-1, j+dr, dr) + grid[j][i]

    for q in range(1, (1 + min(m, n))//2):
      for i in range(q, n - q):
        for j in range(q, m - q):
          p1 = dp(i + q, j, -1) - dp(i, j - q, -1)
          p2 = dp(i - 1, j + q - 1, -1) - dp(i - q - 1, j - 1, -1)
          p3 = dp(i, j - q, 1) - dp(i - q, j, 1)
          p4 = dp(i + q - 1, j + 1, 1) - dp(i - 1, j + q + 1, 1)
          update(heap, p1 + p2 + p3 + p4)

    return sorted(heap)[::-1]
  ```
