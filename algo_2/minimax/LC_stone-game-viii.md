# [LC_stone-game-viii](https://leetcode.com/problems/stone-game-viii)

* en

  ```en
  n stones arranged in a row. On each player's turn, while the number of stones is more than one, do the following:
  Choose an integer x > 1, and remove the leftmost x stones from the row
    Add the sum of the removed stones' values to the player's score
    Place a new stone, whose value is equal to that sum, on the left side of the row
  Game stops when only one stone is left in the row
  Given Alice starting, find score difference between Alice and Bob if they both play optimally
  ```

* tc

  ```tc
  Input: stones = [-1,2,-3,4,-5]
  Output: 5
  ```

## Solution

* py

  ```py
  def stoneGameVIII(self, stones):
    ans = sum(stones)
    for num in list(accumulate(stones))[::-1][1:-1]:
      ans = max(ans, num - ans)
    return ans
  ```
