# [LC_coin-change-2](https://leetcode.com/problems/coin-change-2)

* en

  ```en
  Given integer coins representing coins of different denominations and integer amount representing total money
  Return # combinations that make up that amount
  If that amount of money cannot be made up by any combination of the coins, return 0.
  Have an infinite number of each kind of coin
  ```

* tc

  ```tc
  Input: amount = 5, coins = [1,2,5]
  Output: 4

  Input: amount = 10, coins = [10]
  Output: 1
  ```

## Solution

* py

  ```py
  def change(self, amount: int, coins: List[int]) -> int:
    dp = [1] + [0] * amount
    for c in coins:
      for i in range(c, amount + 1):
        dp[i] += dp[i-c]
    return dp[amount]
  ```
