# [LC_guess-number-higher-or-lower-ii](https://leetcode.com/problems/guess-number-higher-or-lower-ii)

* en

  ```en
  We are playing the Guessing Game. The game will work as follows:
  I pick a number between 1 and n
  You guess a number
  If you guess right number, you win the game
  If you guess wrong number, then tell you whether picked number is higher or lower, and will continue guessing
  Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game

  ```

* tc

  ```tc
  Input: 10
  Output: 16  # Guess 7 first then 9 or (3, 5)
  ```

## Solution

* py

  ```py
  def getMoneyAmount(self, n: int) -> int:
    @lru_cache(maxsize=None)
    def recur(l, r):
      if l >= r: return 0
      return min(i + max(recur(l, i - 1), recur(i + 1, r)) for i in range(l, r + 1))
    return recur(1, n)
  ```
