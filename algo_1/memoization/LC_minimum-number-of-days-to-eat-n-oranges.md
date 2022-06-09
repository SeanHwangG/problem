# [LC_minimum-number-of-days-to-eat-n-oranges](https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges)

* en

  ```en
  There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:
  Eat one orange
  If the number of remaining oranges (n) is divisible by 2 then you can eat  n/2 oranges
  If the number of remaining oranges (n) is divisible by 3 then you can eat  2*(n/3) oranges
  ```

* tc

  ```tc
  Input: n = 10
  Output: 4
  ```

## Solution

* cpp

  ```cpp
  unordered_map<int, int> dp;
  int minDays(int n) {
    if (n <= 1)
      return n;
    if (dp.count(n) == 0)
      dp[n] = 1 + min(n % 2 + minDays(n / 2), n % 3 + minDays(n / 3));
    return dp[n];
  }
  ```

* py

  ```py
  @lru_cache()
  def minDays(self, n: int) -> int:
    if n <= 1:
      return n
    return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))
  ```
