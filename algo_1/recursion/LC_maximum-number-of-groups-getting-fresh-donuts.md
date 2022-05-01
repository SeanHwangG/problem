# [LC_maximum-number-of-groups-getting-fresh-donuts](https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts)

Given integer batchSize and an integer array groups, where groups[i] denotes that they will buy groups[i] donuts
When group visits shop, all customers of group must be served before serving any of following group
Group is happy if first customer of group doesn't receive leftover donut from previous group
Rearrange ordering of groups, return maximum possible number of happy groups after rearranging the groups

```txt
Input: batchSize = 3, groups = [1,2,3,4,5,6]
Output: 4  # [6,2,4,5,1,3] makes 1, 2, 4, 6 happy

Input: batchSize = 4, groups = [1,3,2,5,2,2,1,6]
Output: 4
```

## Solution

* Time: O((n/K)^K * K)
* Space: O((n/K)^K * K)

* py

  ```py
  def maxHappyGroups(self, batch_size: int, groups: List[int]) -> int:
    @lru_cache(None)
    def dp(remains: tuple, waiting: int) -> int:
      ans = 0
      for i in range(batch_size):
        if remains[i] > 0:
          next_remains = tuple(remain - int(i == j) for j, remain in enumerate(remains))
          rest = (waiting + i) % batch_size
          ans = max(ans, dp(next_remains, rest) + (waiting == 0))
      return ans

    remains = [0] * batch_size
    for group in groups:
      remains[group % batch_size] += 1
    ans, remains[0] = remains[0], 0
    for i in range(1, batch_size):
      happy = min(remains[i], remains[batch_size-i])
      if i == batch_size - i:
        happy = remains[i] // 2
      ans += happy
      remains[i] -= happy
      remains[batch_size - i] -= happy
    return ans + dp(tuple(remains), 0)
  ```
