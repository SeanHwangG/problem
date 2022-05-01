# [LC_stone-game-iv](https://leetcode.com/problems/stone-game-iv)

Alice and Bob take turns playing a game, with Alice starting first, initially, given n stones in pile
On each player's turn, that player move consisting of removing any non-zero square number of stones in pile
Also, if a player cannot make a move, he/she loses game
Given positive integer n, return if and only if Alice wins game, assuming both players play optimally

```txt
Input: n = 1
Output: true

Input: n = 2
Output: false

Input: n = 7
Output: false
```

## Solution

* py

  ```py
  def winnerSquareGame(self, n: int) -> bool:
    dp = [False] * (n + 1)
    for i in range(1, n + 1):
      dp[i] = not all(dp[i - k * k] for k in range(1, int(i ** 0.5) + 1))
    return dp[-1]
  ```
