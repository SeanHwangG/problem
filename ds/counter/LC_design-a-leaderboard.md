# [LC_design-a-leaderboard](https://leetcode.com/problems/design-a-leaderboard)

* en

  ```en
  Design a Leaderboard class, which has 3 functions:
  addScore(playerId, score): Update the leaderboard by adding score to the given player's score
    If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
  top(K): Return the score sum of the top K players.
  reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard)
    It is guaranteed that the player was added to the leaderboard before calling this function.
  ```

* tc

  ```tc
  Input:
  ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
  [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]

  Output:
  [null,null,null,null,null,null,73,null,null,null,141]
  ```

## Solution

* py

  ```py
  class Leaderboard(object):
    def __init__(self):
      self.A = collections.Counter()

    def addScore(self, playerId, score):
      self.A[playerId] += score

    def top(self, K):
      return sum(v for i,v in self.A.most_common(K))

    def reset(self, playerId):
      self.A[playerId] = 0
  ```
