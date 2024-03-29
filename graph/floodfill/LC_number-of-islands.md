# [LC_number-of-islands](https://leetcode.com/problems/number-of-islands)

* en

  ```en
  Find number of island
  ```

* tc

  ```tc
  Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]

  Output: 1
  ```

## Solution

* cpp

  ```cpp
  int numIslands(vector<vector<char>>& grid) {
    int m = grid.size(), n = m ? grid[0].size() : 0, islands = 0;
    for (int i = 0; i < m; i++)
      for (int j = 0; j < n; j++)
        if (grid[i][j] == '1') {
          islands++;
          floodfill(grid, i, j);
        }
    return islands;
  }
  void floodfill(vector<vector<char>>& grid, int i, int j) {
    int m = grid.size(), n = grid[0].size();
    if (i < 0 || i == m || j < 0 || j == n || grid[i][j] == '0')
      return;
    grid[i][j] = '0';
    floodfill(grid, i - 1, j);
    floodfill(grid, i + 1, j);
    floodfill(grid, i, j - 1);
    floodfill(grid, i, j + 1);
  }
  ```

* py

  ```py
  def numIslands(self, grid):
    def floodfill(i, j):
      if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
        grid[i][j] = '0'
        list(map(floodfill, (i+1, i-1, i, i), (j, j, j+1, j-1)))
        return 1
      return 0
    return sum(floodfill(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
  ```
