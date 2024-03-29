# [LC_number-of-ways-of-cutting-a-pizza](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza)

* en

  ```en
  Given rectangular pizza represented as rows x cols matrix containing following characters:
  'A' (apple), '.' (empty cell) and given integer k You have to cut the pizza into k pieces using k-1 cuts
  For each cut choose direction: vertical/horizontal, then choose cut position at cell boundary and cut into two pieces
  If you cut pizza vertically, give left part of pizza to a person. If horizontally, give upper part of pizza to a person
  Give last piece of pizza to last person
  Return number of ways of cutting the pizza such that each piece contains at least one apple modulo 1e9 + 7
  ```

* tc

  ```tc
  Input: pizza = ["A..","AAA","..."], k = 3
  Output: 3

  Input: pizza = ["A..","AA.","..."], k = 3
  Output: 1
  ```

## Solution

* py

  ```py
  def ways(self, pizza: List[str], K: int) -> int:
    m, n, MOD = len(pizza), len(pizza[0]), 10 ** 9 + 7
    pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
    for r in range(m - 1, -1, -1):
      for c in range(n - 1, -1, -1):
        pre_sum[r][c] = pre_sum[r][c + 1] + pre_sum[r + 1][c] - pre_sum[r + 1][c + 1] + (pizza[r][c] == 'A')

    @lru_cache(None)
    def dp(k, r, c):
      if pre_sum[r][c] == 0: return 0
      if k == 0: return 1
      ans = 0
      for nr in range(r + 1, m): # cut horizontally
        if pre_sum[r][c] - pre_sum[nr][c] > 0:
          ans = (ans + dp(k - 1, nr, c)) % MOD
      for nc in range(c + 1, n): # cut vertically
        if pre_sum[r][c] - pre_sum[r][nc] > 0:
          ans = (ans + dp(k - 1, r, nc)) % MOD
      return ans

    return dp(K - 1, 0, 0)
  ```
