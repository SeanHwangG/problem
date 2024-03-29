# [LC_tallest-billboard](https://leetcode.com/problems/tallest-billboard)

* en

  ```en
  Installing a billboard and want it to have the largest height
  Billboard will have two steel supports, one on each side. Each steel support must be an equal height.
  Given a collection of rods that can be welded together
  Return largest possible height of your billboard installation. If you cannot support the billboard, return 0
  ```

* tc

  ```tc
  Input: rods = [1,2,3,6]
  Output: 6  # 123, 6

  Input: rods = [1,2,3,4,5,6]
  Output: 10 # 235, 46
  ```

## Solution

* py

  ```py
  def tallestBillboard(self, rods: List[int]) -> int:
    dp = {0: 0}
    for i in rods:
      cur = collections.defaultdict(int)
      for s in dp:
        cur[s + i] = max(dp[s] + i, cur[s + i])
        cur[s] = max(dp[s], cur[s])
        cur[s-i] = max(dp[s], cur[s - i])
      dp = cur
    return dp[0]
  ```
