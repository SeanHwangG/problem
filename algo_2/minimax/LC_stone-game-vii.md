# [LC_stone-game-vii](https://leetcode.com/problems/stone-game-vii)

* en

  ```en
  There are n stones arranged in a row
  On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row
  And receive points equal to the sum of the remaining stones' values in the row
  The winner is the one with the higher score when there are no stones left to remove
  ```

* tc

  ```tc
  Input: stones = [5,3,1,4,2]
  Output: 6
  ```

## Solution

* cpp

  ```cpp
  int dp[1001][1001] = {};
  int dfs(vector<int>& s, int i, int j, int sum) {
    if (i == j)
      return 0;
    return dp[i][j] ? dp[i][j] : dp[i][j] = max(sum - s[i] - dfs(s, i + 1, j, sum - s[i]),
      sum - s[j] - dfs(s, i, j - 1, sum - s[j]));
  }
  int stoneGameVII(vector<int>& s) {
    return dfs(s, 0, s.size() - 1, accumulate(begin(s), end(s), 0));
  }
  ```

* py

  ```py
  def stoneGameVII(self, s: List[int]) -> int:
    dp = [[0] * len(s) for _ in range(len(s))]
    p_sum = [0] + list(accumulate(s))
    def dfs(i, j):
      if i == j:
        return 0
      if dp[i][j] == 0:
        dp[i][j] = p_sum[j + 1] - p_sum[i] - min(s[i] + dfs(i + 1, j), s[j] + dfs(i, j - 1))
      return dp[i][j]
    return dfs(0, len(s) - 1)
  ```
