# [LC_24-game](https://leetcode.com/problems/24-game)

* en

  ```en
  Given integer array cards of length 4 each containing a number in the range [1, 9]
  Arrange numbers on these cards in a mathematical expression using ['+', '-', '*', '/', '(' and ')' to get 24
  ```

* tc

  ```tc
  Input: cards = [4,1,8,7]
  Output: true  # (8-4) * (7-1) = 24

  Input: cards = [1,2,1,2]
  Output: false
  ```

## Solution

* py

  ```py
  def judgePoint24(self, nums: List[int]) -> bool:
    if len(nums) == 1:
      return math.isclose(nums[0], 24)
    return any(self.judgePoint24([x] + rest)
              for a, b, *rest in itertools.permutations(nums)
              for x in {a + b, a - b, a * b, b and a / b})
  ```
